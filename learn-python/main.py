class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


if __name__ == '__main__':
    print("hello world")
    a = A("along", 12)
    name = a.get_name()
    print(name)
