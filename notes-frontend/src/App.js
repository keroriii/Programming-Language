
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const App = () => {
  const [text, setText] = useState('');
  const [category, setCategory] = useState('important-urgent');
  const [notes, setNotes] = useState([]);

  // Fetch notes on initial load
  useEffect(() => {
    axios.get('http://localhost:5000/notes')
      .then(response => setNotes(response.data))
      .catch(error => console.error(error));
  }, []);

  // Add a new note
  const addNote = (e) => {
    e.preventDefault();
    if (!text) return;
    const newNote = { text, category };

    axios.post('http://localhost:5000/notes', newNote)
      .then(response => {
        setNotes([...notes, response.data]);
        setText('');
      })
      .catch(error => console.error(error));
  };

  // Delete a note
  const deleteNote = (id) => {
    axios.delete(`http://localhost:5000/notes/${id}`)
      .then(() => {
        setNotes(notes.filter(note => note.id !== id));
      })
      .catch(error => console.error(error));
  };

  return (
    <div className="App">
      <h1>Note-Taking Website</h1>
      <form onSubmit={addNote} className="note-form">
        <input 
          type="text" 
          value={text} 
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter your note"
        />
        <div className="categories">
  <label className="radio-label important-urgent">
    <input 
      type="radio" 
      value="important-urgent" 
      checked={category === 'important-urgent'} 
      onChange={(e) => setCategory(e.target.value)}
    />
    <span className="radio-text">Important & Urgent </span>
  </label>
  <label className="radio-label important-not-urgent">
    <input 
      type="radio" 
      value="important-not-urgent" 
      checked={category === 'important-not-urgent'} 
      onChange={(e) => setCategory(e.target.value)}
    />
    <span className="radio-text">Important but Not Urgent </span>
  </label>
  <label className="radio-label urgent-not-important">
    <input 
      type="radio" 
      value="urgent-not-important" 
      checked={category === 'urgent-not-important'} 
      onChange={(e) => setCategory(e.target.value)}
    />
    <span className="radio-text">Urgent but Not Important </span>
  </label>
</div>
        <button type="submit">Add Note</button>
      </form>

      <div className="notes-container">
        {notes.map(note => (
          <div key={note.id} className={`note-card ${note.category}`}>
            <p>{note.text}</p>
            <button onClick={() => deleteNote(note.id)}>Done</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
