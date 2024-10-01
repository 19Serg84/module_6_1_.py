# Базовый класс для животных
class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False


# Базовый класс для растений
class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name


# Класс для млекопитающих
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)


# Класс для хищников
class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)


# Класс для цветов
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)


# Класс для фруктов
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем edible на True


# Создаем объекты классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Выводим информацию о животных и растениях
print(a1.name)
print(p1.name)

print(a1.alive)  # True
print(a2.fed)    # False

# Хищник кушает цветок
a1.eat(p1)

# Млекопитающее кушает фрукт
a2.eat(p2)

print(a1.alive)  # False (погиб)
print(a2.fed)    # True
