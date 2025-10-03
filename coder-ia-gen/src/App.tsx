import { useState, useEffect } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';

function App() {


  const [count, setCount] = useState(0);
  
  // Fetch the count when component mounts for first time
  useEffect(() => {
    fetch('http://localhost:8000/count')
      .then((response) => response.json())
      .then((data) => {
        if ('count_number' in data) setCount(Number(data.count_number)); // assuming 'count' is the key in returned json
      });
  }, []);
  
  return (
    <div className="main-container">
      <header className="header">
        <a href="https://vite.dev" target="_blank" rel="noopener noreferrer">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank" rel="noopener noreferrer">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </header>
      <h1 className="title-gradient">Compteur IA</h1>
      <div className="card enhanced-card">
        <div className="count-label">Valeur actuelle :</div>
        <button className="count-btn" onClick={() => {
          fetch('http://localhost:8000/count/increment', { method: 'POST' })
            .then((response) => response.json())
            .then((data) => {
              if ('count_number' in data) setCount(Number(data.count_number));
            });
        }}>
          {count}
        </button>
        <button className="reset-btn" onClick={() => {
          fetch('http://localhost:8000/count/reset', { method: 'POST' })
            .then((response) => response.json())
            .then((data) => {
              if ('count_number' in data) setCount(Number(data.count_number));
            });
        }}>
          Réinitialiser
        </button>
        <p className="hint">Cliquez sur le bouton pour incrémenter le compteur</p>
      </div>
      <footer className="footer">
        <span>🚀 Projet Vite + React + FastAPI + PostgreSQL</span>
      </footer>
    </div>

  );
}


export default App;
