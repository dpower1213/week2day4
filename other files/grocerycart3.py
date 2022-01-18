action = ""
i = 1
item=dict()
list=[]
class Cart():
    
    def __init__(self,item,action,i):
        self.item=item
        self.action=action
        self.i=i
        list=[]

    def menu(self):
        i=0      
        action = input("Select desired action,\'a'=Add Item,\'d'=Delete Item 'd'\'q'=Quit,\'p'=Print list")
        while item != "q":           
            if action.lower() == "a":
                Cart.add(self)
            elif action.lower() == "d":
                Cart.delete(self)
            elif action.lower() == "p":
                Cart.display(self)
                       
        print(action)
        # return action
    
    def add(self):
        # i=0
        item=input("Please enter item to add to cart,'q' to quit:  \n\n") 
        print(item)
        list=list.append.items()
        while item != "q":
            # i=i+1
            item=input("Please enter item to add to cart,'q' to quit:  \n\n")
            if item == "q":
                del item
                print(item)
                Cart.menu(action)
        
            print(item)
    
    def delete(self):
        i=Cart.i
        print(i)
        while item[i] != "q":
            print(item)
            item=input("Please enter item Number to delete from cart,'q' to quit:  \n\n") 
            item.pop[i]    
            if item == "q":
                break

    def delete(self):
        i=Cart.i
        print(i)
        while item[i] != "q":
            print(item)
            item=input("Please enter item Number to delete from cart,'q' to quit:  \n\n") 
            item.pop[i]    
            if item == "q":
                break

Cart.menu(action)
