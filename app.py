from flask import Flask, render_template, request, redirect, url_for
from src.auth.service import TodoServices

app = Flask(__name__)

todo_service = TodoServices()


@app.route("/")
def index():
    """Displays all tasks."""
    data = todo_service.get_all_todo()
    return render_template("index.html", tasks=data)


@app.route("/add", methods=["POST"])
def add_task():
    """Adds a new task."""
    description = request.form["description"]
    title = request.form["title"]
    status = request.form["status"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    d = {
        "description":description,
        "title":title,
        "status":status,
        "start_date":start_date,
        "end_date":end_date

    }
  
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    """Marks a task as complete."""
    todo_service.complete_todo_item(task_id)
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    """Deletes a task."""
    todo_service.delete_todo_item(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)


