
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const PORT = 5000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory notes storage
let notes = [];

// Routes
app.get('/notes', (req, res) => {
  res.json(notes);
});

app.post('/notes', (req, res) => {
  const { text, category } = req.body;
  const newNote = { id: Date.now(), text, category };
  notes.push(newNote);
  res.status(201).json(newNote);
});

// Add DELETE route
app.delete('/notes/:id', (req, res) => {
  const { id } = req.params;
  notes = notes.filter(note => note.id != id);
  res.status(204).send();
});

// Start server
console.log("Before app.listen");
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
console.log("After app.listen");
