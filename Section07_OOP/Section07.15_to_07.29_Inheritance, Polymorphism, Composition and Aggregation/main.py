# To refer to a class you wrote it must be in a Module not in Directory


# import class_Player     # it will be more reliable if we graped the class at the beginning then we can use it
# from class_Player import Player
#
# # crypto = class_Player.Player("Crypto")
# crypto = Player("Crypto")
#
# print(crypto.name)
# print(crypto.lives)
#
# # let's make some test after adding get and set and see if the property() works
# crypto.lives -= 1
# print(crypto.lives)
# ---------------------------------------------------------------------------------
# after adding __str__ method
# crypto.lives -= 1
# print(crypto)
#
# crypto.lives -= 1
# print(crypto)
#
# crypto.lives -= 1
# print(crypto)
# ---------------------------------------------
# lets test the property methods
# print(crypto)
#
# crypto.level += 1
# print(crypto)
#
# crypto.level += 2
# print(crypto)
#
#
# crypto.level -= 1
# print(crypto)
#
# crypto.level += 4
# print(crypto)

# crypto.level = 5
# print(crypto)
#
# crypto.level -= 3
# print(crypto)
# ==========================================================
# Enemy Class - superclass
# from superClass_Enemy import Enemy
#
# random_monster = Enemy("Monster", 20, 1)
#
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(10)
# print(random_monster)
# ==========================================================
# Troll Class - Enemy sub-class (Notice that these instances will only work if we passed the class without adding anything to it)
# from superClass_Enemy import Enemy, Troll
#
# ugly_troll = Troll()
# print("Ugly-Troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug", 10, 1)
# print("Another troll - {}".format(another_troll))
#
# brother = Troll("Urg", 20)
# print(brother)
#
# brother2 = Enemy("Urge", 30)
# print(brother2)

# if you notice, in the instances, you wrote a different amount types of parameter
#  most ignored like the first instance and the third one, you missed the argument of lives
#  in any other languages ex: java, you're restricted to write the tree attributes of the constructor
#  of the superclass. In Python, it doesn't believe in "Overloading" method which writing everything into
#  anything even if it has default value in the superclass attributes
# ==========================================================
# Section 07.20 Calling Super Method
# from superClass_Enemy import Enemy, Troll
#
# # now if we want to initialize a static value to some parameters like lives & hit_point so we can pass the name only
#
# ugly_troll = Troll("Pig")   # you must initialize the constructor Arg that been initialized
# print("Ugly-Troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))
#
# brother = Troll("Urg")
# print(brother)
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()
# ==============================================================================================
# Section 07.11: Changing Behavior of Methods
# from superClass_Enemy import Enemy, Vampire
#
# vamp = Vampire("Exious")

# print(vamp)

# vamp.take_damage(5)
# print(vamp)
#
# vamp.take_damage(5)
# print(vamp)
#
# vamp.take_damage(5)
# print(vamp)
#
# vamp.take_damage(5)
# print(vamp)
# ---------------------
# while vamp.alive:
#     print(vamp)
#     vamp.take_damage(2)
# ==============================================================================================
# Section 07.12: Overriding Methods
# In this section we learn how to override the methods
# from superClass_Enemy import Enemy, Vampire

# while vamp.alive:
#     # if not vamp.dodges():   # before the overriding method
#     print(vamp)
#     vamp.take_damage(2)
# ==============================================================================================
# Section 07.13: Inheritance Challenge Testing - multiple Inheritance
# from superClass_Enemy import Enemy, Vampire, VampireKing
#
# vampKing = VampireKing("Thenous")
#
# while vampKing.alive:
#     print(vampKing)
#     vampKing.take_damage(15)
# ==============================================================================================
# Section 07.14: Polymorphism


