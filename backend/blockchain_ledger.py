# blockchain_ledger.py
import hashlib
import json
import time
from typing import Dict, List

class TaxBlock:
    def __init__(self, index: int, timestamp: str, tax_data: Dict, previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self.tax_data = tax_data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        
    def calculate_hash(self) -> str:
        tax_data_string = json.dumps(self.tax_data, sort_keys=True)
        return hashlib.sha256(tax_data_string.encode()).hexdigest()


class TaxLedger:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        
    def create_genesis_block(self) -> TaxBlock:
        return TaxBlock(0, time.strftime("%Y-%m-%d %H:%M:%S"), 
                       {"message": "Genesis Tax Block"}, "0")
    
    def get_latest_block(self) -> TaxBlock:
        return self.chain[-1]
    
    def add_tax_record(self, tax_data: Dict) -> Dict:
        new_block = TaxBlock(
            len(self.chain),
            time.strftime("%Y-%m-%d %H:%M:%S"),
            tax_data,
            self.get_latest_block().hash
        )
        self.chain.append(new_block)
        return {
            "block_index": new_block.index,
            "block_hash": new_block.hash,
            "timestamp": new_block.timestamp
        }

    def verify_block(self, block_index: int) -> bool:
        if block_index >= len(self.chain):
            return False
        
        block = self.chain[block_index]
        previous_block = self.chain[block_index - 1] if block_index > 0 else None
        
        if block.hash != block.calculate_hash():
            return False
        
        if previous_block and block.previous_hash != previous_block.hash:
            return False
        
        return True
