def show_menu():
    print("welcome")
    print("Menu:")
    print("1. Add item")
    print("2.Remove item")
    print("3.view list")
    print("4.count")

def add_item(shopping_list):
    item = input("enter the item to add:")
    shopping_list.append(item)

def remove_item(item_list):
    item = input("enter the item to remove: ")
    if item in item_list:
        shopping_list.remove(item)
    
def view_list(item_list):
    print("Shopping List: ")
    for item in item_list:
        print("item")

def countitems():
    count = len(shopping_list)
    print(count)

def start():
    shopping_list = []
     
show_menu()
choice = input("choose an option:")
if choice == "1":
        add_item()
elif choice == "2":
        remove_item
elif choice == "3":
        view_list()
elif choice == "4":
        count_items()







