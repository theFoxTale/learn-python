#инкапсуляция
class Product:
    def __init__(self, name, price, discount=0, stock=0, max_discount=20.0):
        self.name = name.strip()
        if not len(self.name) >= 2:
            raise ValueError('Название товара не может быть короче 3-х символов.')
        
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        
        self.max_discount = abs(int(max_discount))
        if self.max_discount > 75:
            raise ValueError('Скидка на товар не может превышать 75%.')
        
        self.discount = abs(float(discount))
        if self.discount > self.max_discount:
            self.discount = self.max_discount

    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
        # Здесь мы можем как-то взаимодействовать с учетной/бухгалтерской системой
        self.stock -= items_count

    def discounted(self):
        return self.price - (self.price * self.discount / 100)

    def get_color(self):
        raise NotImplementedError
    
    def __repr__(self):
        return f'<Product: name = {self.name}, price = {self.price}, stock = {self.stock}, discount = {self.discount}>'


test_product = Product('Xiaomi Mi Mix 3', 25000, stock=20, discount=5)
print(f'Начальное состояние класса:\n{test_product}')

test_product.price = test_product.discounted()
test_product.sell(2)
print('')
print(f'Класс после продажи:\n{test_product}')

#наследование
class Phone(Product):
    def __init__(self, name, price, color, discount=0, stock=0, max_discount=20.0):
        super().__init__(name, price, discount, stock, max_discount)
        self.color = color

    def get_color(self):
        return f'Цвет корпуса: {self.color}'

    def get_memory_size(self):
        #выводит размер памяти в Гб
        pass

    def __repr__(self):
        return f'<Phone name = {self.name}, price = {self.price}, color = {self.color}, stock = {self.stock}, discount = {self.discount}>'

my_phone = Phone('Huawei P30 Pro', 75670, 'синий металлик', stock=16, discount=9)
print('')
print(f'Отнаследованные классы:\n{my_phone}')

class Sofa(Product):
    def __init__(self, name, price, color, texture, discount=0, stock=0, max_discount=20.0):
        super().__init__(name, price, discount, stock, max_discount)
        self.color = color
        self.texture = texture

    def get_color(self):
        return f'Цвет обивки: {self.color}, тип ткани: {self.texture}'

    def __repr__(self):
        return f'<Sofa name = {self.name}, price = {self.price}, stock = {self.stock}, color = {self.color}, texture = {self.texture}>'

my_sofa = Sofa('Диван "Андрей"', 45600, 'апельсиновый', 'тик premium')
print(my_sofa)

print('')
print(f'get_color для телефона:\n{my_phone.get_color()}')
print('')
print(f'get_color для дивана:\n{my_sofa.get_color()}')