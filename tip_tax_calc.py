from time import sleep
import sys
import msvcrt

mealprice = float(input("Enter the price of your dinner this evening: "))

tax = float(input("Thanks.\nEnter the tax (decimal form): "))

tip = float(input("Last step, I promise.\nHow much are you willing to cough up to the waiter for his service (decimal form)? "))

mealprice = mealprice + mealprice * tax
mealprice = mealprice + mealprice * tip


print("Calculating", end="")
sys.stdout.flush()
sleep(1)

print(".", end="")
sys.stdout.flush()
sleep(1)

print(".", end="")
sys.stdout.flush()
sleep(1)

print(".")


print("Thanks for using this calculator, your meal will cost you %s, hope it wasn't too expensive!" % (mealprice))
sys.stdout.flush()
sleep(3)
print("Press any key to close!")
msvcrt.getch()
