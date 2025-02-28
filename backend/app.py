# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from tax_model import TaxModel

app = Flask(__name__)
CORS(app, origins=["https://taxsmart.netlify.app"])

# Initialize and train the model
tax_model = TaxModel()
tax_model.train()

@app.route('/tax-planner', methods=['POST'])
def tax_planner():
    user_data = request.json
    income = user_data['income']
    expenses = user_data['expenses']
    investments = user_data['investments']

    result = tax_model.suggest_tax_savings(income, expenses, investments)
    
    response = {
        'suggestion': result['suggestion'],
        'blockchain_record': {
            'block_index': result['block_info']['block_index'],
            'block_hash': result['block_info']['block_hash'],
            'timestamp': result['block_info']['timestamp']
        }
    }
    
    return jsonify(response)

@app.route('/verify-tax-record', methods=['POST'])
def verify_tax_record():
    block_index = request.json.get('block_index')
    is_valid = tax_model.ledger.verify_block(block_index)
    return jsonify({
        'valid': is_valid,
        'message': 'Tax record is valid' if is_valid else 'Tax record verification failed'
    })

if __name__ == '__main__':
    app.run(debug=True)
