import csv
from structures.bases import ClassicPizza, Margharita, PlainPizza, TurkishPizza
from structures.decorators import Corn, GoatCheese, Meat, Mushroom, Olive, Onion

pizzas = [ClassicPizza(), Margharita(), PlainPizza(), TurkishPizza()]
decorators_uninit = [Corn, GoatCheese, Meat, Mushroom, Olive, Onion]

def decorator_component_initialiser(decorator, component):
    foo = decorator()
    foo.component = component

    return foo

def main():
    menu = str()
    with open("Menu.txt", encoding="utf-8") as menu_file:
        menu = menu_file.read()

    items = dict()

    for item in list(filter(lambda line: not line.startswith("*"),menu.split("\n"))):
        index, *name = item.split(":")

        items[index] = ' '.join(name).strip()
    
    print(menu)

    with open('Orders_Database.csv', encoding="utf-8", mode="a", newline="\n") as csv_file:
        db = csv.writer(csv_file)

        pizza_index = str(input("Bir Pizza Seçin: "))
        pizza = next((item for item in pizzas if item.get_description() == items[pizza_index]), None)

        print("\n" + pizza.get_description() + "\n")

        decorators = map(lambda x: decorator_component_initialiser(x, pizza), decorators_uninit)

        decorator_index = str(input("Bir Sos Seçin: "))
        decorator = next((item for item in decorators if item._Decorator__description == items[decorator_index]), None)

        print("\n" + decorator.get_description())
        print(str(decorator.get_cost()) + "TL\n")

        username = str(input("Kullanıcı adınızı girin: "))
        tc_no = str(input("TC Kimliğinizi girin: "))
        cc_no = str(input("Kredi Kartı Numaranızı girin: "))
        cc_pass = str(input("Kredi Kartı Şifrenizi girin: "))

        csv_file.write("\n")
        db.writerow([username, tc_no, cc_no, cc_pass])

        print("Siparişiniz Alınmıştır!")
main()