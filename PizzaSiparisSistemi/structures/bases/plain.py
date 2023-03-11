from structures.bases.base_pizza import Pizza


class PlainPizza(Pizza):

    def __init__(self) -> None:
        super().__init__("Sade Pizza", 62.99)
