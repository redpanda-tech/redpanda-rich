from random import *
from time import *
block_id=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
block_master=[""]*16
location=block_id[0]
money=10000
class Player:
    def __init__(self,money,location):
        self.money=money
        self.location=location%16
    def dice(self):
        dice_number=randint(1,6)
        return dice_number
    def move(self,number):
        location_now=self.location+number
        return location_now
    def get_money(self,number):
        self.money=self.money+1000
    def lose_money(self,number):
        self.money=self.money-1000
class Game:
    def __init__(self,name,money,location):
        self.location=location%16
        self.name=name
        self.block_id=block_id
        self.block_master=block_master
        self.money=money
        master=self.get_block(location)
        self.judge(name,location,master)
    def set_block(self,location):
        if location<15:
            number=location
        else:
            number=location%16
        self.location=number
        block_number=block_id.index(self.location)
        block_master[block_number]=self.name
    def get_block(self,location):
        if location<16:
            number=location
        else:
            number=location%16
        self.location=number
        block_number=block_id.index(self.location)
        master=block_master[block_number]
        return master
    def judge(self,name,location,master):
        if location<16:
            number=location
        else:
            number=location%16
        self.location=number
        if master=="":
            choise=input("地块:"+str(self.location)+"，需要购买吗?(y/n)")
            if choise=="y":
                self.set_block(location)
                print(block)
            else:
                sleep(0.01)
        else:
            money=self.money-1000
            print("玩家"+name+"剩余"+str(money))
a=Player(money,location)
a.get_money(1000)
print(a.money)
