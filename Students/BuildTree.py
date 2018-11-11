'''
    A class to build a binary serach tree for type Student
'''

ordered = [];

class Tree():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def addElement(self, x):
        if (x.number <= self.val.number) and (self.left == None):
            self.left = Tree(x, None, None)
        elif (x.number <= self.val.number):
            self.left.addElement(x)
        elif (x.number > self.val.number) and (self.right == None):
            self.right = Tree(x, None, None)
        else:
            self.right.addElement(x)

    def searchElement(self, x):
        if self.val.number == x:
            return self.val
        elif (self.val.number < x) and (self.right != None):
            return self.right.searchElement(x)
        elif (self.val.number > x) and (self.left != None):
            return self.left.searchElement(x)
        else:
            return None

    def deleteElement(self, x):
        if self.val.number == x:
            if (self.right != None):
                temp = self.right
                while temp.left != None:
                    temp = temp.left
                temp.left = self.left
                return self.right
            elif (self.left != None):
                return self.left
            else:
                return None
        elif (self.val.number < x) and (self.right != None):
            self.right = self.right.deleteElement(x)
            return self
        elif (self.val.number > x) and (self.left != None):
            self.left = self.left.deleteElement(x)
            return self
        else:
            return self


    def orderList(self):
        ordered.append(self.val)
        
        if (self.left != None):
            self.left.orderList()
            
        if (self.right != None):
            self.right.orderList()
