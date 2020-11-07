#%%
class Store:
  def __init__(self, name):
    self.name = name
    self.items = []

  def add_item(self, name, price):
    self.items.append({"name": name, "price": price})
  
  def stock_price(self):
    total = 0
    for item in self.items:
      total = item["price"] + total
    return total 
    # OR 
    # return sum([item['price'] for item in self.items])

  @classmethod
  def franchise(cls, store):
    return cls(store.name + " - franchise")

  @staticmethod
  def store_details(store):
    print(f"{store.name}, total stock price: {int(store.stock_price())}")
  

store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

store3 = Store.franchise(store)
Store.franchise(store2)

Store.store_details(store)
Store.store_details(store2)

print(store3.name)