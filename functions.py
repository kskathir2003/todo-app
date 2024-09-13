def get_todos(filepath='todos.txt'):
    """
    read a file and return the list of todos
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath='todos.txt'):
    """
    write the list of todo items in the filepath
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
