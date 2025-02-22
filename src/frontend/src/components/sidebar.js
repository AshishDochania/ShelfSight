
import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => (
  <nav className="sidebar">
    <ul>
      <li><Link to="/">Dashboard</Link></li>
      <li><Link to="/tasks">Tasks</Link></li>
      <li><Link to="/analytics">Analytics</Link></li>
      <li><Link to="/settings">Settings</Link></li>
    </ul>
  </nav>
);

export default Sidebar;