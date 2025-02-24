const ImmutableTaxLedger = artifacts.require("ImmutableTaxLedger");

module.exports = function(deployer) {
  deployer.deploy(ImmutableTaxLedger);
};