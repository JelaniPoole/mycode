#!/usr/bin/env python3



# Define a class named SpendingOption
class SpendingOption:
    # The initializer method for the class with parameters 'description' and 'price'
    def __init__(self, description, price):
        self.description = description  # Assigns the provided description to the instance
        self.price = price              # Assigns the provided price to the instance
        self.price_revealed = False     # Initializes a flag to track if the price has been revealed

    # A method to reveal the price of the spending option
    def reveal_price(self):
        self.price_revealed = True      # Sets the flag to indicate the price has been revealed
        return self.price               # Returns the price of the option

# Define a function 'ask_question' with parameters 'question' and 'options'
def ask_question(question, options):
    print(question)                    # Prints the provided question
    # Enumerates through the options, starting the count at 1
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option.description}")  # Prints each option with its number

    while True:  # An infinite loop to repeatedly ask the user until a valid input is given
        try:
            # Asks the user to choose an option and converts the input to an integer
            choice = int(input("Choose an option (1-{}): ".format(len(options))))
            # Checks if the choice is within the range of available options
            if 1 <= choice <= len(options):
                selected_option = options[choice - 1]  # Retrieves the chosen option from the list
                price = selected_option.reveal_price() # Calls the reveal_price method on the chosen option
                # Prints the chosen option's description and cost
                print(f"You chose: {selected_option.description} - Cost: ${price:,}\n")
                return price  # Returns the price of the chosen option
            else:
                # If the choice is out of range, informs the user
                print(f"Please enter a number between 1 and {len(options)}.\n")
        except ValueError:
            # If the input is not a valid integer, informs the user
            print("Invalid input. Please enter a number.\n")


