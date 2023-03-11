from structures.bases.base_pizza import Pizza


class Decorator:
    component: Pizza = None
    __description = ""
    __cost = 0

    def __init__(self, description, cost) -> None:
        self.__description = description
        self.__cost = cost

    def get_cost(self):
        return self.component.get_cost() + \
            self.__cost 

    def get_description(self):
       return self.component.get_description() + \
         ' ' + self.__description