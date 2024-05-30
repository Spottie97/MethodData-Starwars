// src/CompareCharacters.js
import React, { useState } from 'react';
import axios from 'axios';

const CompareCharacters = () => {
    const [name1, setName1] = useState('');
    const [name2, setName2] = useState('');
    const [result, setResult] = useState(null);
    const [error, setError] = useState('');

    const handleCompare = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/compare`, {
                params: { name1, name2 }
            });
            setResult(response.data);
            setError('');
        } catch (err) {
            setError('One or both characters not found');
            setResult(null);
            console.error('Error fetching comparison:', err);
        }
    };

    return (
        <div>
            <h1>Compare Star Wars Characters</h1>
            <div>
                <input
                    type="text"
                    placeholder="First Character Name"
                    value={name1}
                    onChange={(e) => setName1(e.target.value)}
                />
                <input
                    type="text"
                    placeholder="Second Character Name"
                    value={name2}
                    onChange={(e) => setName2(e.target.value)}
                />
                <button onClick={handleCompare}>Compare</button>
            </div>
            {error && <p>{error}</p>}
            {result && (
                <div className="result">
                    <h2>Comparison Result</h2>
                    <pre>{JSON.stringify(result, null, 2)}</pre>
                </div>
            )}
        </div>
    );
};

export default CompareCharacters;
