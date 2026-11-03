import json, pathlib
base = pathlib.Path.home() / "workspace/NOYA-Token-Delivery"
art = json.loads((base / "artifacts/contracts/NOYA.sol/NOYA.json").read_text())
bytecode = art["bytecode"]
assert bytecode.startswith("0x608060405234801562000011"), "unexpected bytecode prefix"
# No ethers CDN, no external JS: use window.ethereum directly.
# Deployment tx data = creation bytecode + ABI-encoded constructor arg
# (address, left-padded to 32 bytes). Gas is estimated by MetaMask.
page = r"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>NOYA 部署 v2 - Base 主网 / MetaMask 插件（无需外部库）</title>
<style>body{font-family:system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;max-width:760px;margin:32px auto;padding:0 20px;line-height:1.7;color:#111}h1{font-size:22px}button{padding:10px 18px;font-size:16px;cursor:pointer}button:disabled{opacity:.45;cursor:not-allowed}input{width:100%;padding:10px;font-size:15px;box-sizing:border-box}.warn{background:#fff4e5;border:1px solid #f0b429;padding:12px;border-radius:8px}.ok{color:#0a7a2f}.err{color:#b00020}pre{white-space:pre-wrap;word-break:break-all;background:#f7f7f7;padding:12px;border-radius:8px}</style></head>
<body>
<h1>NOYA 部署 v2（Base 主网 · MetaMask 浏览器插件）</h1>
<p class="warn"><b>只在电脑 Chrome + MetaMask 插件里打开本页。</b>本页不加载任何外部 JS 库，直接调用 MetaMask 自带的 provider；如果点按钮没反应，页面下方日志会直接显示报错原因，不会静默失败。本页不收集、不发送助记词或私钥，签名只在你自己的 MetaMask 弹窗里完成。</p>
<h2>固定参数（不可改）</h2>
<ul>
<li>名称 / 符号：NOYA / NOYA，总量：100,000,000，精度：18，标准：ERC-20</li>
<li>网络：Base Mainnet，Chain ID：8453（0x2105），RPC：https://mainnet.base.org</li>
<li>Solidity：0.8.24，OpenZeppelin：5.0.2，Optimizer：enabled runs 200，EVM：paris</li>
<li>机制：构造函数一次性向接收地址发全量，无增发、无税、无黑名单、无冻结、无代理</li>
</ul>
<button id="connect">1. 连接 MetaMask</button>
<p id="account">未连接</p>
<p id="chain">未检测网络</p>
<button id="switch">2. 切换到 Base 主网（如已在 Base 可跳过）</button>
<h2>3. 接收地址</h2>
<p>全部 1 亿枚 NOYA 将直接发到这个地址。部署后无法改，填错就等于发错人。</p>
<input id="recipient" placeholder="0x 开头的 40 位十六进制地址">
<p id="recipientCheck"></p>
<button id="deploy" disabled>4. 部署 NOYA（MetaMask 弹窗确认）</button>
<pre id="log">等待连接…</pre>
<p>部署成功后请记录：合约地址、交易哈希，并到 https://basescan.org 查合约，再用 Solidity 0.8.24 / Optimizer 200 / EVM paris / MIT License / 构造参数为接收地址，做源码验证，目标 Exact Match。</p>
<script>
const BYTECODE = "__BYTECODE__";
const logEl = document.getElementById('log');
function log(s){ logEl.textContent += "\n" + s; }
function isAddr(a){ return /^0x[0-9a-fA-F]{40}$/.test(a||''); }
let account = null;
function refreshDeployBtn(){
  const v = document.getElementById('recipient').value.trim();
  document.getElementById('deploy').disabled = !(account && isAddr(v));
}
document.getElementById('recipient').addEventListener('input', (e) => {
  const v = e.target.value.trim();
  const el = document.getElementById('recipientCheck');
  el.textContent = isAddr(v) ? '地址格式正确，请再逐字核对一次。' : '地址格式不对：必须是 0x 开头、共 42 个字符。';
  el.className = isAddr(v) ? 'ok' : 'err';
  refreshDeployBtn();
});
async function checkChain(){
  try {
    const id = await window.ethereum.request({method:'eth_chainId'});
    const el = document.getElementById('chain');
    el.textContent = '当前 Chain ID：' + id + (id === '0x2105' ? '（Base 主网，正确）' : '（不是 Base 主网，请切换）');
    el.className = id === '0x2105' ? 'ok' : 'err';
    return id;
  } catch(e){ log('检测网络失败：' + (e.message||e)); return null; }
}
document.getElementById('connect').onclick = async () => {
  try {
    if(!window.ethereum){ alert('未检测到 MetaMask：请确认本页是在 Chrome 里打开、MetaMask 已启用、且扩展详情里“允许访问文件网址”已打开，然后刷新再试。'); log('错误：window.ethereum 不存在'); return; }
    log('检测到 MetaMask，正在请求连接…');
    const accounts = await window.ethereum.request({method:'eth_requestAccounts'});
    account = accounts[0];
    document.getElementById('account').textContent = '已连接：' + account;
    log('已连接 ' + account);
    await checkChain();
    refreshDeployBtn();
    if(window.ethereum.on){ window.ethereum.on('chainChanged', () => location.reload()); }
  } catch(e){ log('连接失败：' + (e.code||'') + ' ' + (e.message||e)); alert('连接失败：' + (e.message||e)); }
};
document.getElementById('switch').onclick = async () => {
  try {
    await window.ethereum.request({method:'wallet_switchEthereumChain', params:[{chainId:'0x2105'}]});
  } catch(e) {
    if(e.code === 4902){
      await window.ethereum.request({method:'wallet_addEthereumChain', params:[{chainId:'0x2105', chainName:'Base', nativeCurrency:{name:'Ether',symbol:'ETH',decimals:18}, rpcUrls:['https://mainnet.base.org'], blockExplorerUrls:['https://basescan.org']}]});
    } else { log('切换失败：' + (e.message||e)); alert('切换失败：' + (e.message||e)); return; }
  }
  await checkChain(); log('已切换到 Base 主网');
};
function sleep(ms){ return new Promise(r => setTimeout(r, ms)); }
document.getElementById('deploy').onclick = async () => {
  try {
    const recipient = document.getElementById('recipient').value.trim();
    if(!isAddr(recipient)){ alert('接收地址格式不对'); return; }
    const chainId = await checkChain();
    if(chainId !== '0x2105'){ alert('当前不是 Base 主网（8453），已拒绝部署。'); return; }
    if(!confirm('最后确认：\n网络：Base 主网 8453\n部署钱包：' + account + '\n接收地址：' + recipient + '\n将向该地址发行全部 100,000,000 NOYA，部署后无法更改。\n点确定后请在 MetaMask 弹窗里再次核对 Gas 和网络再确认。')) return;
    const data = BYTECODE + recipient.slice(2).toLowerCase().padStart(64, '0');
    log('正在发送部署交易，请在 MetaMask 弹窗里确认…');
    const txHash = await window.ethereum.request({method:'eth_sendTransaction', params:[{from: account, data: data}]});
    log('交易已发送，哈希：' + txHash);
    log('等待链上确认中…');
    for(let i=0;i<120;i++){
      await sleep(3000);
      const receipt = await window.ethereum.request({method:'eth_getTransactionReceipt', params:[txHash]});
      if(receipt && receipt.contractAddress){
        log('部署成功！合约地址：' + receipt.contractAddress);
        log('区块高度：' + parseInt(receipt.blockNumber, 16));
        log('BaseScan：https://basescan.org/address/' + receipt.contractAddress);
        log('请立即记录合约地址和交易哈希，并做源码验证（0.8.24 / runs 200 / paris / MIT，构造参数为接收地址）。');
        return;
      }
    }
    log('超时未拿到回执，请用交易哈希到 BaseScan 查询：https://basescan.org/tx/' + txHash);
  } catch(e){ log('部署失败或被取消：' + (e.code||'') + ' ' + (e.message||e)); alert('部署失败或被取消：' + (e.message||e)); }
};
</script></body></html>
"""
page = page.replace("__BYTECODE__", bytecode)
out = base / "scripts/deploy-via-metamask-v2.html"
out.write_text(page)
print(f"wrote {out} bytes={len(page)} bytecode_len={len(bytecode)} external_js={'cdn.jsdelivr' in page or 'ethers' in page}")
