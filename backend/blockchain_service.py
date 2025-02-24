from web3 import Web3
from solcx import compile_standard, install_solc
import json
import os

class BlockchainService:
    def __init__(self):
        install_solc("0.8.0")
        self.w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
        self.contract = self._deploy_contract()

    def _deploy_contract(self):
        with open("../blockchain/contracts/ImmutableTaxLedger.sol", "r") as file:
            contract_source_code = file.read()

        compiled_sol = compile_standard({
            "language": "Solidity",
            "sources": {"ImmutableTaxLedger.sol": {"content": contract_source_code}},
            "settings": {"outputSelection": {"*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}}}
        })

        bytecode = compiled_sol['contracts']['ImmutableTaxLedger.sol']['ImmutableTaxLedger']['evm']['bytecode']['object']
        abi = compiled_sol['contracts']['ImmutableTaxLedger.sol']['ImmutableTaxLedger']['abi']

        ImmutableTaxLedger = self.w3.eth.contract(abi=abi, bytecode=bytecode)
        tx_hash = ImmutableTaxLedger.constructor().transact({'from': self.w3.eth.accounts[0]})
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        return self.w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

    def add_tax_record(self, record_id, data_hash, computation_hash, compliance_status, ai_model_version):
        tx_hash = self.contract.functions.addTaxRecord(
            self.w3.keccak(text=record_id),
            self.w3.keccak(text=data_hash),
            self.w3.keccak(text=computation_hash),
            compliance_status,
            ai_model_version
        ).transact({'from': self.w3.eth.accounts[0]})
        self.w3.eth.wait_for_transaction_receipt(tx_hash)

    def verify_tax_record(self, record_id, data_hash):
        return self.contract.functions.verifyTaxRecord(
            self.w3.keccak(text=record_id),
            self.w3.keccak(text=data_hash)
        ).call()
