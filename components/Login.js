import React, { useState } from 'react';
import './Login.css';

const Login = () => {
  const [nickname, setNickname] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    // Save nickname and password to local storage
    localStorage.setItem('nickname', nickname);
    localStorage.setItem('password', password);

    // You can also add more validation and error handling here
  };

  return (
    <div>
      <h2>Login</h2>
      <input
        type="text"
        placeholder="Nickname"
        value={nickname}
        onChange={(e) => setNickname(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;
