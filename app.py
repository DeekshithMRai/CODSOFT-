from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = ['Task 1', 'Task 2', 'Task 3']

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    new_task = request.form['task']
    if new_task and new_task.strip() != '':
        tasks.append(new_task.strip())
    return jsonify(tasks=tasks)

@app.route('/update_task/<int:index>', methods=['POST'])
def update_task(index):
    tasks[index] = request.form['task'].strip()
    return jsonify(tasks=tasks)

@app.route('/delete_task/<int:index>', methods=['POST'])
def delete_task(index):
    tasks.pop(index)
    return jsonify(tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
