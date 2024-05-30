from flask import Flask, request, jsonify
import swapi

app = Flask(__name__)

def get_character_data(name):
    people = swapi.get_all("people")
    for person in people.items:
        if person.name.lower() == name.lower():
            return person
    return None

def compare_characters(char1, char2):
    attributes = ['height', 'mass', 'hair_color', 'skin_color']
    comparison = {}
    for attr in attributes:
        char1_attr = getattr(char1, attr)
        char2_attr = getattr(char2, attr)
        if char1_attr > char2_attr:
            comparison[attr] = char1.name
        elif char1_attr < char2_attr:
            comparison[attr] = char2.name
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
