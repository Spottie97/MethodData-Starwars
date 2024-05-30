from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SWAPI_BASE_URL = "https://swapi.dev/api/people/"

def get_character_data(name):
    response = requests.get(SWAPI_BASE_URL, params={'search': name})
    if response.status_code == 200:
        data = response.json()
        if data['count'] > 0:
            return data['results'][0]
    return None

def compare_characters(char1, char2):
    comparison = {}
    attributes = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender']
    for attr in attributes:
        char1_value = char1.get(attr, 'unknown')
        char2_value = char2.get(attr, 'unknown')
        if char1_value != char2_value:
            comparison[attr] = {'character1': char1_value, 'character2': char2_value}
    return comparison

@app.route('/compare', methods=['GET'])
def compare():
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    if not name1 or not name2:
        return jsonify({'error': 'Please provide two character names'}), 400

    char1 = get_character_data(name1)
    char2 = get_character_data(name2)

    if not char1 or not char2:
        return jsonify({'error': 'One or both characters not found'}), 404

    comparison_result = compare_characters(char1, char2)
    return jsonify(comparison_result)

if __name__ == '__main__':
    app.run(debug=True)
