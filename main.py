class Car:
    def __init__(self, make, model, color, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.mileage = mileage

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Color: {self.color}, Mileage: {self.mileage}")

    def update_info(self):
        while True:
            print("Which data You would want to change:")
            print("1. Model")
            print("2. Color")
            print("3. Mileage")
            print("4. Make")
            print("5. Finish updating")
            choice = input("Enter your choice: ")
        
            if choice == "1" or choice == "one":
                while True:
                    new_model = input("Enter new model: ")
                    if new_model == "":
                        print("Invalid input")
                    else:
                        self.model = new_model
                        print(f"The model will change to {self.model}")
                        break
            
            elif choice == "2" or choice == "two":
                while True:
                    new_color = input("Enter new color: ")
                    if new_color == "":
                        print("Invalid input")
                    else:
                        self.color = new_color
                        print(f"Your new color will change to {self.color}")
                        break
            
            elif choice == "3" or choice == "three":
                while True:
                    try:
                        new_mileage = int(input("Enter new mileage: "))
                        if new_mileage <= -1:
                            print("Mileage must be a positive integer.")
                        else:
                            self.mileage = new_mileage
                            print(f"Cars mileage will change to {self.mileage}")
                            break
                    except ValueError:
                        print("Invalid input. Please enter a whole number.")
        
            elif choice == "4" or choice == "four":
                while True:
                    new_make = input("Enter car news Make:")
                    if new_make == "":
                        print("Invalid input")
                    else:
                        self.make = new_make
                        print(f"Your cars new make is {self.make}")
                        break
            
            elif choice == "5" or choice == "five":
                break
            else:
                print("Your choice isn't valid")

car1 = Car("Honda", "Avanza", "Black", 1000)
car1.display_info()
car1.update_info()
car1.display_info()
