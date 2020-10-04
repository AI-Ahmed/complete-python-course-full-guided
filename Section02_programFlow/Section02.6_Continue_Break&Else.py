__author__ = "Crypto"

# 'continue' Mechanism
shipping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shipping_list:
    if item == "spam":
        print("I'm ignoring this item " + item)
        # 'continue' is a function that stops the process 'bypasses'
        continue
    print("Buy " + item)
# ----------------------------------------------------
print("\n")
# 'break' Mechanism
shipping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shipping_list:
    if item == "spam":
        # 'break' is a function that ends the whole process after the condition
        break
    print("Buy " + item)
print("\n")
# another example 'with "else" included'
meal = ["egg", "bacon", "spam", "sausages"]
# meal = ["egg", "bacon", "Tomato", "sausages"] # <--- for 'else' execution
nasty_food_item = ''  # underscore case
# Nasty_food_item <--- totally different
# nastyFoodItem <--- camel case
item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break  # <---- try with the 'break' and without the 'break'
else:  # <-- why we didn't make 'else' under 'if'? to have only one answer without a redundancy
    print("I'll have a plate of that, then, please")
if nasty_food_item:
    print("Can't I have anything without '{}' in it ".format(item))
