import React, { Component } from "react";
import { Link } from "react-router-dom";

function Navigation(props) {
  return (
    <div className="navigation">
      <nav class="navbar navbar-expand navbar-dark bg-dark">
        <div class="container">
          <Link class="navbar-brand" to="/">
            Sapling
          </Link>

          <div>
            <ul class="navbar-nav ml-auto">
              <li
                class={`nav-item  ${
                  props.location.pathname === "/" ? "active" : ""
                }`}
              >
                <Link class="nav-link" to="/">
                  Home
                  <span class="sr-only">(current)</span>
                </Link>
              </li>
              <li
                class={`nav-item  ${
                  props.location.pathname === "/education" ? "active" : ""
                }`}
              >
                <Link class="nav-link" to="/education">
                  Education
                </Link>
              </li>
              <li
                class={`nav-item  ${
                  props.location.pathname === "/investment" ? "active" : ""
                }`}
              >
                <Link class="nav-link" to="/investment">
                  Investment
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
}

export default Navigation;