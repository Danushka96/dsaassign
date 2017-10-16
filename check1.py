#Author: Danushka Herath
#Subject: Data Structures and Algorithems II
#Assignment: I
#Used Data Structure: K-D trees

#Imported Libraries
import math
import re

#Node Implementation
class Node:
    def __init__(self,x=None,y=None,z=None):
        self.x=x
        self.y=y
        self.z=z
        self.left=None
        self.right=None
        self.parent=None
        self.color=0 #0 for x and 1 for y and 2 for z

    def Setx(self,x):
        self.x=x

    def Sety(self,y):
        self.y=y

    def Setz(self,z):
        self.z=z

    def isleaf(self):
        if self.left==None and self.right==None:
            return True
        else:
            return False

    def Setcolor(self,data):
        self.color=data

    def Hasleft(self):
        return self.left!=None

    def Getleft(self):
        return self.left

    def Hasright(self):
        return self.right!=None

    def Getright(self):
        return self.right

    def Getparent(self):
        if self.parent==None:
            return -1
        else:
            return self.parent

    def Setparent(self,parent): #parent should be a Node
        self.parent=parent

    def Getcolor(self):
        return self.color

class tree:
    def __init__(self,dem=2):
        self.head=None
        self.dem=dem #This attribute represents the Dimension of the tree

    #This Function changes the Dimension of the tree as user's choise
    def changedem(self,data):
        if self.head==None: #Can't change the dimension of the tree if tree has already inserted a value
            self.dem=data

    #Start the Insert part of the tree
    #The recursive Function of the Start Node
    def insert(self,node,start,min):
        global ans
        global mini
        global parent
        x = self.cladist(start, node)
        if self.head==None:
            self.head=node
        elif start.color==0:
            if start.x<node.x:
                if start.right==None:
                    start.right=node
                    node.Setparent(start)
                    node.Setcolor(1)
                    if x<min:
                        min=x
                        #mini=min
                        parent=start
                        dicset[min]=start
                    mini=min #When Changing the min to new value mini should be changed
                else:
                    x = self.cladist(start, node)
                    if x < min:
                        min=x
                        parent=start
                        dicset[min] = start
                    self.insert(node,start.right,min)

            else:
                if start.left==None:
                    start.left=node
                    node.Setparent(start)
                    node.Setcolor(1)
                    x = self.cladist(start, node)
                    if x < min:
                        min = x
                        parent=start
                        dicset[min] = start
                    mini=min
                else:
                    x = self.cladist(start, node)
                    if x < min:
                        min = x
                        parent=start
                        dicset[min] = start
                    self.insert(node,start.left,min)

        elif start.color==1:
            if start.y<node.y:
                if start.right==None:
                    start.right=node
                    node.Setparent(start)
                    if self.dem==2:
                        node.Setcolor(0)
                    else:
                        node.Setcolor(2)
                    if x < min:
                        min = x
                        parent=start
                        dicset[min] = start
                    mini=min

                else:
                    if x < min:
                        min = x
                        parent=start
                        dicset[min] = start
                    self.insert(node,start.right,min)
            else:

                if start.left==None:
                    start.left=node
                    node.Setparent(start)
                    if self.dem==2:
                        node.Setcolor(0)
                    else:
                        node.Setcolor(2)
                    if x < min:
                        min = x
                        parent=start
                        dicset[min] = start
                    mini=min
                else:
                    if x < min:
                        min = x
                        parent=start
                        dicset[min] = start
                    self.insert(node,start.left,min)
        elif node.color==2:
            if start.z<node.z:
                if start.right==None:
                    start.right=node
                    node.Setparent(start)
                    node.Setcolor(0)
                    if x<min:
                        min=x
                        parent=start
                        dicset[min]=start
                    mini=min
                else:
                    if x < min:
                        min =x
                        parent=start
                        dicset[min]=start
                    self.insert(node,start.right,min)
            else:
                if start.left==None:
                    start.left=node
                    node.Setparent(start)
                    node.Setcolor(0)
                    if x < min:
                        min=x
                        parent=start
                        dicset[min]=start
                    mini=min
                else:
                    if x < min:
                        min=x
                        parent=start
                        dicset[min]=start
    #This function call the above one with a smarter way (x,y)
    def Insert(self,x,y,z=None):
        new=Node(x,y,z)
        start=self.head
        global dicset #for store the minimum values and nodes as a dictionary
        global mini #This Saves minimum value of a insert point
        global ans #For BackTracking process
        global parent
        dicset={} #key - minimum distance and Value is the Node which has minimum
        parent=self.head
        ans=None
        if self.head==None:
            self.head=new
            mini=0
            parent=new
        else:
            mini=self.cladist(start,new)
            dicset[mini]=parent
            self.insert(new,start,mini)
            ans=parent
            self._backtrack(new,parent,mini)
            self._bestmatch(new,self.head,mini)
            print(dicset)
            print("(",x, y,")","\tmin:",round(mini,2),"\tclosest: ","(",ans.x,ans.y,")")
        return dicset
        #print(mini)

    #This function calculate the distance between two points
    def cladist(self,start,node):
        if node==None:
            pass
        elif node.z==None:
            d=math.sqrt(math.pow((start.x-node.x),2)+math.pow((start.y-node.y),2))
            return d
        else:
            d=math.sqrt(math.pow((start.x-node.x),2)+math.pow((start.y-node.y),2)+math.pow((start.z-node.z),2))
            return d

    def checkreturn(self,threshold,x,y,z=None):
        d=self.Insert(x,y,z) #This one is the Dictionary wich has minimum values and it's own nodes
        # keys=d.keys()
        # print(keys)
        # print("(",x,",",y,")\t>\t",end='')
        # count=0
        # for i in keys:
        #     node=d[i]
        #     print("(",node.x,",",node.y,")",end='')
        #     count+=1
        #     if count==threshold:
        #         break
        # print()

    def _backtrack(self,node,parent,min): #parent is a Node is the newly inserted point
        global ans
        cmin=min
        if parent!=self.head and (parent!=None):
            if parent.Getcolor()==0:
                if 0<node.x-parent.x<min or  0<parent.x-node.x<min:
                    if parent.x-node.x>=0:
                        if parent.Hasright():
                            minim=self.cladist(node,parent.right)
                            if minim<cmin:
                                cmin=minim
                                ans=parent
                                dicset[cmin]=parent
                            if not parent.right.isleaf():
                                self._backtrack(node,parent.right,cmin)
                        else:
                            self._backtrack(node,parent.parent,cmin)
                    else:
                        if parent.Hasleft():
                            minim=self.cladist(node,parent.left)
                            if minim<cmin:
                                cmin=minim
                                ans=parent
                                dicset[cmin] = parent
                            if not parent.left.isleaf():
                                self._backtrack(node,parent.left,cmin)
                        else:
                            self._backtrack(node,parent.parent,cmin)
                else:
                    self._backtrack(node,parent.parent,cmin)
            elif parent.Getcolor()==1:
                if 0<node.y-parent.y<min or 0<parent.y-node.y<min:
                    if parent.y-node.y>=0:
                        if parent.Hasright():
                            minim=self.cladist(node,parent.right)
                            if minim<cmin:
                                cmin=minim
                                ans=parent
                                dicset[cmin] = parent
                            if not parent.right.isleaf():
                                self._backtrack(node,parent.right,cmin)
                        else:
                            self._backtrack(node,parent.parent,cmin)
                    else:
                        if parent.Hasleft():
                            minim=self.cladist(node,parent.left)
                            if minim<cmin:
                                cmin=minim
                                ans=parent
                                dicset[cmin] = parent
                            if not parent.left.isleaf():
                                self._backtrack(node,parent.parent,cmin)
            elif parent.Getcolor()==2:
                if 0<node.z-parent.z<min or 0<parent.z-node.z<min:
                    if parent.z-node.z>=0:
                        if parent.Hasright():
                            minim=self.cladist(node,parent.right)
                            if minim<cmin:
                                cmin=minim
                                ans=parent
                                dicset[cmin]=parent
                            if not parent.right.isleaf():
                                self._backtrack(node,parent.right,cmin)
                        else:
                            self._backtrack(node,parent.parent,cmin)
                    else:
                        if parent.Hasleft():
                            minim=self.cladist(node,parent.left)
                            if minim<cmin:
                                cmin=minim
                                ans=parent
                                dicset[cmin]=parent
                            if not parent.right.isleaf():
                                self._backtrack(node,parent.parent,cmin)
                        else:
                            self._backtrack(node,parent.parent,cmin)

    def _bestmatch(self,node,point,min):
        global ans
        if point==self.head:
            if node.x < point.x:
                if (0<node.x-point.x<min or 0<point.x-node.x<min) and (0<node.y-point.y<min or 0<point.y-node.y):
                    minim=self.cladist(point,node)
                    if minim<min:
                        ans=point
                        min=minim
                        dicset[min] = point
                if point.Hasright():
                    #print("Done")
                    self._bestmatch(node,point.right,min)
            else:
                if (0<node.x-point.x<min or 0<point.x-node.x<min) and (0<node.y-point.y<min or 0<point.y-node.y):
                    minim=self.cladist(point,node)
                    if minim<min:
                        ans=point
                        min=minim
                        dicset[min] = point
                if point.Hasleft():
                    self._bestmatch(node,point.left,min)

        elif point!=None:
            #print(point.x,point.y)
            #print("Done")
            if point.Getcolor()==1:
                #print(point.x, point.y)
                if node.y<=point.y:
                    if (0<=node.y-point.y<min or 0<=point.y-node.y<min) and (0<=node.y-point.y<min or 0<=point.y-node.y<min):
                        #print(point.x, point.y)
                        minim=self.cladist(node,point)
                        if minim<min:
                            ans=point
                            min=minim
                            dicset[min] = point
                    if point.Hasleft():
                        #print("Done")
                        self._bestmatch(node,point.left,min)
                else:
                    if 0<node.y-point.y<min or 0<point.y-node.y:
                        minim=self.cladist(node,point)
                        if minim<min:
                            ans=point
                            min=minim
                            dicset[min] = point
                    if point.Hasright():
                        self._bestmatch(node,point.right,min)
            elif point.Getcolor()==0:
                #print(point.x, point.y)
                if node.x<point.x:
                    if (0<=node.x-point.x<min or 0<=point.x-node.x<min) and (0<=node.y-point.y<min or 0<=point.y-node.y<min):
                        minim=self.cladist(node,point)
                        if minim<min:
                            ans=point
                            min=minim
                            dicset[min] = point
                    if point.Hasleft():
                        self._bestmatch(node,point.left,min)
                else:
                    if (0<=node.x-point.x<min or 0<=point.x-node.x<min) and (0<=node.y-point.y<min or 0<=point.y-node.y<min):
                        minim=self.cladist(node,point)
                        if minim<min:
                            ans=point
                            min=minim
                            dicset[min] = point
                    if point.Hasright():
                        self._bestmatch(node,point.right,min)
            elif point.Getcolor()==2:
                #print(point.x, point.y)
                if node.z<point.z:
                    if (0<=node.z-point.z<min or 0<=point.z-node.z<min) and (0<=node.z-point.z<min or 0<=point.z-node.z<min):
                        minim=self.cladist(node,point)
                        if minim<min:
                            ans=point
                            min=minim
                            dicset[min] = point
                    if point.Hasleft():
                        self._bestmatch(node,point.left,min)
                else:
                    if (0<=node.z-point.z<min or 0<=point.z-node.z<min) and (0<=node.z-point.z<min or 0<=point.z-node.z<min):
                        minim=self.cladist(node,point)
                        if minim<min:
                            ans=point
                            min=minim
                            dicset[min] = point
                    if point.Hasright():
                        self._bestmatch(node,point.right,min)
