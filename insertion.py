class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def enqueue(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        
        return 'inserted'
    
    def dequeue(self):
        if self.head is None:
            return 'no node'
        else:
            temp=self.head
            if self.head==self.tail:
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
            return temp
    
    def isEmpty(self):
        if self.head is None:
            return True
        return False


class treeNode(object):
	def __init__(self, value):
		self.value = value
		self.l = None
		self.r = None
		self.h = 1

class AVLTree(object):
    
    def getHeight(self,root):
        if not root:
            return 0
        else:
            return root.h
    
    def balance(self,root):
        if not root:
            return 0
        return self.getHeight(root.l)-self.getHeight(root.r)
    
    def rRotate(self,r):
        y=r.l
        r.l=r.l.r
        y.r=r
        
        y.h=1+max(self.getHeight(y.r),self.getHeight(y.l))
        r.h=1+max(self.getHeight(r.r),self.getHeight(r.l))
        
        return y
    
    def lRotate(self,r):
        y=r.r
        r.r=r.r.l
        y.l=r
        
        y.h=1+max(self.getHeight(y.r),self.getHeight(y.l))
        r.h=1+max(self.getHeight(r.r),self.getHeight(r.l))
        
        return y
    
    def insert(self,root,value):
        if not root:
            return treeNode(value)
        elif value<root.value:
            root.l=self.insert(root.l,value)
        else:
            root.r=self.insert(root.r,value)
        
        root.h=1+max(self.getHeight(root.l),self.getHeight(root.r))
        
        b=self.balance(root)
        
        if b>1 and value<root.l.value:       
            return self.rRotate(root)
        if b < -1 and value > root.r.value:
            return self.lRotate(root)
        if b>1 and value>root.l.value:
            root.l=self.lRotate(root.l)
            return self.rRotate(root)
        
        if b<-1 and value<root.r.value:
            root.r=self.rRotate(root.r)
            return self.lRotate(root)
        
        return root  
    
    def preOrder(self,root):
        if not root:
            return
        else:
            print(root.value)
            self.preOrder(root.l)
            self.preOrder(root.r)
    
    def postOrder(self,root):
        if not root:
            return
        else:
            self.postOrder(root.l)
            self.postOrder(root.r)
            print(root.value)
            
    def inOrder(self,root):
        if not root:
            return
        else:
            self.inOrder(root.l)
            print(root.value)
            self.inOrder(root.r)
    
    def levelOrder(self,root):
        if not root:
            return
        else:
            custom=Queue()
            custom.enqueue(root)
            
            while not custom.isEmpty():
                root=custom.dequeue()
                print(root.value.value)
                
                if root.value.l is not None:
                    custom.enqueue(root.value.l)
                
                if root.value.r is not None:
                    custom.enqueue(root.value.r)
    
    def search(self,root,value):
        if not root:
            return
        else:
            custom=Queue()
            custom.enqueue(root)
            
            while not custom.isEmpty():
                root=custom.dequeue()
                if root.value.value==value:
                    return 'found'
                
                if root.value.l is not None:
                    custom.enqueue(root.value.l)
                
                if root.value.r is not None:
                    custom.enqueue(root.value.r)
            
            return 'not found'
    
    def getMinimum(self,root):
        if root is None or root.l is None:
            return root
        return self.getMinimum(root.l)
    
    def deleteNode(self,root,value): #time=O(log n) space=O(log n)
        if not root:
            return
        elif value<root.value:
            root.l=self.deleteNode(root.l,value)
        elif value>root.value:
            root.r=self.deleteNode(root.r,value)
        else:
            if root.l is None:
                temp=root.r
                root=None
                return temp
            elif root.r is None:
                temp=root.l
                root=None
                return temp
            
            temp=self.getMinimum(root.r)
            root.value=temp.value
            root.r=self.deleteNode(root.r,temp.value)
            
        balance=self.balance(root)
        if balance>1 and self.balance(root.l)>=0:#LL
            return self.rRotate(root)
        if balance<-1 and self.balance(root.r)<=0:#RR
            return self.lRotate(root)
        if balance>1 and self.balance(root.l)<0:#LR
            root.l=self.lRotate(root.l)
            return self.rRotate(root)
        if balance<-1 and self.balance(root.r)>0:#RL
            root.r=self.rRotate(root.r)
            return self.lRotate(root)
            
        return root
    
    def deleteWhole(self,root): #time=O(1) space=O(1)
        root.value=None
        root.l=None
        root.r=None
        return 'deleted'

Tree=AVLTree()
root=None

while True:
    a=int(input("""
1 for insert
2 for preOrder
3 for postOrder
4 for inOrder
5 for levelOrder
6 for search
7 for delete
8 for deleting whole
9 for break
                """))
    if a==1:
        value=input("enter the value")
        root=Tree.insert(root,value)
    elif a==2:
        Tree.preOrder(root)
    elif a==3:
        Tree.postOrder(root)
    elif a==4:
        Tree.inOrder(root)
    elif a==5:
        Tree.levelOrder(root)
    elif a==6:
        value=input("value to search ")
        print(Tree.search(root,value))
    elif a==7:
        value=input("enter the node to be deleted")
        Tree.deleteNode(root,value)
    elif a==8:
        print(Tree.deleteWhole(root))
    elif a==9:
        break
    else:
        print("wrong input")