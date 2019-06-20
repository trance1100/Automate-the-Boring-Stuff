def collatz(number):
	if number % 2 == 0:
		print(str(number // 2))
		return number // 2
	elif number % 2 == 1:
		print(str(3 * number + 1))
		return 3 * number + 1


try:
	n = int(input("Enter number:\n"))
except ValueError:
	print("You must enter a integer")
# n = int(input("Enter number:\n"))
while(n != 1):
	n = collatz(n)

