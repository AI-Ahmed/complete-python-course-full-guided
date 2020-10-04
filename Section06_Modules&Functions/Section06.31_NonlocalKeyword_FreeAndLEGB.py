__author__ = "crypto"


# spam with difference methods IN FUNCTIONS


def spam1():
    def spam2():
        def spam3():
            z = " even more spam"
            print("In spam3, Locals are {}".format(locals()))  # printing the spam location
            return z

        y = " more spam"
        y += spam3()
        print("In spam2, Locals are {}".format(locals()))  # printing the spam location
        return y

    x = "spam"
    x += spam2()
    print("In spam1, Locals are {}".format(locals()))  # printing the spam location
    return x


print(spam1())
# ---------------------------------------------------------------------
print('=' * 40)


def spam1():

    def spam2():

        def spam3():
            z = " even"
            z += y  # you may wondering about this confusing that y which non local variable got accessed although its non-local.
            #         what do you've to understand is python sometimes try to run the reference of the variable that has not been shadowing or changed for running it faster thought if its not effect the code
            #         what i mean by that the explanation behavior of non-local variables is perfectly correct so, function works
            #         and some optimization is the part of python and that's because when you use a non-local variable in the way we've done
            #         python adds it to the local variable name space so that it doesn't have go hunting through all the enclosing scopes
            #         and this being called LEGB (Local Enclosing Global Build ins)


            print("In spam3, Locals are {}".format(locals()))   # printing the spam location
            return z

        # y = " more " + x    # we will get error because x hasn't defined, yet
        y = " more "            # y must be exist before spam3 is called
        y += spam3()        # Do not combine these assignment.
        print("In spam2, Locals are {}".format(locals()))   # printing the spam location
        return y

    x = "spam"  # x must be exist before spam2 is called
    x += spam2()
    print("In spam1, Locals are {}".format(locals()))   # printing the spam location
    return x


print(spam1())
# if you print locals and print globals you will find that both of them are identical
print(locals())
print(globals())