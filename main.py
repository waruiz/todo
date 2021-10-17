import sys
from user import User
from item import Item

def main(argv):
    user_name = argv[0]
    list_name = argv[1]

    user1 = User(user_name)
    user1.create_list(list_name)
    todos1 = user1.get_list(list_name)

    thing1 = Item("laundry")
    thing2 = Item("mop")

    todos1.add(thing1)
    # todos1.show()

    todos1.add(thing2)
    todos1.show()

if __name__ == "__main__":
    main(sys.argv[1:])
