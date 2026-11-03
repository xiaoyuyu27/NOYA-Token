# NOYA 最终部署确认单（部署前逐项确认，未确认不得广播）

## 固定参数

- Token：NOYA / NOYA
- 总量：100,000,000，精度：18，标准：ERC-20
- 网络：Base Mainnet，Chain ID 8453（0x2105）
- 合约：contracts/NOYA.sol，Solidity 0.8.24，OpenZeppelin 5.0.2，Optimizer runs 200，EVM paris，非代理，无增发/税/黑名单/冻结

## 钱包（用户 2026-11-02 提供，已链上核验）

- 接收钱包（将收到全部 1 亿枚）：0xCAc8F76a31586AdAc44deeEF11fa66A8B282eeCa
- 地址格式：42 位，0x + 40 位十六进制，校验通过
- Base 主网 ETH 余额（核验时）：0.005 ETH（0x11c37937e08000 wei）
- Base 主网交易计数（核验时）：0（该地址在 Base 上尚未有交易记录）
- 部署钱包：待用户确认是否与接收钱包为同一地址
  - 如为同一地址：部署钱包 = 0xCAc8F76a31586AdAc44deeEF11fa66A8B282eeCa
  - 如为不同地址：请用户另行提供部署钱包地址，并确认其 Base ETH 余额

## 部署前用户必须确认

- [x] 接收地址无误：0xCAc8F76a31586AdAc44deeEF11fa66A8B282eeCa，部署后无法更改（用户 2026-11-02 提供该地址）
- [x] 用户 2026-11-02 17:12 下达“部署”指令，视为按本确认单参数启动部署；实际广播仍需用户本人在 MetaMask 弹窗里签名，助手未签名、未广播
- [ ] MetaMask 已在电脑插件安装，网络已切到 Base 主网 8453（部署时由页面强制校验 0x2105）
- [ ] 部署钱包 Base ETH 足够付 Gas（最终 Gas 以 MetaMask 弹窗显示为准；核验时接收钱包余额 0.005 ETH）
- [ ] 是否以 noya.ai 官方名义发布已由用户自行确认（公开市场已有同名项目，关系未经证实）
- [ ] 用户本人在 MetaMask 弹窗里核对网络、接收地址、Gas 后才点确认

## 部署后待填（不得提前填写）

- 合约地址：
- 部署交易哈希：
- 区块高度：
- BaseScan 验证结果（目标 Exact Match）：
- GitHub Public 仓库链接：
