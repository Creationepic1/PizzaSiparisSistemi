from structures.bases.base_pizza import Pizza


class TurkishPizza(Pizza):

    def __init__(self) -> None:
        super().__init__("TürkPizza", 62.99)
