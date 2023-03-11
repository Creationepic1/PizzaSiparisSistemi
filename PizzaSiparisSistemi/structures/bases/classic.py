from structures.bases.base_pizza import Pizza


class ClassicPizza(Pizza):

    def __init__(self) -> None:
        super().__init__("Klasik", 22.49)