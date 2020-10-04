__author__ = "crypto"


class Aggregation:
    """Aggregation is very similar to Composition and is often
       described as a "weak form" of composition.

    Composition the objects that another object is composed of "don't exist" ---> outside of their container
    Like in our example in line 150 - 152 in Composition.py
    the instances of a DocType which is created in a HTML doc init method on line 150 as i mentioned
    and header and body on the next two lines. so instances of all three classes exist but they only
    exist within the context of our HtmlDoc class object myPage. Now, if we delete myPage
    then those three instances will no longer exist.

    Aggregation:
        Unlike "Composition", aggregation uses existing instances of object to build up another object

        The composed object doesn't actually own the object that it's composed of -
         if it's destroyed, those objects continue to exist

        (-) We can give an example about the difference between
            the composition (Strong Relationship) && Aggregation (Weak Relationship):

            -- Human skin is essential part from the human body (Strong Relationship)
                    --> Body class (object)
                    --> Skin class (Body)

            -- Weapon in a game, the player can use multiple weapons or switch between them (Weak Relationship)
                    ---> Player Class ()
                    ---> Weapon class (player_hand_right)
                            self.mozambique = player_hand_right

    So, now let's change the HtmlDoc class's Attributes
     """
    pass


class Tag(object):

    def __init__(self, name, contents):
        self._start__tag = '<{}>'.format(name)
        self._end__tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0._start__tag}\n\t{0.contents}\n{0._end__tag}\n".format(self)

    def display(self, file=None):
        print(self, file=file)


# We need to create the DOCTYPE class for HTML (Inherently from Tag class)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strick.dtd', '')
        self._end__tag = ''  # DOCTYPE doesn't have an end tag


class Header(Tag):

    def __init__(self, title=None):  # the one we'll use here for the title tag is the one we took into the session
        super().__init__('head', '')
        if title:
            self.title_tag = Tag('title', title)
            self.contents = str(self.title_tag)


class Body(Tag):

    def __init__(self):
        super().__init__("body", '')
        self._body__contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body__contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body__contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):
    """HtmlDoc is the class the compose-->(that has) all classes object without any inheritance
    beside it uses polymorphism in its display() method.

    Attribute(s):
        _doc__type (object): DocType
        _head_ (object): Head(title(str))
        _body_ (object): body

    Method(s):
        add_tag(): it's a method that append the tags that being written in Body object or Head object
        display():  it's a method for displaying the objects and methods as HTML
    """

    def __init__(self, doc_type, head, body):
        self._doc__type = doc_type
        self._head_ = head
        self._body_ = body

    def add_tag(self, name, contents):
        self._body_.add_tag(name, contents)

    def display(self, file=None):
        self._doc__type.display(file=file)
        print('<html>', file=file)
        self._head_.display(file=file)
        self._body_.display(file=file)
        print('</html>', file=file)
