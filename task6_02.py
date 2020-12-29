'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна.
Проверить работу метода.
    Например: 20 м * 5000 м * 25 кг/(м2*см) * 5 см = 12500000 кг == 12500 т
'''

class Road:
    __asphalt_mass = 25 # кг - масса покрытия площадью 1 м2 и тощиной 1 см

    def __init__(self, lenght, width):
        '''
        :param lenght: длина, м
        :param width: ширина, м
        '''
        self._length = float(lenght)
        self._width = float(width)

    def asphalt_sum(self):
        thickness = input('Укажите толщину дорожного полотна, см:\n>>>')
        while True:
            try:
                thickness = float(thickness)
                break
            except ValueError as e:
                print(f'{e}\nВведено неверное значение.')
        return print(f'Масса дорожного покрытия составит {self._length * self._width * self.__asphalt_mass * thickness / 1000} тонн.')
