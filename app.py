from flask import Flask, request, jsonify

app = Flask(__name__)
notes = []

@app.route('/notes', methods=['GET', 'POST'])
def manage_notes():
    if request.method == 'POST':
        data = request.get_json()
        note = data.get('note')
        notes.append(note)
        return jsonify({'message': 'Note added successfully'})
    elif request.method == 'GET':
        return jsonify({'notes': notes})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
