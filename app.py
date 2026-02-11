# AI Disclosure: Gemini was used to assist with implementing 
# the tasks CRUD endpoints and validation logic.

from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial Data (In-memory)
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

tasks = [
    {"id": 1, "title": "Learn REST", "description": "Study REST principles", "user_id": 1, "completed": True},
    {"id": 2, "title": "Build API", "description": "Complete the assignment", "user_id": 2, "completed": False},
]

# --- USER ENDPOINTS ---
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Task Management API on Azure!"})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# --- TASK ENDPOINTS (Part 1) ---

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    
    # Validation
    if not data or 'title' not in data or 'user_id' not in data:
        return jsonify({"error": "Missing title or user_id"}), 400
    
    user_exists = any(u['id'] == data['user_id'] for u in users)
    if not user_exists:
        return jsonify({"error": "Invalid user_id"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "description": data.get('description', ""),
        "user_id": data['user_id'],
        "completed": data.get('completed', False)
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    task.update({
        "title": data.get('title', task['title']),
        "description": data.get('description', task['description']),
        "completed": data.get('completed', task['completed'])
    })
    return jsonify(task), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return '', 204

# --- USER-TASKS ENDPOINT (Part 2) ---

@app.route('/users/<int:user_id>/tasks', methods=['GET'])
def get_user_tasks(user_id):
    user_exists = any(u['id'] == user_id for u in users)
    if not user_exists:
        return jsonify({"error": "User not found"}), 404
    
    user_tasks = [t for t in tasks if t['user_id'] == user_id]
    return jsonify(user_tasks), 200

if __name__ == '__main__':
    app.run(debug=True)