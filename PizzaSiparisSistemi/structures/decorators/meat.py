from structures.decorators.base_decorator import Decorator


class Meat(Decorator):

    def __init__(self) -> None:
        super().__init__("Et", 8.99)