import db_interaction
from flask import Flask, jsonify, request

api_endpoint= "/api/v0"

app= Flask(__name__)

@app.route('/')
def index():
    return "Home Page Use API to exexute queries"

@app.route(api_endpoint+'/tasks', methods=['GET'])
def get_tasks_list():
    t= db_interaction.showTasks()
    return jsonify(t)

@app.route(api_endpoint + '/tasks/<int:id>', methods=['GET'])
def get_task(id):
    return jsonify(db_interaction.showSpecificTasks(id))

@app.route(api_endpoint+'/tasks', methods=['POST'])
def new_task():
    task= request.json
    db_interaction.newTask(task["Description"], task["Urgent"])
    return jsonify(task)

@app.route(api_endpoint+'/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task= request.json
    db_interaction.updateTask(id, task["Description"], task["Urgent"])
    t= db_interaction.showSpecificTasks(id)
    return jsonify(t)

@app.route(api_endpoint+'/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    db_interaction.removeTask(id)
    task= db_interaction.showTasks()
    return jsonify(task)

if __name__ == '__main__':
    app.run()