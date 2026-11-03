const hre = require("hardhat");

async function main() {
  const recipient = process.env.RECIPIENT_ADDRESS;
  if (!recipient || !/^0x[0-9a-fA-F]{40}$/.test(recipient)) {
    throw new Error("RECIPIENT_ADDRESS env var is missing or not a valid address. Refusing to deploy.");
  }
  const chainId = (await hre.ethers.provider.getNetwork()).chainId;
  if (chainId !== 8453n) {
    throw new Error(`Refusing to deploy: expected Base Mainnet chainId 8453, got ${chainId}`);
  }
  const [deployer] = await hre.ethers.getSigners();
  console.log("Network: Base Mainnet, chainId:", chainId.toString());
  console.log("Deployer:", deployer.address);
  console.log("Recipient (receives 100,000,000 NOYA):", recipient);
  console.log("Deployer ETH balance:", hre.ethers.formatEther(await hre.ethers.provider.getBalance(deployer.address)));

  const NOYA = await hre.ethers.getContractFactory("NOYA");
  const noya = await NOYA.deploy(recipient);
  await noya.waitForDeployment();
  const address = await noya.getAddress();
  console.log("NOYA deployed to:", address);
  console.log("Deployment tx hash:", noya.deploymentTransaction().hash);
  console.log("Total supply:", (await noya.totalSupply()).toString());
  console.log("Recipient balance:", (await noya.balanceOf(recipient)).toString());
  console.log("Verify with: npx hardhat verify --network base", address, recipient);
}

main().catch((e) => { console.error(e); process.exitCode = 1; });
