// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/// @title NOYA
/// @notice Standard ERC-20 token, fixed supply, no mint, no tax, no blacklist,
///         no freeze, no transfer limits, no admin, no proxy, no external fee contract.
/// @dev Total supply is minted exactly once in the constructor to the
///      recipient address supplied at deployment. There is no mint function
///      anywhere in this contract, and no owner/admin role is inherited.
contract NOYA is ERC20 {
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10 ** 18;

    constructor(address initialRecipient) ERC20("NOYA", "NOYA") {
        require(initialRecipient != address(0), "NOYA: recipient is zero address");
        _mint(initialRecipient, TOTAL_SUPPLY);
    }
}
