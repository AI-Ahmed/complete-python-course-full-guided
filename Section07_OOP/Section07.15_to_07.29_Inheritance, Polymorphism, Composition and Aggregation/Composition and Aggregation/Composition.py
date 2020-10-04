__author__ = "crypto"


class Composition:
    """Composition is about has a relationship rather that is a relationship

     Example:
         (-) Inheritance:

             ---> Troll "is a" Enemy
             ---> Vampire "is a" Enemy

         BUT

        (-) Composition:

             ---> Duck "has a" Wings
             ---> Penguin "has a" wings

     Another example we can deal with it is HTML language. It's one of the language
     that you can see the composition is working perfectly on it.

     <html>
        <header>
            <title><h1> ------ </h1></title>
        </header>

        <body>
            <dev>
                <h2> Dev 01 </h2>
                <p> hello, this's the first session of the code </p>
                --------

                --------
                --------

                ------
                ----
            </dev>
            <dev>
                <h2> Dev 02 </h2>
                <p> hello, this's the second session of the code </p>
                --------

                --------
                --------

                ------
                ----
            </dev>
        </body>
     </html>

     In Html, as you can see its couples of objects inside each other related and connected
     to create a form that represent <web page>

     each tag here represent and object with container to the other tag

     So, let's implement that in sort of HTML Document.
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

    # we'll use this code if we want to add tag or something could not be a default for a browser
    #     self._header__contents = []
    #
    # def add_tag(self, name, contents):
    #     new_tag_header = Tag(name, contents)  # Header in Composition
    #
    #     self._header__contents.append(new_tag_header)
    #
    # def display(self, file=None):
    #     for tag in self._header__contents:
    #         self.contents += str(tag)
    #
    #     super().display(file=file)


class Body(Tag):

    def __init__(self):
        super().__init__("body", '')
        self._body__contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)  # body object is actually having a lots of tags
        #                                 that we can counting it to create each class object for them all.
        #                                 So, we compose them into the body and the header objects.
        self._body__contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body__contents:
            self.contents += str(tag)

        super().display(file=file)


# ===================================
# Section 07.17: Composition Continued
# now, lets HtmlDoc that contains every object that we create and compose them


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

    def __init__(self, title=None):
        self._doc__type = DocType()
        self._head_ = Header(title)
        self._body_ = Body()

    # def add_tag_header(self, name, contents):
    #     self._head_.add_tag(name, contents)

    def add_tag(self, name, contents):
        self._body_.add_tag(name, contents)

    def display(self, file=None):
        self._doc__type.display(file=file)
        print('<html>', file=file)
        self._head_.display(file=file)
        self._body_.display(file=file)
        print('</html>', file=file)

# =======================================================================================
# Section 07.18: Test Code and Challenge
# Challenge:
    """At the moment, our "Head" Class doesn't create a document header with anything in it.
    So, your challenge is to modify the program so that the "Head" class can include a "Title" tag
    """