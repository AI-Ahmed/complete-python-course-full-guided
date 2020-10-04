__author__ = "Crypto"

# While loop is the looping condition that indicates a condition when it turns 'False' the loop stops the process

# for i in range(10):
#     print("i is now {}".format(i))

i = 0  # <-- the condition initialized
while i < 10:
    print("i is now {}".format(i))
    i += 1  # <--- the condition that accumulate until the condition turns 'False'
# ------------------------------------------------------------------------------------
print("\n")
# Another example

available_exits = ["east", "north east", "south"]

chosen_exit = ''
while chosen_exit not in available_exits:  # <----false condition makes the while exit
    chosen_exit = input("Please, Choose another direction: ")
    if chosen_exit == 'quit':
        print("Programme Executed!")
        break
else:
    print("Aren't you glad you got out of there!")
