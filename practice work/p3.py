class Parent:
    def ParentInfo(self):
        print("this is parent")

class Chlid(Parent):
    def ChildInfo(self):
        print("this is child")


c=Chlid()
c.ParentInfo()
c.ChildInfo()
