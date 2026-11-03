const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("NOYA", function () {
  const TOTAL = 100_000_000n * 10n ** 18n;
  let noya, deployer, recipient, userA, userB;

  beforeEach(async function () {
    [deployer, recipient, userA, userB] = await ethers.getSigners();
    const NOYA = await ethers.getContractFactory("NOYA");
    noya = await NOYA.deploy(recipient.address);
    await noya.waitForDeployment();
  });

  it("name / symbol / decimals are NOYA / NOYA / 18", async function () {
    expect(await noya.name()).to.equal("NOYA");
    expect(await noya.symbol()).to.equal("NOYA");
    expect(await noya.decimals()).to.equal(18);
  });

  it("total supply is exactly 100,000,000", async function () {
    expect(await noya.totalSupply()).to.equal(TOTAL);
  });

  it("initial recipient receives the full supply, deployer receives 0", async function () {
    expect(await noya.balanceOf(recipient.address)).to.equal(TOTAL);
    expect(await noya.balanceOf(deployer.address)).to.equal(0);
  });

  it("plain transfer works", async function () {
    const amount = ethers.parseUnits("1000", 18);
    await expect(noya.connect(recipient).transfer(userA.address, amount))
      .to.emit(noya, "Transfer").withArgs(recipient.address, userA.address, amount);
    expect(await noya.balanceOf(userA.address)).to.equal(amount);
    expect(await noya.balanceOf(recipient.address)).to.equal(TOTAL - amount);
  });

  it("approve + transferFrom works", async function () {
    const amount = ethers.parseUnits("500", 18);
    await noya.connect(recipient).approve(userA.address, amount);
    expect(await noya.allowance(recipient.address, userA.address)).to.equal(amount);
    await noya.connect(userA).transferFrom(recipient.address, userB.address, amount);
    expect(await noya.balanceOf(userB.address)).to.equal(amount);
  });

  it("transfer above balance reverts", async function () {
    await expect(
      noya.connect(userA).transfer(userB.address, ethers.parseUnits("1", 18))
    ).to.be.reverted;
  });

  it("there is no mint / burn / owner / blacklist / pause entry point in the ABI", async function () {
    // Ethers v6 exposes only ABI functions; a missing function is undefined.
    for (const fn of ["mint", "burn", "owner", "pause", "unpause", "blacklist", "setTax", "setFee", "freeze"]) {
      expect(noya[fn], `unexpected function ${fn}`).to.equal(undefined);
    }
    const fnNames = noya.interface.fragments.filter((f) => f.type === "function").map((f) => f.name);
    expect(fnNames).to.include.members(["name", "symbol", "decimals", "totalSupply", "balanceOf", "transfer", "approve", "allowance", "transferFrom"]);
  });

  it("constructor rejects the zero address", async function () {
    const NOYA = await ethers.getContractFactory("NOYA");
    await expect(NOYA.deploy(ethers.ZeroAddress)).to.be.revertedWith("NOYA: recipient is zero address");
  });
});
