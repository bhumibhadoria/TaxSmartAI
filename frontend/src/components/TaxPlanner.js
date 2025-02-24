import React, { useState } from "react";
import axios from "axios";

function TaxPlanner() {
  const [income, setIncome] = useState("");
  const [expenses, setExpenses] = useState("");
  const [investments, setInvestments] = useState("");
  const [suggestion, setSuggestion] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:5000/tax-planner", {
        income: parseInt(income),
        expenses: parseInt(expenses),
        investments: parseInt(investments),
      });
      setSuggestion(response.data.suggestion);
    } catch (error) {
      console.error("Error fetching suggestion:", error);
    }
  };

  return (
    <div>
      <h1>AI-Driven Tax Planner</h1>
      <form onSubmit={handleSubmit}>
        <input type="number" placeholder="Income" value={income} onChange={(e) => setIncome(e.target.value)} required />
        <input type="number" placeholder="Expenses" value={expenses} onChange={(e) => setExpenses(e.target.value)} required />
        <input type="number" placeholder="Investments" value={investments} onChange={(e) => setInvestments(e.target.value)} required />
        <button type="submit">Get Suggestions</button>
      </form>
      {suggestion && <p>Suggestion: {suggestion}</p>}
    </div>
  );
}

export default TaxPlanner;
