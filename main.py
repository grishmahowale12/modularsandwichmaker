import data
from sandwich_maker import SandwichMaker
from cashier import Cashier



# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    while True:
        choice = input("What would you like? (small/medium/large/off/report): ")
        if choice == "off":
            break
        elif choice == "report":
            print(f"Bread: {resources['bread']} slice(s)")
            print(f"Ham: {resources['ham']} slice(s)")
            print(f"Cheese: {resources['cheese']} ounce(s)")
        elif choice in ["small", "medium", "large"]:
            drink = recipes[choice]
            if sandwich_maker_instance.check_resources(drink["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, drink["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, drink["ingredients"])
        else:
            print("Please enter a valid choice.")

if __name__=="__main__":
    main()
