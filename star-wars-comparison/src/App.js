import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [name1, setName1] = useState('');
  const [name2, setName2] = useState('');
  const [result, setResult] = useState(null);

  const handleCompare = async () => {
    try {
      const response = await axios.post('http://localhost:5000/compare', {
        names: [name1, name2],
      });
      setResult(response.data);
    } catch (error) {
      console.error('Error comparing characters:', error);
    }
  };

  return (
    <div className="App">
      <h1>Star Wars Character Comparison</h1>
      <div>
        <input
          type="text"
          value={name1}
          onChange={(e) => setName1(e.target.value)}
          placeholder="Enter first character name"
        />
        <input
          type="text"
          value={name2}
          onChange={(e) => setName2(e.target.value)}
          placeholder="Enter second character name"
        />
        <button onClick={handleCompare}>Compare</button>
      </div>
      {result && (
        <div>
          <h2>Comparison Result</h2>
          <div>
            <h3>{result.character1.name}</h3>
            <p>Height: {result.character1.height}</p>
            <p>Mass: {result.character1.mass}</p>
            <p>Hair Color: {result.character1.hair_color}</p>
            <p>Skin Color: {result.character1.skin_color}</p>
            <h3>{result.character2.name}</h3>
            <p>Height: {result.character2.height}</p>
            <p>Mass: {result.character2.mass}</p>
            <p>Hair Color: {result.character2.hair_color}</p>
            <p>Skin Color: {result.character2.skin_color}</p>
            <h3>Comparison</h3>
            <p>Height Winner: {result.comparison.height}</p>
            <p>Mass Winner: {result.comparison.mass}</p>
            <p>Hair Color Winner: {result.comparison.hair_color}</p>
            <p>Skin Color Winner: {result.comparison.skin_color}</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
