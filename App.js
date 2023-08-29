import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import News from './components/News';
import './components/Login.css'; 
import './components/News.css'; 
import './App.css'; 

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/news" element={<News />} />
      </Routes>
    </Router>
  );
};

export default App;
