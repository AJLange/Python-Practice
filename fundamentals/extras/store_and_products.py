class Products:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def print_info(self):
        print(self.name, self.category, "$", f'{self.price:.2f}')
        return self
        
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price * (percent_change/100)
        else:
            self.price -= self.price * (percent_change/100)
        return self


class Store:

    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_product(self, new_product):
        my_product = Products(new_product.name, new_product.price, new_product.category)
        self.products.append(my_product)
        return self
    
    def sell_product(self, id):
        print("Sold")
        Products.print_info(self.products[id])
        self.products.remove(self.products[id])
        return self

    def inflation(self, percent_increase):
        for a_product in self.products:
            a_product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for a_product in self.products:
            if a_product.category == category:
                a_product.update_price(percent_discount, False)
        return self


# various tests

my_first_product = Products("Bath Towel", 10, "Home goods")
my_second_product = Products("Oven Mitts", 40, "Home goods")
my_third_product = Products("Headphones", 60, "Electronics")

Products.print_info(my_second_product)

new_store = Store("CostCo")
print(new_store.products)

new_store.add_product(my_first_product).add_product(my_second_product).add_product(my_third_product)
#this shows that the objects are added to the list, though it doesn't print their info yet
print(new_store.products)

#can print an individual item like this
Products.print_info(new_store.products[0])
Products.print_info(new_store.products[1])
Products.print_info(new_store.products[2])

new_store.sell_product(1)

new_store.inflation(20)
print("Price after inflation")
Products.print_info(new_store.products[0])
Products.print_info(new_store.products[1])


new_store.set_clearance("Electronics", 50)
print("Price after clearance")
Products.print_info(new_store.products[0])
Products.print_info(new_store.products[1])
