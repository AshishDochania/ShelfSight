// src/frontend/src/components/Header.js
import React from 'react';

const Header = () => (
  <header>
    <img src="/logo.png" alt="ShelfSight AI Logo" />
    <h1>ShelfSight AI</h1>
    <div className="store-info">
      <span>Store: Main Street</span>
      <span>{new Date().toLocaleString()}</span>
    </div>
  </header>
);

export default Header;

