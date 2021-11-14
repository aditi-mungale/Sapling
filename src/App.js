import React from "react";
import "./App.css";
import { BrowserRouter as Router, Route, Routes, Link, BrowserRouter } from "react-router-dom";
import Navigation from "./components/Navigation";
import Home from "./components/Home";
import Education from "./components/Education";
import Investment from "./components/Investment";
import Logo from "./images/logo.png";
import Chart from "./images/chart.jpg";
import "./bootstrap.min.css"

function App() {
  return (
      <div className="App">
        <img src={Logo} width="50" alt="logo" />
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<Home />}/>
          <Route exact path="/education" element={<Education />}/>
          <Route exact path="/investment" element={<Investment />}/>
        </Routes>
      </BrowserRouter>
      <img src={Chart} width="500" alt="chart" />
      
      
      </div>
  );
}

export default App;