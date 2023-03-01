class Inventory:
    items = []

    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        left_capacity = self.__capacity
        self.left_capacity = left_capacity

    def add_item(self, item:str):
        if self.left_capacity > 0:
            self.left_capacity -= 1
            Inventory.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(Inventory.items)}.\nCapacity left: {int(self.__capacity) - int(len(Inventory.items))}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
