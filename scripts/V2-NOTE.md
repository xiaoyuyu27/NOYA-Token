# 部署页 v2 说明

- v1（deploy-via-metamask.html）依赖 jsdelivr CDN 的 ethers 库；若该 CDN 在用户网络打不开，点“连接”会静默失败、无任何提示，这正是“点不动”的一种可能根因。
- v2（deploy-via-metamask-v2.html）不加载任何外部 JS，直接调用 MetaMask 自带的 window.ethereum：
  - 连接：eth_requestAccounts
  - 切链：wallet_switchEthereumChain / wallet_addEthereumChain
  - 部署：eth_sendTransaction，data = 创建字节码 + 构造参数（接收地址左补零到 32 字节），Gas 由 MetaMask 估算
  - 确认：轮询 eth_getTransactionReceipt 拿 contractAddress
- v2 所有失败都会写进页面下方日志并弹窗显示原因，不再静默。
- v2 字节码与 Hardhat 编译产物完全一致（已实测），JS 语法已通过 node --check，构造参数编码已实测。
- 使用方法与 v1 相同：Chrome 里打开本文件 → 连接 → 切 Base → 填接收地址 → 部署 → 在 MetaMask 弹窗确认。
