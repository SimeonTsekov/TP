import unittest

class Widget:
    def __init__(self, name):
        self.__name = name
        self.__width = 100
        self.__height = 50

    def size(self):
        return (self.__width, self.__height)

    def resize(self, new_width, new_height):
        self.__width = new_width
        self.__height = new_height

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (100, 50), 'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150), 'wrong after resize')


if __name__ == '__main__':
    unittest.main()
