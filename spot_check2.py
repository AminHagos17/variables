weight = int(input("please enter the weight: "))

hundred_grams = weight // 100
hundred_grams_remainder = weight % 100

fifty_grams = hundred_grams_remainder // 50
fifty_grams_remainder = hundred_grams_remainder % 50

ten_grams = fifty_grams_remainder // 10
ten_grams_remainder = fifty_grams_remainder % 10

five_grams = ten_grams_remainder // 5
five_grams_remainder = ten_grams_remainder % 5

two_grams = five_grams_remainder // 2
two_grams_remainder = five_grams_remainder % 2

one_grams = two_grams_remainder // 1

print("to carry the weight you have entered, you will need {0} 100g scales, {1} 50g scales, {2} 10g scales, {3} 5g scales, {4} 2g scales and {5} 1g scales.".format(hundred_grams,fifty_grams,ten_grams,five_grams,two_grams,one_grams))
