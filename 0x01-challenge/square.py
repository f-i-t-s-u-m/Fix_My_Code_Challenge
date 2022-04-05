#!/usr/bin/python3
""" python file"""


class Square():
    """ square class"""

    def __init__(self, *args, **kwargs):
        """ init here """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """ Area of the square """
        return self.width * self.height

    def permiter(self):
        """ return permiter"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ return str doc"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.permiter())
