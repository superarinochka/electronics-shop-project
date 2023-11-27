from src.item import Item
class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = int(number_of_sim)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"


    def __str__(self):
        return self.name


    @property
    def number_of_sim(self):
        return self.__number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if isinstance(number_of_sim, int) and number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            return f"ValueError: Количество физических SIM-карт должно быть целым числом больше нуля."