def main():
    total_spent = 0

    # questions and options
    stay_options = [
        SpendingOption("Burj Al Arab: Dubai", 59616),
        SpendingOption("Hotel Lutetia: Paris, France", 84000),
        SpendingOption("Bulgari Tokyo: Tokyo, Japan", 210000),
        SpendingOption("The Ranch at Rock Creek: Philipsburg, Montana", 101500),
        SpendingOption("Velaa Private Island: Republic of Maldives, Maldives", 126000),
        SpendingOption("Amanyara: Turks and Caicos", 56000),
    ]
    total_spent += ask_question("1. Where will you stay?\n", stay_options)

    transport_options = [
        SpendingOption("Private Jet Rental", 250000),
        SpendingOption("Luxury Yacht Charter", 150000),
        SpendingOption("Exotic Car Rental", 70000),
        SpendingOption("Private Helicopter Rental", 125000),
        SpendingOption("First-Class Rail Pass", 50000),
        SpendingOption("Personal Chauffeur Service", 30000)
    ]
    total_spent += ask_question("2. What is your mode of transportation for the week?\n", transport_options)

    pamper_options = [
        SpendingOption("Full-Week Spa Retreat", 50000),
        SpendingOption("Luxury Day at a Thermal Spring", 10000),
        SpendingOption("Personal Yoga and Meditation Retreat", 15000),
        SpendingOption("High-End Beauty Treatment Package", 20000),
        SpendingOption("Luxury Shopping Spree with a Personal Stylist", 50000),
        SpendingOption("VIP Entertainment Experience", 40000)
    ]

    total_spent += ask_question("3. What will you do to pamper yourself?\n", pamper_options)

    chef_options = [
        SpendingOption("Gordon Ramsay", 200000),
        SpendingOption("Rachael Ray", 300000),
        SpendingOption("Guy Fieri", 100000),
        SpendingOption("Masaharu Morimoto", 50000),
        SpendingOption("Wolfgang Puck", 75000),
        SpendingOption("Bobby Flay", 50000)
    ]

    total_spent += ask_question("4. What celebrity chef do you want to cook lunch for you?\n", chef_options)

    lunch_options = [
        SpendingOption("Caviar and Champagne", 15000),
        SpendingOption("Kobe Beef Steak", 12000),
        SpendingOption("Truffle Tasting Menu", 10000),
        SpendingOption("Lobster Feast", 9000),
        SpendingOption("Sushi Omakase", 11000),
        SpendingOption("Vegan Gourmet Experience", 8000)
    ]

    total_spent += ask_question("5. What do you want for lunch?\n", lunch_options)

    gadget_options = [
        SpendingOption("Orpheus headphones", 55000),
        SpendingOption("Samsung Gear S2 by de GRISOGONO Smartwatch", 15000),
        SpendingOption("Canon EOS R3", 5999),
        SpendingOption("High-Performance Rion Thrust RE90 Electric Scooter", 6800),
        SpendingOption("Baronics Automated Personal Bartender", 110000),
        SpendingOption("High-End Fitness Equipment with Virtual Training", 10000)
    ]

    total_spent += ask_question("6. What gadget would you buy?\n", gadget_options)

    party_options = [
        SpendingOption("Famous Club in Ibiza", 150000),
        SpendingOption("Rooftop Venue in New York City", 100000),
        SpendingOption("Beachfront Resort in Malibu", 80000),
        SpendingOption("Exclusive Vineyard in Napa Valley", 120000),
        SpendingOption("Penthouse Suite in Las Vegas", 180000),
        SpendingOption("Safari Lodge in South Africa", 220000),
    ]

    total_spent += ask_question("7. Throw a party at one of these places!\n", party_options)

    perform_options = [
        SpendingOption("Calvin Harris", 250000),
        SpendingOption("Morgan Wallen", 250000),
        SpendingOption("Jack Harlow", 250000),
        SpendingOption("Pete Davidson", 100000),
        SpendingOption("Hozier", 250000),
        SpendingOption("The Chainsmokers", 500000),
    ]

    total_spent += ask_question("8. Which celebrity will be performing at the party?\n", perform_options)

    dinner_options = [
        SpendingOption("Dinner at the Eiffel Tower, Paris", 20000),
        SpendingOption("Exclusive Sushi Restaurant in Tokyo", 15000),
        SpendingOption("Michelin Star Restaurant in New York", 25000),
        SpendingOption("Underwater Restaurant in the Maldives", 30000),
        SpendingOption("Rooftop Dining in Dubai", 18000),
        SpendingOption("Historic Winery in Tuscany", 22000),
    ]

    total_spent += ask_question("9. Where do you want to have dinner?\n", dinner_options)

    drink_options = [
        SpendingOption("Legacy by Angostura Rum", 25000),
        SpendingOption("The Winston Cocktail", 12500),
        SpendingOption("Penfolds Grange Hermitage 1951 Wine", 50000),
        SpendingOption("Balvenie 50-Year-Old Single Malt Scotch", 38000),
        SpendingOption("Clase Azul 15th Anniversary Edition Tequila", 30000),
        SpendingOption("Russo-Baltique Vodka", 100000)
    ]

    total_spent += ask_question("10. Pick an expensive drink!\n", drink_options)

    bucket_list_options = [
        SpendingOption("Hot Air Balloon Ride over Cappadocia, Turkey", 500),
        SpendingOption("Scuba Diving in the Great Barrier Reef, Australia", 600),
        SpendingOption("Skydiving Over the Swiss Alps", 700),
        SpendingOption("Sailing Trip Around the Greek Islands", 5000),
        SpendingOption("Wildlife Safari in Kenya", 4000),
        SpendingOption("Attend a Major Fashion Show in Paris (VIP Access)", 2000),
    ]

    total_spent += ask_question("11. Check something off your bucket list!\n", bucket_list_options)

    useless_options = [
        SpendingOption("Lalique Crystal Tourbillons Grand Vase", 200000),
        SpendingOption("Gucci Crocodile Skin Bomber Jacket", 60000),
        SpendingOption("Bang & Olufsen BeoLab 90 Loudspeakers", 85000),
        SpendingOption("Patek Philippe Grand Complications Watch", 60000),
        SpendingOption("Diamond Encrusted Bluetooth Headset", 50000),
        SpendingOption("Soild gold toothpick", 445),
    ]

    total_spent += ask_question("Finally, pick an unnecessary expensive item to buy!\n", useless_options)

    # Results
    if total_spent >= 1000000:
        print(f"Congratulations! You spent ${total_spent:,} you big baller!")
    else:
        print(f"Sorry, you only managed to spend ${total_spent:,}!")

if __name__ == "__main__":
    main()

