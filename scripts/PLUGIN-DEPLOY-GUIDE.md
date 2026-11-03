# 电脑浏览器插件部署指南（MetaMask）

适用：已在电脑 Chrome 安装官方 MetaMask 插件的用户。手机 App 不走本指南。

## 准备

1. 把 `scripts/deploy-via-metamask.html` 下载到电脑，用 Chrome 打开（不要用手机打开）。
2. MetaMask 里确认：
   - 钱包已解锁；
   - 网络是 Base 主网，Chain ID 8453（页面里有“切换到 Base 主网”按钮，点它会自动切换或添加）；
   - 部署钱包里有足够 ETH 付 Gas（Gas 多少以 MetaMask 弹窗显示为准，部署前先看，不要盲点确认）。
3. 准备好接收地址：全部 1 亿枚 NOYA 将直接发到这个地址，部署后无法更改。

## 部署步骤（按页面顺序点）

1. 点“连接 MetaMask”，在弹窗里选你要部署的钱包账号，核对地址无误。
2. 页面显示当前 Chain ID 为 `0x2105` 才继续；不是就点“切换到 Base 主网”。
3. 在接收地址框里粘贴地址，页面会先校验格式，你再逐字核对一遍（首尾字符 + 中间几位）。
4. 点“部署 NOYA”，先在页面二次确认框里核对网络 + 接收地址，再在 MetaMask 弹窗里核对网络、Gas、接收地址（构造参数），确认无误才点确认。
5. 等交易确认，页面会显示合约地址和交易哈希，立刻记下来。

## 部署后必做

1. 到 https://basescan.org/address/<合约地址> 核对：Name NOYA、Symbol NOYA、Decimals 18、Total Supply 100,000,000、接收钱包余额 100,000,000。
2. 做 BaseScan 源码验证，参数必须与本项目一致：
   - Solidity 0.8.24，Optimizer enabled runs 200，EVM paris，License MIT
   - 构造参数：接收地址（ABI 编码，页面部署成功后需另行从交易输入数据或 Hardhat 验证命令取）
   - 目标：Exact Match
3. 把合约地址、交易哈希、验证链接回填到 NOYA-DEPLOYMENT-REPORT.md，并创建 GitHub Public 仓库 NOYA-Token 上传全部源码。

## 安全红线

- 本页不收集助记词或私钥；任何让你在网页里填助记词/私钥的页面都是假的，立刻关掉。
- 如果 MetaMask 弹窗显示的网络不是 Base、接收地址不是你填的地址，取消，不要确认。
- 部署前没有最终确认单，就不要广播；本指南本身不是部署成功证明。
