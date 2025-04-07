def main():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    print("Length of the list:", len(fruit_list))

    fruit_list.append('mango')

    print("Updated list:", fruit_list)

main()


def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except:
        return "Invalid slice indices."

def play_index_game():
    my_list = ['sun', 'moon', 'stars', 'clouds', 'sky']
    print("\nWelcome to the Index Game!")
    print("Your starting list:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            result = access_element(my_list, index)
            print("Result:", result)

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            result = modify_element(my_list, index, new_value)
            print("Updated list:", result)

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced list:", result)

        elif choice == '4':
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Please choose between 1 and 4.")


play_index_game()
