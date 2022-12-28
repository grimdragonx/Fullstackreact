import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import React, { useState } from "react";

import './App.css';
import Home from "./Home";

function App() {
  return (
    <div className="App">
      <ToastContainer />
      <Home />
    </div>
  );
}

export default App;
