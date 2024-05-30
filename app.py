from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SWAPI_BASE_URL = 'https://swapi.dev/api/people/'

def get_character_data(name):
    try:
        response = requests.get(SWAPI_BASE_URL, params={'search': name})
        response.raise_for_status() 
        data = response.json()
        if data['count'] > 0:
            return data['results'][0]
    except requests.exceptions.RequestException as e:
        return None

def compare_characters(char1, char2):
    attributes = ['height', 'mass', 'hair_color', 'skin_color']
    comparison = {}
    for attr in attributes:
        if char1[attr] > char2[attr]:
            comparison[attr] = char1['name']
        elif char1[attr] < char2[attr]:
            comparison[attr] = char2['name']
        else:
            comparison[attr] = 'Tie'
    return comparison

@app.route('/compare', methods=['POST'])
def compare():
    names = request.json.get('names')
    char1 = get_character_data(names[0])
    char2 = get_character_data(names[1])
    if char1 and char2:
        comparison = compare_characters(char1, char2)
        return jsonify({
            'character1': char1,
            'character2': char2,
            'comparison': comparison
        })
    return jsonify({'error': 'Character not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
