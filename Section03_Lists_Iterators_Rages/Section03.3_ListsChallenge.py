__author__ = "Crypto"

# continue from the previous lecture
menu = []
menu.append(["egg", "spam", "beacon"])
menu.append(["egg", "sausage", "beacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "beacon", "spam"])
menu.append(["egg", "beacon", "sausage", "spam"])
menu.append(["spam", "beacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

# print(menu)

for meal in menu:
    if not 'spam' in meal:
        print(meal)

        # Style 01
        for ingredient in meal:
            print(ingredient)

        print("\n")

        # Style 02
        print(*meal, sep="\n")
