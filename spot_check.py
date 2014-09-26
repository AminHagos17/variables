width_pool = int(input("please enter the width of the pool: "))
length_pool = int(input("please enter the length of the pool: "))
depth_pool = int(input("please enter the depth of the pool: "))

main_section_volume = width_pool * length_pool * depth_pool
circle_radius = width_pool / 2
circle_area = 3.14 * (circle_radius * circle_radius)
half_circle_volume = (circle_area / 2) * depth_pool

pool_volume = main_section_volume + half_circle_volume

print("the volume of the pool is {0}!".format(pool_volume))
