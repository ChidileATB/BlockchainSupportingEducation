from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the blockchain
blockchain = Blockchain()

# Endpoint to add data (certificates/badges) to the blockchain
@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.get_json()
    blockchain.add_data(data)
    return jsonify({'message': 'Data added successfully.'}), 201

# Endpoint to view the entire blockchain
@app.route('/view_chain', methods=['GET'])
def view_chain():
    return jsonify({'chain': [vars(block) for block in blockchain.chain]}), 200

if __name__ == '__main__':
    app.run(port=5000)