#End of Tree Implementation

#Programming Part Starts from Here
def Createtree(dem):
    global a
    a=tree(dem)

def firstline():
    x = str(input())
    l = x.strip('()').split(' ')
    if len(l)!=2:
        print("Not Valied! Try Again")
        firstline()
    else:
        m= int(l[0])
        n= int(l[1])
        inputlooper(m,n)

def Checkdem():
    global dem
    x=Getinput()
    dem=len(x)
    if len(x)==3:
        Createtree(3)
    elif len(x)==2:
        Createtree(2)
    return x

def Getinput():
    global l
    x = str(input("Enter the Coordinate: "))
    l=x.strip('()').split(',')
    if len(l)!=2 and len(l)!=3:
        print("Not valied! Try Again!")
        return Getinput()
    return l

def inputlooper(m,n):
    k=Checkdem()
    #Start of Fixing Function Checkdem Bug Here(Once he call for input)(To check dem)
    if len(k) == 3:
        x = int(k[0])
        y = int(k[1])
        z = int(k[2])
        a.checkreturn(n, x, y, z)
    elif len(k) == 2:
        x = int(k[0])
        y = int(k[1])
        a.checkreturn(n, x, y)
    else:
        print("Can't Change the Dimension of the tree while insert")
        print("Chance Skipped")
    #End of Bug Correction
    for i in range(m-1):
        k=Getinput()
        if dem==3 and len(k)==3:
            x=int(k[0])
            y=int(k[1])
            z=int(k[2])
            a.checkreturn(n,x,y,z)
        elif dem==2 and len(k)==2:
            x=int(k[0])
            y=int(k[1])
            a.checkreturn(n,x,y)
        else:
            print("Can't Change the Dimension of the tree while insert")
            print("Chance Skipped")

#firstline()
a=tree()

a.checkreturn(2,12,16)
a.checkreturn(2,15,8)
a.checkreturn(2,5,18)
a.checkreturn(2,18,5)
a.checkreturn(2,16,15)
a.checkreturn(2,2,5)
a.checkreturn(2,7,10)
a.checkreturn(2,8,7)
a.checkreturn(2,5,5)
a.checkreturn(2,19,12)
a.checkreturn(2,10,2)
a.checkreturn(2,13,2)
