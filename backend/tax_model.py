# tax_model.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os
from blockchain_ledger import TaxLedger
import hashlib
import json
import time
class TaxModel:
    def __init__(self):
        self.model = LinearRegression()
        self.trained = False
        self.ledger = TaxLedger()
        self.model_version = "v1.0.0"

    # ... (keep existing train method)
    def train(self):
        try:
            
            data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "synthetic_financial_data.csv")
            # Load and prepare data
            data = pd.read_csv(data_path)
            X = data[['income', 'expenses', 'investments']]
            y = data['tax_liability']

            # Train model
            self.model.fit(X, y)
            self.trained = True
        except Exception as e:
            raise Exception(f"Training failed: {str(e)}")

    def generate_financial_hash(self, income: float, expenses: float, investments: float) -> str:
        data = {
            "income": income,
            "expenses": expenses,
            "investments": investments,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

    def predict_tax_liability(self, income, expenses, investments):
        if not self.trained:
            raise Exception("Model not trained. Call train() first.")
        
        input_data = np.array([[income, expenses, investments]])
        predicted_tax = self.model.predict(input_data)[0]
        
        # Create tax record for blockchain
        tax_record = {
            "financial_data_hash": self.generate_financial_hash(income, expenses, investments),
            "tax_computation": {
                "predicted_tax": round(predicted_tax, 2),
                "input_parameters": {
                    "income": income,
                    "expenses": expenses,
                    "investments": investments
                },
                "model_version": self.model_version
            },
            "compliance_flags": {
                "high_income_verified": income > 1000000,
                "investment_ratio_valid": investments/income <= 0.5
            }
        }
        
        # Add to blockchain
        block_info = self.ledger.add_tax_record(tax_record)
        
        return round(predicted_tax, 2), block_info

    def suggest_tax_savings(self, income, expenses, investments):
        current_tax, block_info = self.predict_tax_liability(income, expenses, investments)
        max_deduction = 150000

        if investments < max_deduction:
            additional_investment = max_deduction - investments
            new_tax, _ = self.predict_tax_liability(income, expenses, max_deduction)
            tax_savings = current_tax - new_tax

            return {
                "suggestion": f"Consider investing an additional ₹{additional_investment} in tax-saving instruments. This could potentially save you ₹{tax_savings:.2f} in taxes.",
                "block_info": block_info
            }
        else:
            return {
                "suggestion": "You've already maximized your tax-saving investments under the current model.",
                "block_info": block_info
            }
