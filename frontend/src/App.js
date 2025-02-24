import React from 'react';
import TaxPlanner from './components/TaxPlanner';
import './index';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>TaxSmart AI</h1>
      </header>
      <main>
        <TaxPlanner />
      </main>
    </div>
  );
}

export default App;