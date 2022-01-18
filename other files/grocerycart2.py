from ast import IsNot


action = ""
i=0
global item
item=""
grocerylist= dict()

class Cart():
    def __init__(self,item,action):
        self.item=item
        self.action=action

    def menu(self):    
        action = input("Select desired action,\'a'=Add Item,\'d'=Delete Item,\'q'=Quit,\'p'=Print list")
        while item != "q":          
            if action.lower() == "a":
                Cart.add(self)
            elif action.lower() == "d":
                Cart.delete(self)
            elif action.lower() == "p":
                Cart.printlist(self)
                
    def add(self):
        global i
        global grocerylist        
        item=input("Please enter item to add to cart,'q' to quit:  \n\n")
        grocerylist.update({i:item})
        i=i+1
        print(grocerylist)
        print(type(item))
        while item != "q":
            item=input("Please enter item to add to cart,'q' to quit:  \n\n")
            grocerylist.update({i:item})
            print(grocerylist)
            i=i+1
            if item == "q":
                grocerylist.pop(i-1)
                Cart.menu(action)
                i=i-1
            
    def delete(self):
        global item
        a=""
        while item != "q":
            item=input("Please enter item Number to delete from cart,'q' to quit:  \n\n") 
            # if item not in grocerylist:
            #     "please enter a number or 'q'"
            #     Cart.delete(self)
            if item == "q":
                Cart.menu(action)
                break
            print(grocerylist)
            grocerylist.pop(int(item))
            print(grocerylist)                

    def printlist(self):
        global grocerylist
        print(grocerylist)
        print(grocerylist)
        Cart.menu(action)

Cart.menu(action)