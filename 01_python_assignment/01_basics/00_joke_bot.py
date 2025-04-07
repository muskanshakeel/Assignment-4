joke = "Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs"
prompt = "what do you want"
sorry = "sorry i can only tell a jokes"

def joke_bot():
    user_input = input("what do you want")
    if "joke"  == user_input:
        print(f"HERE IS THE {joke}")
    else:
        print(f"{sorry}")
joke_bot()