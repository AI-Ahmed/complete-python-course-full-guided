__author__ = "crypto"

# Composition
from Composition import HtmlDoc
if __name__ == '__main__':
    myPage = HtmlDoc('Composition Document')
    # header
    # myPage.add_tag_header("title", "HTML using Classes")
    # body
    myPage.add_tag('h1', 'my first letter into the body')
    myPage.add_tag('h2', 'my second letter into the body')
    myPage.add_tag('h3', 'my third letter into the body')
    myPage.add_tag('h4', 'my fourth letter into the body')
    myPage.add_tag('h5', 'my fifth letter into the body')
    myPage.add_tag('h5', 'my fifth letter into the body')
    myPage.add_tag('p', "hello, its very pleasure to create a website by my own style")

    with open('htmlComposed.html', 'w') as html_file:
        myPage.display(file=html_file)
# =======================================================================================
# Aggregation
# In aggregation each instance created "independently" Unlike Composition.
# but then passed to the constructor to create  the new document
# So, deleting any of these instances will not effect the code properties

from Aggregation import HtmlDoc, Header, Body, DocType
if __name__ == '__main__':

    # DocType
    new_DocType = DocType()
    # --------------------------------------------------------------
    # Header
    new_header = Header("Aggregation Document")
    # --------------------------------------------------------------

    # Body instance:
    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "Unlike <strong>Composition</strong>, aggregation uses existing instances"
                          " of objects to build up another object.")

    new_body.add_tag('p', "The composed objects doesn't actually own the objects that it's composed of"
                          "- if it's destroyed, those objects continue to exist.")

    # --------------------------------------------------------------
    # HTML Instance
    new_page = HtmlDoc(new_DocType, new_header, new_body)

    with open('htmlAggregate.html', 'w') as html_file:
        new_page.display(file=html_file)
