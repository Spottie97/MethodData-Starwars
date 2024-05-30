from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SWAPI_BASE_URL = "https://swapi.dev/api/people/"

def get_character_data(name: str) -> Dict:
    response = requests.get(SWAPI_BASE_URL, params={'search': name})
    if response.status_code == 200:
        data = response.json()
        if data['count'] > 0:
            return data['results'][0]
    return None

def compare_characters(char1: Dict, char2: Dict) -> Dict:
    comparison = {}
    attributes = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender']
    for attr in attributes:
        char1_value = char1.get(attr, 'unknown')
        char2_value = char2.get(attr, 'unknown')
        if char1_value != char2_value:
            comparison[attr] = {
                'character1': char1_value, 
                'character2': char2_value,
                'winner': 'character1' if char1_value > char2_value else 'character2'
            }
    return comparison

@app.get("/compare")
def compare(name1: str, name2: str):
    char1 = get_character_data(name1)
    char2 = get_character_data(name2)

    if not char1 or not char2:
        raise HTTPException(status_code=404, detail="One or both characters not found")

    comparison_result = compare_characters(char1, char2)
    return comparison_result

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
