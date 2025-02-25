import csv
import random
from datetime import datetime, timedelta

def generate_financial_data(num_rows=200):
    data = []
    current_date = datetime(2025, 1, 1)
    
    for _ in range(num_rows):
        income = random.randint(300000, 5000000)  # Income range
        expenses = random.randint(100000, int(income * 0.6))  # Expenses range
        investments = random.randint(50000, int(income * 0.3))  # Investments range
        
        # Calculate tax liability (20% on taxable income above standard deduction of 150,000)
        tax_liability = max(0, (income - expenses - 150000) * 0.2)
        
        data.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'income': income,
            'expenses': expenses,
            'investments': investments,
            'tax_liability': round(tax_liability, 2)
        })
        
        current_date += timedelta(days=1)  # Increment date for next row
    
    return data

def save_to_csv(data, filename='synthetic_financial_data.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['date', 'income', 'expenses', 'investments', 'tax_liability']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    financial_data = generate_financial_data(200)
    save_to_csv(financial_data)
    print("✅ Synthetic financial dataset generated successfully!")
