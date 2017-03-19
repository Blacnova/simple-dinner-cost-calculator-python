
# Find the initial price of the meal and convert to a float.
mealprice = float(input("Enter the price of your dinner this evening: "))

# Do the same for the tax.
tax = float(input("Thanks.\nEnter the tax (decimal form): "))

# And the tip.
tip = float(input("Last step, I promise.\nHow much are you willing to cough up to the waiter for his service (decimal form)? "))

# Calculate the final price of the meal, including the tip and the tax.(Although tip should be calculated before tax, to be cheap.)
mealprice = mealprice + mealprice * tax
mealprice = mealprice + mealprice * tip

print("Thanks for using this calculator, your meal will cost you {}, hope it wasn't too expensive! \n Press enter to close.".format(mealprice))
# Waits for enter in a much, much more efficient way.
input("")
