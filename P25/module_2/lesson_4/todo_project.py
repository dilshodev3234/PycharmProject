# todo(id , title , description , execute_at)
# CRUD
# Create
# Read
# Update
# Delete


todos: list['ToDo'] = []


class ToDo:
    def __init__(self,
                 id: int = None,
                 title: str = None,
                 description: str = None,
                 execute_at: str = None):
        self.id = id
        self.title = title
        self.description = description
        self.execute_at = execute_at


    def search(self) -> list:
        result = []
        for todo in todos:
            if todo.title.lower().startswith(self.title.lower()):
                result.append(todo)
        return result
    def sequence_id(self):
        if len(todos) == 0:
            return 1
        else:
            return todos[-1].id + 1

    def create(self):
        todos.append(self)

    def delete(self):
        for todo in todos:
            if todo.id == self.id:
                todos.remove(todo)

    def update(self, attribute, new_value):
        for todo in todos:
            if todo.id == self.id:
                if attribute == 'title':
                    todo.title = new_value
                elif attribute == 'description':
                    todo.description = new_value
                elif attribute == 'execute_at':
                    todo.execute_at = new_value

    def read(self):
        return todos


# Time : 16:35
# ctrl+alt+L
while True:
    menu = """
        *) search
        1) create
        2) read
        3) update
        4) delete
        0) exit
        >>>"""
    match input(menu):
        case "*":
            short_title = input('>>>')
            todo_list = ToDo(title=short_title).search()
            for todo in todo_list:
                print(f"{todo.id}) {todo.title}")
        case "1":
            todo = {
                "id" : ToDo().sequence_id(),
                "title" : input("Title"),
                "description" : input("Description: "),
                "execute_at" : input("Execute_at: ")
            }
            ToDo(**todo).create()
        case "2":
            todo_list = ToDo().read()
            for todo in todo_list:
            # id) title
                print(f"{todo.id}) {todo.title}")
        case "3":

            todo_id = int(input("ID : "))
            attribute = input("[title , description, execute_at]>>>")
            new_value = input("New value : ")
            ToDo(id = todo_id).update(attribute , new_value)
        case "4":
            todo_id = int(input("ID : "))
            ToDo(id = todo_id).delete()
        case "0":
            break

math