x = [1,2]
print (x)

print (x[0])

x[0] = 33

print(x[0])
    
my_list = ["Spoon", "Fork", "Knife"]
for item in my_list:
    print(item)
    my_list.append("Ladle")
    print(my_list)    
for i in range(len(my_list)):
    print(my_list[i])
    
my_list = [] # Empty list
for i in range(5):
    user_input = input( "Enter an integer: ")
    user_input = int(user_input)
    my_list.append(user_input)
    print(my_list)