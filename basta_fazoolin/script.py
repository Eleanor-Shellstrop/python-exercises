# Original restaurant class
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return "The " + self.name + " menu is available from " + self.start_time + " until " + self.end_time

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            bill += self.items[purchased_item]
        return bill


# Franchise class after main restaurant did well
class Franchaise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def __repr__(self):
        return "This Basta Fazoolin' With My Heart restaurant is located at " + self.address


#----------------------------------------------------------------------------
# Menus
#----------------------------------------------------------------------------

brunch = Menu("brunch", {
    'pancakes': 7.50, 
    'waffles': 9.00, 
    'burger': 11.00, 
    'home fries': 4.50, 
    'coffee': 1.50, 
    'espresso': 3.00, 
    'tea': 1.00, 
    'mimosa': 10.50, 
    'orange juice': 3.50
    }, 
    "11 am", "4 pm")


early_bird = Menu("early bird", {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 
  'espresso': 3.00,
  }, 
  "3 pm", "6 pm" )


dinner = Menu("dinner", {
  'crostini with eggplant caponata': 13.00, 
  'ceaser salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 
  'espresso': 3.00,
  }, 
  "5 pm", "11 pm")


kids = Menu("kids", {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
  }, 
  "11 am", "9 pm")


#----------------------------------------------------------------------------
# Add two locations
#----------------------------------------------------------------------------

flagship_store = Franchaise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchaise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

print(flagship_store.menus)