__author__ = "crypto"

import webbrowser   # for browsing access

# webbrowser.open("https://www.google.com")
# webbrowser.open("https://www.google.com", new=1)    # enable to open in new tab
# webbrowser.open("https://www.google.com", new=2)    # enable to open in new tab
# webbrowser.open_new("https://www.google.com")
# webbrowser.open_new_tab("https://www.google.com")
# webbrowser.get(using=None)
# webbrowser.register(name, constructor, instance=None)
# webbrowser.register(url, new=0, autoraise=True)
#
# help(webbrowser)

# --------------------------------------------------------
# to open the web into a specific web browser
# webbrowser.get(using=None)

firefox = webbrowser.get(using='firefox')   # style 01
# firefox = webbrowser.get('firefox %s').open_new("https://www.google.com")   # style 02
firefox.open_new("https://www.google.com")
# --------------------------------------------------------
for i in range(0, 10):
    print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=";", end=" ")