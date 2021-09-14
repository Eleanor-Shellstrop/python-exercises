#----------------------------------
# Classes
#----------------------------------

# Original restaurant class
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return "The " + self.name + " menu is available from " + str(self.start_time) + " until " + str(self.end_time)

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
        return "This restaurant is located at " + self.address
    
    def available_menus(self, time):
        available_menu = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menu.append(menu)
            else:
                available_menu.append("Sorry, no menu is available at this time")
        return available_menu


# Business class
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


#----------------------------------
# Menus
#----------------------------------

# For Basta Fazoolin

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
    1100, 1600)


early_bird = Menu("early bird", {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 
  'espresso': 3.00,
  }, 
  1500, 1800)


dinner = Menu("dinner", {
  'crostini with eggplant caponata': 13.00, 
  'ceaser salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 
  'espresso': 3.00,
  }, 
  1700, 2300)


kids = Menu("kids", {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
  }, 
  1100, 2100)


# For Take a' Arepa

arepas_menu = Menu("Arepas", {
    'arepa pabellon': 7.00, 
    'pernil arepa': 8.50, 
    'guayanes arepa': 8.00, 
    'jamon arepa': 7.50    
    },
    1000, 2000)


#----------------------------------
# Add three restaurant locations
#----------------------------------

flagship_store = Franchaise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchaise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

arepas_place = Franchaise("189 Fitzgerald Avenue", [arepas_menu])


#----------------------------------
# Add businesses
#----------------------------------

basta_business = Business("Basta Fazoolin' with My Heart", [flagship_store, new_installment])

arepas_business = Business("Take a' Arepa", [arepas_place])