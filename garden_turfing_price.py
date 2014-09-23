garden_length = int(input("please enter the length of your garden: "))
garden_width = int(input("please enter the width of your garden: "))

garden_area = garden_width * garden_length - (garden_length * 2) - (garden_width * 2)
cost = garden_area * 10

print("the area of your garden is {0} metres squared unincluding the 1 metre border around the perimeter of the garden, the price to turf your garden is {1}!".format(garden_area,cost))
