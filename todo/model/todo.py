# TODO: Add code here
class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self) -> None:
        self.completed = True

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"{self.code_id} - {self.title}"


class TodoBook:
    def __init__(self):
        self.todos: dict[int, Todo] = {}

    def add_todo(self, title: str, description: str) -> int:
        new_id = len(self.todos) + 1
        new_todo = Todo(code_id=new_id, title=title, description=description)
        self.todos[new_id] = new_todo
        return new_id

    def pending_todos(self) -> list[Todo]:
        return [todo for todo in self.todos.values() if not todo.completed]

    def completed_todos(self) -> list[Todo]:
        return [todo for todo in self.todos.values() if todo.completed]

    def tags_todo_count(self) -> dict[str, int]:
        tag_count: dict[str, int] = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag in tag_count:
                    tag_count[tag] += 1
                else:
                    tag_count[tag] = 1
        return tag_count
