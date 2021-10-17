from items import Items

class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.lists = {}

    def create_list(self, list_name):
        if self._is_valid_list_name(list_name):
            self.lists[list_name] = Items()

    def _is_valid_list_name(self, list_name):
        return isinstance(list_name, str) and len(list_name) > 0 and list_name not in self.lists

    def show_lists(self):
        for list_name in self.lists:
            print(list_name)

    def get_list(self, list_name) -> Items:
        return self.lists[list_name]
