class MenuItem:
    def __init__(self, name, category, price):
        self.name = str(name)
        self.category = str(category)
        self.price = price

    def __str__(self):
        return f"{self.name}, {self.category},  \u20A8 {self.price:.2f}"

class MenuManager:
    def __init__(self):
            self.menu_items = {}

    def add_item(self, item):
        if item.category not in self.menu_items:
            self.menu_items[item.category] = {}
            self.menu_items[item.category][item.name] = item.price
            print(f"Added {item.name} to the category {item.category}")
        else:
            self.menu_items[item.category][item.name] = item.price
            print(f"Added {item.name} to the category {item.category}")

    def remove_item(self,item):
        if item.category not in self.menu_items:
            return  
        elif item.name not in self.menu_items[item.category]: 
            return 
        else:
            del self.menu_items[item.category][item.name]
            print(f"Removed the item {item.name} from the category {item.category}")

    def update_item_price(self, item):
        if item.category not in self.menu_items:
            return
        elif item.name not in self.menu_items[item.category]: 
            return 
        else:
            self.menu_items[item.category][item.name] = item.price
            print(f"Updated {item.name} to the price {item.price}")
    
    def list_items_by_category(self,category):
        if category not in self.menu_items:
            return
        else:
            print(f"{category}: ")
            for items in self.menu_items[category]:
                print(items)   

    def remove_orphan(self):
        for category in self.menu_items:
            if len(category)!=0:
                return
            else:
                del self.menu_items[category]
                print(f"Removed orphan category: {category}\n")


menu_manager = MenuManager()

latte = MenuItem("Latte", "Beverage", 70.50) 
cola = MenuItem("Cola", "Beverage", 50.20)
mango_shake = MenuItem("Mango Shake", "Beverage", 60.45)
samosa = MenuItem("Samosa", "Snack", 50.20)

menu_manager.add_item(latte)
menu_manager.add_item(cola)
menu_manager.add_item(mango_shake)
menu_manager.add_item(samosa)
print()

menu_manager.remove_item(samosa)
menu_manager.list_items_by_category("Beverage")