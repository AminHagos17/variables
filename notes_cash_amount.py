#Amin Hagos
#18-09-2014
#Program to find amount of notes needed for a cash amount

money_amount = int(input("please enter your cash amount: "))

twenty_notes = money_amount // 20
twenty_remainder = money_amount % 20

ten_notes = twenty_remainder // 10
ten_remainder = twenty_remainder % 10

five_notes = ten_remainder // 5
five_remainder = ten_remainder % 5

two_coins = five_remainder // 2
two_remainder = five_remainder % 2

one_coins = two_remainder // 1

print("your cash amount, £{0} will turn into {1} £20 notes, {2} £10 notes, {3} £5 notes and {4} £2 coins and {5} £1 coins!".format(money_amount,twenty_notes,ten_notes,five_notes,two_coins,one_coins))
