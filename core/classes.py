class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, brand='', model=''):
        self.brand = brand
        self.model = model

    def __repr__(self):
        return '{} {}'.format(self.brand, self.model)


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, cars=None):
        if cars is None:
            self.cars = []
        else:
            self.cars = cars

    def __getitem__(self, position):
        return self.cars[position]

    def __repr__(self):
        return '{}'.format(self.cars)

    def add(self, new_car):
        self.cars.append(new_car)

    def delete(self, position):
        del self.cars[position]


if __name__ == '__main__':
    garage = Garage([Car('LADA', 'Vesta'), Car('УАЗ', 'Патриот')])
    garage.delete(0)
    garage.add(Car('LADA', 'Granta'))
    for c in garage:
        print(c)