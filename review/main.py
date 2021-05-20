import utils


def main():
    users = utils.getUsers()
    todos = utils.getTodoItems()

    for user in users:
        userTodos = [t for t in todos if t.userId == user.id]
        print("{} ({})".format(user.name, len(userTodos)))


if __name__ == '__main__':
    main()
    