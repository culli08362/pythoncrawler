class Parent1(object):
    def __init__(self):
        super(Parent1, self).__init__()
        self.var1 = 1

class Parent2(object):
    def __init__(self):
        super(Parent2, self).__init__()
        self.var2 = 2

class Child(Parent1, Parent2):
    def __init__(self):
        super(Child, self).__init__(
