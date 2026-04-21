import React, { useState } from "react";
import "./Register.css";

const Register = () => {
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");

  const register = async (e) => {
    e.preventDefault();
    let register_url = window.location.origin + "/djangoapp/register";
    
    const res = await fetch(register_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userName: userName,
        password: password,
        firstName: firstName,
        lastName: lastName,
        email: email,
      }),
    });

    const json = await res.json();
    if (json.status === "Authenticated") {
      sessionStorage.setItem("username", json.userName);
      window.location.href = window.location.origin;
    } else {
      alert("Registration failed: " + (json.error || "Unknown error"));
    }
  };

  return (
    <div className="register_container">
      <div className="register_card">
        <div className="register_header">
          <h2>Create Account</h2>
          <p>Join Cars Dealership Network</p>
        </div>
        <form onSubmit={register}>
          <div className="input_group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              name="username"
              placeholder="Username"
              className="input_field"
              onChange={(e) => setUserName(e.target.value)}
              required
            />
          </div>
          <div className="row">
            <div className="input_group col">
              <label htmlFor="firstname">First Name</label>
              <input
                type="text"
                name="firstname"
                placeholder="First Name"
                className="input_field"
                onChange={(e) => setFirstName(e.target.value)}
                required
              />
            </div>
            <div className="input_group col">
              <label htmlFor="lastname">Last Name</label>
              <input
                type="text"
                name="lastname"
                placeholder="Last Name"
                className="input_field"
                onChange={(e) => setLastName(e.target.value)}
                required
              />
            </div>
          </div>
          <div className="input_group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              name="email"
              placeholder="email@example.com"
              className="input_field"
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="input_group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              name="password"
              placeholder="Password"
              className="input_field"
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="register_button">Register</button>
        </form>
      </div>
    </div>
  );
};

export default Register;
