action = ""
item=dict()
i = 1
class Cart():
    
    def __init__(self,item,action):
        self.item=item
        self.action=action
        
    def menu(self):       
        action = input("Select desired action,\'a'=Add Item,\'d'=Delete Item 'd'\'q'=Quit,\'p'=Print list")
        while item != "q":           
            if action.lower() == "a":
                Cart.add(self)
            elif action.lower() == "d":
                Cart.delete(self)
            elif action.lower() == "p":
                Cart.display(self)
                       
        print(action)
        return action
    
    def add(self):
        item=dict()
        i=0
        item[i]=input("Please enter item to add to cart,'q' to quit:  ") 
        print(item)
        while item[i] != "q":
            i=i+1
            item[i]=input("Please enter item to add to cart,'q' to quit:  ")
            if item[i] == "q":
                item[i]=[]
                print(item)
                Cart.menu(action)
            print(i)
            print(item)
    def delete(self):
        item==0
        while item[i] != "q":
            print(item)
            item=input("Please enter item Number to delete from cart,'q' to quit:  "/n) 
            item.pop[i]    
            if item == "q":
                Cart.menu(action)
                             
Cart.menu(action)


