action = ""
i=0
item=""
global grocerylist
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
            elif action.lower() == "q":
                break

    def add(self):
        global i       
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
                
    def printlist(self):
        global grocerylist
        print(type(grocerylist))
        Cart.menu(action)
    def delete(self):
        global item
        while item != "q":
            print(grocerylist)
            item=input("Please enter item Number to delete from cart,'q' to quit:  \n\n") 
            if item == "q":
                Cart.menu(action)    
            if item in grocerylist:             
                grocerylist.pop(int(item))
                print(grocerylist)
        print(grocerylist)
        Cart.menu(action)    
Cart.menu(action)