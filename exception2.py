from exp import WrongOperation

class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

    def input_data(self):
        try:
            model_number = input("Enter the model number: ")
            if len(model_number) > 4:
                raise WrongOperation("Model number should not have more than 4 digits.")
            self.model_number=model_number

            screen_size = float(input("Enter the screen size (in inches): "))
            if screen_size < 12 or screen_size > 70:
                raise WrongOperation("Screen size should be between 12 and 70 inches.")
            self.screen_size=screen_size
          

            price = float(input("Enter the price (in Rs.): "))
            if price < 0 or price > 5000:
                raise WrongOperation("Price should be between 0 and 5000 Rs.")
            self.price = price
           

        except WrongOperation as e:
            print(e)
            self.model_number = 0
            self.screen_size = 0
            self.price = 0
    def display_data(self):
        print("Model Number ",self.model_number)
        print("Screen Size: ",self.screen_size," inches")
        print("Price: Rs. ",self.price)



tv = Television()
tv.input_data()
print("\nTelevision Information:")
tv.display_data()


    
