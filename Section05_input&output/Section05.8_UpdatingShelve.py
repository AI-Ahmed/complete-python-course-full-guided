__author__ = "crypto"

import shelve

# 1- after running this code, lets comment it because now we will use the data from the db
# 2- now you can comment the last recipe which soup


# blt = ["beacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans",  "bread"]
# scrambled_eggs = ["eggs",  "butter",  "milk"]
soup = ["tins of soup"]
# pasta = ["pasta",  "cheese"]

with shelve.open("recipes", writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # --------------------------------------------------------

    # After running this, the shelve has no way to know that these lists are changed
    # What's actually happened is that we've appended items into a "copy" of the list read
    # into the memory but we haven't provided any trigger for the shelve to write data
    # back out again and this is very confusing when you first starting with shelve
    # the reason that it works this way is to keep the disk access to an absolute minimum
    # so that values aren't continually written into disk it does have this unfortunate
    # side effect that when accessing the same keys value after a change causes it to
    # be read from the shelve and that's the unchanged value is returned
    # rather than the value that you think it would be in this case by our tomato

    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")

    # # so, what we need to do first is to retrieve the list:
    # temp_list = recipes["blt"]
    # # then append the value
    # temp_list.append("butter")
    # recipes["blt"] = temp_list  # now we insert the key
    #
    # temp_list = recipes["pasta"]
    # # then append the value
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    # deleting the attribute
    # del recipes["blt"]

    # --------------------------------------------------------
    # "writeback=True"

    # now lets comment the indentation that we done

    # make sure that the key for the shelve is immutable object

    # another way to append into the shelve db is:

    # recipes["soup"].append("croutons")  # but you need to add into line 15 'writeback=True'

    # when you actually use writeback, python caches the object into the memory
    # doesn't actually update the shelve file itself until you close the shelve
    # or used to seat method so, if there's been changes closing a shelve can take a while
    # because all have to be written to disk at or so this gives the advantage as you saw
    # from line 35 - 44
    # but the price of this disadvantage in other words is heavy
    # memory usage could possibly much more heavy usage heavily depending on how many changes

    # --------------------------------------------------------
    # "auto Sync"

    # sync itself causes all entries in the cache to be written to disk
    # but it also "clears the cache as well so sync is called automatically
    # when the shelve is closed but you can also use it anywhere anytime you want to force the data
    # to be updated

    # essentially with writeback=True enabled is going to overwrite our previous entries
    # so, its kinda delete any changed happened and reset the list like it has to be

    recipes["soup"] = soup
    recipes.sync()
    soup.append("cream")

    # if you run the code or disabled it "cream" will NOT be appended
    # cause soup object list sored in the cache and the sync causes the cache to be cleared so
    # soup.append on line 81 added cream to the list but
    # there's no corresponding list object in the cache anymore because we called recipes.sync
    # so, when we call the loop again we're calling the soup list from the disk
    # soup list retrieved is not the same one that we've just added cream too
    # so, that best thing not to use this method.
    # use the method that we previously showed here "writeback=True"

    for snack in recipes:
        print(snack, recipes[snack])

# Let's summarize the shelve

# The keys must be string but the values can be just
# about any python objects.

# dictionaries containing lists for example can be use
# as values in the shelves the value are pickled
# before being stored in the underlying data base fields so that same for pickle
# applies to shelve values because of that now this makes shelves really
# convenient and simple way to store programs data unless you have persistent
# storage yet continue to use the usual python syntax without having learn SQL


# sometimes shelves it's not suitable for some application so as
# a few examples; because values are pickled before being stored
# are unpickled by the value where read back if your values are really complex
# this pickling and unpickling may impose significant overhead
# and effect the performance
