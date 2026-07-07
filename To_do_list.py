class Notebook:
    def __init__(self):
        self.task = []

    def add_note(self, note):
        self.task.append(note)

    def show_notes(self):
        for  i,note in enumerate(self.task, start=1):
            print(f"{i}. {note}")
nb = Notebook()
n=int(input("How many tasks  : "))
for i in range(n):
    task=(input("Enter task : "))
    nb.add_note(task)
nb.show_notes()