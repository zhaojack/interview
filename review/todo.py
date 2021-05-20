class Todo(object):

    def __init__(self, todo_data):
        self.id = todo_data['id']
        self.userId = todo_data['userId']
        self.title = todo_data['title']
        self.completed = todo_data['completed']