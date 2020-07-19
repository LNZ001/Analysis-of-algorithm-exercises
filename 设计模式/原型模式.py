'''
利用深浅拷贝得到多个图层.进行完善. 节省了资源.
'''
from copy import copy, deepcopy
class simpleLayer:
    background=[0,0,0,0]
    content="blank"
    def getContent(self):
        return self.content
    def getBackgroud(self):
        return self.background
    def paint(self,painting):
        self.content=painting
    def setParent(self,p):
        self.background[3]=p
    def fillBackground(self,back):
        self.background=back
    def clone(self):
        return copy(self)
    def deep_clone(self):
        return deepcopy(self)