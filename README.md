# NOYA Token

标准 ERC-20，Base Mainnet（Chain ID 8453）。

## 固定参数（不得擅自修改）

- Name: NOYA
- Symbol: NOYA
- Total Supply: 100,000,000
- Decimals: 18
- Standard: ERC-20
- Solidity: 0.8.24（锁定）
- OpenZeppelin Contracts: 5.0.2
- Hardhat: 2.28.0
- Optimizer: enabled, runs 200
- EVM Version: paris
- 非代理、无增发、无交易税、无黑名单、无冻结、无交易限制、无管理员、无后门

## 机制

部署时构造函数一次性向 `initialRecipient` 铸造全部 1 亿枚。合约中不存在任何 mint 函数，部署后总量永久固定。

## 本地命令

```bash
npm install
npx hardhat compile
npx hardhat test
```

## 主网部署（需用户最终确认后才可执行）

部署脚本会强制校验：

1. `RECIPIENT_ADDRESS` 必须是有效地址；
2. 链上 `eth_chainId` 必须为 8453（0x2105），否则拒绝部署，绝不把 Base Sepolia 当主网；
3. 不读取、不打印、不保存助记词或私钥。

```bash
RECIPIENT_ADDRESS=0x... npx hardhat run scripts/deploy.js --network base
```

部署后用以下命令在 BaseScan 验证（编译参数须与 hardhat.config.js 完全一致）：

```bash
npx hardhat verify --network base <CONTRACT_ADDRESS> <RECIPIENT_ADDRESS>
```

## 主网部署状态（2026-11-03，链上已核验）

- 合约地址：`0x0e0147e45f87649097b85214c4d0705d6caa8ad6`
- 区块高度（部署页日志）：53450235
- 部署钱包 = 接收钱包：`0xCAc8F76a31586AdAc44deeEF11fa66A8B282eeCa`
- Base RPC 核验：totalSupply = 100,000,000，decimals = 18，接收钱包余额 = 全量
- BaseScan 合约页：https://basescan.org/address/0x0e0147e45f87649097b85214c4d0705d6caa8ad6
- GitHub 公开仓库：https://github.com/xiaoyuyu27/NOYA-Token（Public，首推提交 602bb86be79c31d206f1666bf4d374ef34fb54a4）
- 部署交易哈希：0xafaeb88b93f2c3b1574d8ae4835226b8f33387d371a33007f2cacf41eeb6d957（回执核验成功）
- 待完成：无（仅 noya.ai 官方关系仍未确认，对外不得宣称为官方币）

## 重要提醒

- 名称 NOYA 在公开市场已有同名项目（noya.ai），本项目与该官方项目的关系未经用户证实。正式对外宣传前，请用户自行确认是否以官方名义发布，避免与已存在代币混淆。
