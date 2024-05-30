import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [name1, setName1] = useState('');
    const [name2, setName2] = useState('');
    const [comparison, setComparison] = useState(null);

    const handleCompare = async () => {
        try {
            const response = await axios.get('http://localhost:8000/compare', {
                params: { name1, name2 }
            });
            setComparison(response.data);
        } catch (error) {
            console.error('Error fetching comparison:', error);
        }
    };

    return (
        <div className="App">
            <h1>Star Wars Character Comparison</h1>
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
            {comparison && (
                <div>
                    <h2>Comparison Results</h2>
                    <ul>
                        {Object.keys(comparison).map((key) => (
                            <li key={key}>
                                <strong>{key}:</strong> {comparison[key].character1} vs {comparison[key].character2}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}

export default App;
