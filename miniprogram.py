class Stack():
    def __init__(self):
        self.item = []
    def push(self, x):
        self.item.append(x)
    def pop(self):
        if self.is_empty():
            return "Nothing to POP"
        return self.item.pop()
    def is_empty(self):
        return len(self.item) == 0
class text_edit():
    def __init__(self):
        self.text = ""
        self.undostack = Stack()
        self.redostack = Stack()
    def write(self, newtext):
        self.undostack.push(self.text)
        self.text += newtext
        self.redostack = Stack()
    def undo(self):
        if self.undostack.is_empty():
            print("Nothing to print")
            return
        self.redostack.push(self.text)
        self.text = self.undostack.pop()
    def redo(self):
        if self.redostack.is_empty():
            print("Nothing to redo")
            return
        self.undostack.push(self.text)
        self.text = self.redostack.pop()
    def show(self):
        print("Current Text : "+ self.text)
    
editor = text_edit()

while True:
    print("\n1. Write text")
    print("2. Undo")
    print("3. Redo")
    print("4. Show text")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        t = input("Enter text: ")
        editor.write(t)
    elif choice == "2":
        editor.undo()
    elif choice == "3":
        editor.redo()
    elif choice == "4":
        editor.show()
    elif choice == "5":
        break
    else:
        print("Invalid choice")