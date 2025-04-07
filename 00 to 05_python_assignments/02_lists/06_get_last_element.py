def get_last_element(lst):
    print(lst[-1])

lst = []
n = int(input("How many elements in the list? "))
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    lst.append(element)

get_last_element(lst)