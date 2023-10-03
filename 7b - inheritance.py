class abc:
def show(self):
print("Base class") class xyz(abc):
def show1(self):
print("Derived class")
i=xyz()
i.show()
i.show1()
