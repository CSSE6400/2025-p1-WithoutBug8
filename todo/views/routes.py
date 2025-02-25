from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api/v1')

# Use for call the health
@api.route('/health')
def health():
    return jsonify({"status": "OK"})

# Use for GET all todos
# @api.route("/todos",methods=['GET'])
# def get_todos():
#     return jsonify([])

# Use for GET
@api.route('/todos',methods=['GET'])
def get_todo():
    return jsonify([{
        "id": 1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch CSSE6400 Lecture on ECHO360 for week1",
        "completed": True,
        "decline_at": "2025-02-25T00:00:00",
        "created_at": "2025-02-24T00:00:00",
        "updated_at": "2025-02-24T00:00:00"
    }])

# Use for GET method with id
@api.route('/todos/<int:id>',methods=['GET'])
def get_todos(id):
    return jsonify([{
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch CSSE6400 Lecture on ECHO360 for week1",
        "completed": True,
        "decline_at": "2025-02-25T00:00:00",
        "created_at": "2025-02-24T00:00:00",
        "updated_at": "2025-02-24T00:00:00"
    }])

# Use for POST method
@api.route('/todos',methods=['POST'])
def create_todo():
    return jsonify({
        "id": 2300847,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch CSSE6400 Lecture on ECHO360 for week1",
        "completed": True,
        "decline_at": "2025-02-25T00:00:00",
        "created_at": "2025-02-24T00:00:00",
        "updated_at": "2025-02-24T00:00:00"
    }), 201 # 201 is the status code for created(Normally 200 is meant for created successfully)

# Use for PUT method
@api.route('/todos/<int:id>',methods=['PUT'])
def update_todo(id):
    return jsonify({
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch CSSE6400 Lecture on ECHO360 for week1",
        "completed": True,
        "decline_at": "2025-02-25T00:00:00",
        "created_at": "2025-02-24T00:00:00",
        "updated_at": "2025-02-24T00:00:00"
    })

# Use for DELETE method
@api.route('/todos/<int:id>',methods=['DELETE'])
def delete_todo(id):
    return jsonify({
        "id": id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch CSSE6400 Lecture on ECHO360 for week1",
        "completed": True,
        "decline_at": "2025-02-25T00:00:00",
        "created_at": "2025-02-24T00:00:00",
        "updated_at": "2025-02-24T00:00:00"
    })