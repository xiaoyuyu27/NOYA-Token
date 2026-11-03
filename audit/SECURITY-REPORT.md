# NOYA 安全审计报告（第一阶段，部署前）

- 合约：contracts/NOYA.sol
- 标准：OpenZeppelin ERC20 5.0.2，Solidity 0.8.24（锁定）
- 编译：Hardhat 2.28.0，optimizer enabled runs 200，evmVersion paris
- 编译结果：Compiled 6 Solidity files successfully，无警告输出
- ABI 函数（实测）：TOTAL_SUPPLY, allowance, approve, balanceOf, decimals, name, symbol, totalSupply, transfer, transferFrom
- 结论：ABI 中不存在 mint / burn / owner / pause / blacklist / setTax / setFee / freeze 等入口。

## Slither 0.11.6 实测结果

命令：slither contracts/NOYA.sol（solc 0.8.24，remap @openzeppelin/contracts 到 node_modules）
原始日志：audit/noya-slither.log
结果：5 条，全部为 INFO 级，无 High / Medium / Low：

1. pragma：NOYA 锁定 0.8.24，OpenZeppelin 使用 ^0.8.20 范围。实际编译器为 0.8.24，属预期，不构成问题。
2. dead-code：OpenZeppelin Context 的 _msgData/_contextSuffixLength 未使用；ERC20._burn 未被调用。
   - 后者恰好佐证：本合约没有任何 burn 入口调用内部 _burn。
3. solc-version：OpenZeppelin 的 ^0.8.20 范围提示已知问题清单，但实际锁定编译器为 0.8.24，不以范围版本编译。

## 手动检查

- _mint 仅出现 1 次：构造函数内，发送给 initialRecipient，数量为 TOTAL_SUPPLY 常量。
- grep 禁止模式（owner/onlyOwner/blacklist/pause/selfdestruct/delegatecall/proxy/upgrade/setTax）在合约源码正文中除注释说明“不设置”外无任何实现。
- 非代理合约：无 Proxy、Beacon、delegatecall 逻辑。
- 无外部收费合约调用，无交易税逻辑（transfer 直接走 OpenZeppelin ERC20 标准逻辑）。
- 构造函数拒绝零地址接收者。

## 未完成项（不得谎称已完成）

- 主网尚未部署：无合约地址、无部署交易哈希、无区块高度。
- BaseScan 尚未验证：无 Exact Match 结果。
- GitHub 公开仓库尚未创建：本阶段仅本地交付目录齐备。
- 链上只读核验需在部署后另行执行。
