from flask import Flask, jsonify, request, abort 

app = Flask(__name__)

# In-memory user storage
users = {}
user_id_counter = 1

# Home route
@app.route('/')
def home():
    return '<h1>Flask REST API- In-Memory User Management</h1>'

# Get all users
@app.route('/api/users/', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

# Get single user by ID
@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    user = users.get(id)
    if not user:
        abort(404, description="User not found")
    return jsonify(user), 200

# Create a new user
@app.route('/api/users/', methods=['POST'])
def create_user():
    global user_id_counter
    data = request.get_json()

    if not data or not data.get('name') or not data.get('email'):
        abort(400, description="Name and email are required")

    # Create User
    user = {
        'id': user_id_counter,
        'name': data['name'],
        'email': data['email']
    }

    users[user_id_counter] = user
    user_id_counter += 1

    return jsonify(user), 201

# Update user by ID
@app.route('/api/users/<int:id>', methods=['PATCH'])
def update_user(id):
    user = users.get(id)
    if not user:
        abort(404, description = "User not found")

    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])

    return jsonify(user), 200

# Delete user by ID
@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    if id not in users:
        abort(404, description = "User not found")

    del users[id]
    return jsonify({"message": f"User {id} deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)