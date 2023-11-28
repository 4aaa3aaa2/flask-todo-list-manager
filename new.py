from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for todo items
todo_list = []

@app.route("/")
def home():
    return render_template("web.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = {"id": len(todo_list) + 1, "title": title, "complete": False}
    todo_list.append(new_todo)
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    for todo in todo_list:
        if todo["id"] == todo_id:
            todo["complete"] = not todo["complete"]
            break
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    for todo in todo_list:
        if todo["id"] == todo_id:
            todo_list.remove(todo)
            break
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)