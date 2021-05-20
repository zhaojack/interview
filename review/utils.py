import requests

from user import User
from todo import Todo


def getUsers():
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    return [User(data) for data in users]


def getTodoItems():
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    return [Todo(data) for data in todos]


def getUserTodoItems(user):
    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(user.id)).json()
    return [Todo(data) for data in todos]