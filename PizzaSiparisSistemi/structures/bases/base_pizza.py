class Pizza:
    __description = ""
    __cost = 0

    def __init__(self, description, cost) -> None:
        self.__description = description
        self.__cost = cost

    def get_description(self) -> str:
        return self.__description

    def get_cost(self) -> float:
        return self.__cost
