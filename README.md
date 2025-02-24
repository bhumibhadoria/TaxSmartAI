# TaxSmart AI

TaxSmart AI is an innovative tax planning application that combines artificial intelligence and blockchain technology to provide secure, transparent, and efficient tax advice.

## Features

- ✅ AI-driven tax planning suggestions
- 🔗 Blockchain-based immutable audit trail
- 🖥️ User-friendly interface for inputting financial data
- ✅ Verification system for tax records

## Technologies Used

- **Frontend:** React
- **Backend:** Flask
- **AI Model:** Scikit-learn
- **Blockchain:** Ethereum (Truffle, Ganache)
- **Database:** MongoDB

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- [Node.js](https://nodejs.org/)
- [Python 3.8+](https://www.python.org/downloads/)
- [Ganache](https://www.trufflesuite.com/ganache)
- [Truffle](https://www.trufflesuite.com/truffle)

### Installation

#### Clone the repository

```bash
git clone https://github.com/yourusername/taxsmart-ai.git
cd taxsmart-ai
```

#### Set up the backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

#### Set up the frontend

```bash
cd ../frontend
npm install
```

#### Set up the blockchain

```bash
cd ../blockchain
npm install -g truffle
truffle migrate
```

## Usage

#### Start the backend server

```bash
cd backend
python app.py
```

#### Start the frontend development server

```bash
cd frontend
npm start
```

Open your browser and navigate to [http://localhost:3000](http://localhost:3000) to access the application.
