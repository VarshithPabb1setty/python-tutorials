from Chef import Chef

class ChineseChef(Chef):
    def make_fried_rice(self):
        print("Making fried rice")
    
    def make_chicken(self): # Method oveerriding
        print("Making orange chicken")