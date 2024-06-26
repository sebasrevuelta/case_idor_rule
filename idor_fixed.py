from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Simulated database of user data
user_data = {
    '1': {'name': 'Alice', 'balance': 5000},
    '2': {'name': 'Bob', 'balance': 3000},
    '3': {'name': 'Charlie', 'balance': 7000},
}

# Simulated user login (for demonstration purposes)
@app.route('/login', methods=['POST'])
def login():
    user_id = request.form.get('user_id')
    if user_id in user_data:
        session['user_id'] = user_id
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'error': 'Invalid user ID'}), 401

@app.route('/balance', methods=['GET'])
def get_balance():
    user_id = session.get('user_id')
    if user_id and user_id in user_data:
        return jsonify(user_data[user_id])
    else:
        return jsonify({'error': 'User not found or not authenticated'}), 404

if __name__ == '__main__':
    app.run(debug=True)
