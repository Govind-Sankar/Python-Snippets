import sys
place = { 'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1 }
decimal = 0
numeral_str = input("Enter Roman Numerals: ")
numeral = []
for i in range(len(numeral_str)):
	if numeral_str[i] not in place.keys():
		print("Please Enter a vaild Roman Numeral in the format XXXX")
		sys.exit()
	numeral.append(place[numeral_str[i]])

for i in range(len(numeral)):
	if (i == len(numeral) - 1) or (numeral[i] >= numeral[i+1]):
		decimal = decimal + numeral[i]
	else:
		decimal = decimal - numeral[i]
		
print("The value of ", numeral_str, " in decimal is ", decimal)
	