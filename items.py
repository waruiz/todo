class Items:
    def __init__(self):
        self.items = []

    def empty(self):
        self.items.clear()

    def add(self, item):
        self.items.append(item)

    def show(self):
        for item in self.items:
            print(item.title)
