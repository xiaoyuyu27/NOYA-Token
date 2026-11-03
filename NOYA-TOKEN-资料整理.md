# NOYA Token 资料整理（2026-11-03，全部经链上 / 平台实测核验）

![NOYA Logo](noya-logo-user.svg)

## 一、代币基本信息

- 代币名称：NOYA
- 代币符号：NOYA
- 总发行量：100,000,000
- 精度：18
- 标准：ERC-20（OpenZeppelin Contracts 5.0.2）
- 网络：Base Mainnet
- Chain ID：8453（0x2105）
- RPC：https://mainnet.base.org
- 浏览器：https://basescan.org
- 合约类型：非代理、无增发、无交易税、无黑名单、无冻结、无交易限制、无管理员、无外部收费合约、无后门函数
- 许可证：MIT

## 二、部署信息（已回执核验）

- 合约地址：0x0e0147e45f87649097b85214c4d0705d6caa8ad6
- 部署交易哈希：0xafaeb88b93f2c3b1574d8ae4835226b8f33387d371a33007f2cacf41eeb6d957
- 区块高度：53450235（0x32f95fb）
- 部署时间：2026-11-03 15:10:17 +08:00（回执区块时间）
- 部署钱包 = 接收钱包：0xCAc8F76a31586AdAc44deeEF11fa66A8B282eeCa
- 回执核验结果：status 成功；from 为部署钱包；to 为空，即合约创建交易；contractAddress 与合约地址一致；铸造 Transfer 日志为零地址 → 接收钱包，金额为全部 1 亿枚

## 三、链上核验（Base RPC）

- eth_chainId：0x2105
- 合约代码：存在
- totalSupply：100000000000000000000000000（即 100,000,000 × 10^18）
- decimals：18
- 接收钱包 balanceOf：等于 totalSupply，全量已到接收钱包

## 四、BaseScan 源码验证

- 结果：Pass - Verified（Etherscan API V2，checkverifystatus 两次查询一致）
- 编译器：Solidity 0.8.24，v0.8.24+commit.e11b9ed9
- 优化：Enabled，runs 200；EVM：paris；许可证：MIT；Proxy：0（非代理）
- 构造函数参数：initialRecipient = 0xCAc8F76a31586AdAc44deeEF11fa66A8B282eeCa
- 源码与 ABI 已在 BaseScan 公开可读
- BaseScan 合约页：https://basescan.org/address/0x0e0147e45f87649097b85214c4d0705d6caa8ad6
- BaseScan 交易页：https://basescan.org/tx/0xafaeb88b93f2c3b1574d8ae4835226b8f33387d371a33007f2cacf41eeb6d957

## 五、GitHub 公开仓库

- 仓库：https://github.com/xiaoyuyu27/NOYA-Token
- 可见性：Public，默认分支 main，不登录也能打开
- 内容：合约、部署脚本、测试、审计报告、部署记录、验证记录、README、MIT LICENSE 等共 22 个文件
- 最新提交（资料整理时）：caa9bb85e4bf3f6fcfb3e1d39cddd5952cdca624
- 关键文件：contracts/NOYA.sol、scripts/deploy.js、test/NOYA.test.js、audit/SECURITY-REPORT.md、NOYA-DEPLOYMENT-REPORT.md

## 六、测试与安全（部署前真实执行）

- 编译：Hardhat 2.28.0，Compiled 6 Solidity files successfully
- 测试：8 passing（名称/符号/精度、总量、接收全量、转账、授权转账、超额转账 revert、无 mint/burn/owner/pause/黑名单/税费/冻结入口、零地址构造函数 revert）
- Slither 0.11.6：5 条结果，全部 INFO 级，无 High / Medium / Low
- _mint 仅在构造函数出现 1 次

## 七、链接汇总

- 合约：https://basescan.org/address/0x0e0147e45f87649097b85214c4d0705d6caa8ad6
- 部署交易：https://basescan.org/tx/0xafaeb88b93f2c3b1574d8ae4835226b8f33387d371a33007f2cacf41eeb6d957
- 接收钱包：https://basescan.org/address/0xCAc8F76a31586AdAc44deeEF11fa66A8B282eeCa
- GitHub：https://github.com/xiaoyuyu27/NOYA-Token
- 用户提供的项目官网：https://noya.ai/

## 八、注意事项

1. 与 noya.ai 官方项目的关系仍未确认，对外不得宣称为官方币，正式宣传前请自行确认。
2. 本文件只含公开链上信息，不含任何私钥、助记词、API Key，请勿把私钥或助记词发给任何人。
3. 早期部署页日志截图读出的哈希有误，已按用户以文字回传的完整哈希纠正并经回执核验，以本文件中的哈希为准。
4. 临时部署页已删除，ai.hljyykj.com 首页未改动。
