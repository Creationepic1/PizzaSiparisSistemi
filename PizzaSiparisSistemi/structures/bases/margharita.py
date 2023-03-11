from structures.bases.base_pizza import Pizza


class Margharita(Pizza):

    def __init__(self) -> None:
        super().__init__("Margarita", 26.99)