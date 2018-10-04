import datetime
r"""
This is doc string to document your module
you can see from command line with typeing that CommentAndDocument.__doc__
This module creates empty file

If you want to print special character use r to print them. such as \n
    \t   " '' " likıe that...
"""

filename=datetime.datetime.now()

#create empty file
def create_file(writeToFile=""):
    """
    This doc string inline of the function.
    You can access doc string with typing that CommentAndDocument.create_file.__doc__
    :return:
    """
    with open(filename.strftime("%Y-%m-%d-%H-%M-%S-%f"+".txt"),"w") as file:
        file.write(writeToFile)








