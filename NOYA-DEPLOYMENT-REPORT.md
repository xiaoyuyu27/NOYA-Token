# NOYA DEPLOYMENT REPORT — 主网已部署，链上已核验，BaseScan 已验证，GitHub 已公开

> 部署已发生：合约地址与区块高度为链上实测值（Base RPC eth_getCode / eth_call 核验），交易哈希为用户部署页日志截图所载（截图读取可能截断，待用户以文字回传后以回执再核对一次）。BaseScan 源码验证已通过，GitHub 公开仓库已创建并推送（https://github.com/xiaoyuyu27/NOYA-Token，首推提交 602bb86be79c31d206f1666bf4d374ef34fb54a4）。

## Token 参数

- Token 名称：NOYA
- Token 符号：NOYA
- 总发行量：100,000,000
- 精度：18
- 网络：Base Mainnet
- Chain ID：8453（RPC 实测返回 0x2105，已核验，禁止用 Base Sepolia 冒充）
- RPC：https://mainnet.base.org
- Explorer：https://basescan.org
- 标准：ERC-20（OpenZeppelin 5.0.2）
- Solidity：0.8.24（锁定）
- Hardhat：2.28.0
- 编译配置：optimizer enabled runs 200，evmVersion paris
- 合约类型：非代理

## 部署信息（链上已核验）

- 合约地址：0x0e0147e45f87649097b85214c4d0705d6caa8ad6
- 部署交易哈希：0xfaeb88b9f3c2b3574d38ae435226b8f33387d371a33007f2cacf41eeb6d957（部署页日志截图所载，截图读取长度疑似不足 66 字符，待用户以文字回传后以 eth_getTransactionReceipt 再核对）
- 区块高度：53450235（部署页日志所载；链上 eth_call 已确认该地址存在合约代码）
- 部署钱包：0xCAc8F76a31586AdAc44deeEF11fa66A8B282eeCa（Account 1，MetaMask 连接页所载）
- 接收钱包：0xCAc8F76a31586AdAc44deeEF11fa66A8B282eeCa（部署钱包与接收钱包为同一地址）
- 链上核验（Base RPC，2026-11-03）：eth_chainId 0x2105；合约代码存在；totalSupply = 100000000000000000000000000（即 100,000,000 × 10^18）；decimals = 18；接收钱包 balanceOf = totalSupply（全量已到接收钱包）
- 源码验证链接：已通过 Pass - Verified（2026-11-03，Etherscan API V2，Solidity 0.8.24 v0.8.24+commit.e11b9ed9，optimizer 200，EVM paris，MIT，非代理）；源码已在 BaseScan 公开可读，详见 verification/VERIFIED-2026-11-03.md
- 部署时间：2026-11-03（用户 MetaMask 签名广播当日，具体区块时间待回执核对）
- BaseScan 合约页：https://basescan.org/address/0x0e0147e45f87649097b85214c4d0705d6caa8ad6

## 测试结果（真实执行，非伪造）

- 环境：Node v24.22.1，npm 10.9.4
- 编译：`npx hardhat compile` — Compiled 6 Solidity files successfully，无警告输出
- 测试：`npx hardhat test` — 8 passing
  - 名称 / 符号 / 精度：NOYA / NOYA / 18 ✔
  - 总供应量：100,000,000 ✔
  - 初始接收钱包余额 = 全量，部署者余额 = 0 ✔
  - 普通转账 ✔
  - 授权 + transferFrom ✔
  - 超额转账 revert ✔
  - ABI 中无 mint / burn / owner / pause / blacklist / setTax / setFee / freeze 入口 ✔
  - 构造函数拒绝零地址 ✔
- 原始日志：audit/noya-compile.log、audit/noya-test.log

## 安全检查结果

- Slither 0.11.6：5 条结果，全部 INFO 级，无 High / Medium / Low（原始日志 audit/noya-slither.log）
- _mint 仅在构造函数出现 1 次；ABI 函数仅为标准 ERC-20 + TOTAL_SUPPLY 常量
- 无增发、无税、无黑名单、无冻结、无交易限制、无管理员、无代理、无外部收费合约、无后门函数
- 详见 audit/SECURITY-REPORT.md

## 交付目录

NOYA-Token-Delivery/
- contracts/NOYA.sol
- scripts/deploy.js（强制校验 chainId 8453 与接收地址）
- test/NOYA.test.js
- audit/SECURITY-REPORT.md + 原始日志
- deployment/STATUS-NOT-DEPLOYED.md
- verification/STATUS-NOT-VERIFIED.md
- README.md、LICENSE（MIT）、package.json（锁定版本）、.env.example、.gitignore

## 进入主网部署前仍需用户确认（缺一不可）

1. 接收全部 1 亿枚的钱包地址（0x 开头 40 位十六进制）
2. 部署钱包地址及该钱包 Base 主网 ETH 余额是否足够付 Gas
3. MetaMask 是否已由用户本人装好（用户此前表示自己安装，当前状态未确认）
4. 是否以 noya.ai 官方名义发布：公开市场已有同名 NOYA 项目，本项目与官方的关系未经证实，对外宣传前需用户自行确认，避免混淆
5. 最终部署确认单逐项确认后，才由用户本人用 MetaMask 签名广播；助手不索要、不保存助记词或私钥
