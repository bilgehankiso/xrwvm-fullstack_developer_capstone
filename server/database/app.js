const express = require('express');
const mongoose = require('mongoose');
const fs = require('fs');
const cors = require('cors');
const app = express();
const port = 3030;

app.use(cors());
app.use(express.json());

const reviews_data = JSON.parse(fs.readFileSync('reviews.json', 'utf8'));
const dealers_data = JSON.parse(fs.readFileSync('dealerships.json', 'utf8'));

// Express Routes
app.get('/fetchDealers', async (req, res) => {
  res.json(dealers_data.dealerships);
});

app.get('/fetchDealers/:state', async (req, res) => {
  const state = req.params.state;
  const filtered = dealers_data.dealerships.filter(dealer => dealer.state === state);
  res.json(filtered);
});

app.get('/fetchDealer/:id', async (req, res) => {
  const id = parseInt(req.params.id);
  const dealer = dealers_data.dealerships.find(d => d.id === id);
  res.json(dealer ? [dealer] : []);
});

app.get('/fetchReviews/dealer/:id', async (req, res) => {
  const id = parseInt(req.params.id);
  const reviews = reviews_data.reviews.filter(r => r.dealership === id);
  res.json(reviews);
});

app.post('/fetchReviews/put', async (req, res) => {
  const new_review = req.body;
  new_review.id = reviews_data.reviews.length + 1;
  reviews_data.reviews.push(new_review);
  res.json({status: "success", review: new_review});
});

app.listen(port, () => {
  console.log(`Dealer microservice listening at http://localhost:${port}`);
});
