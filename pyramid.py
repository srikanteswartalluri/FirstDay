rows = 6
#   *
#  ***
# *****
# #
# no_of_stars =
# rows = 3
# spaces : 0 to rows-line
# stars:  1 to
# line   spaces  stars
# 0      2        1
# 1      1        3
# 2      0        5
#
# rows = 4
# 1      3        1   2*1 - 1
# 2      2        3   2*2 - 1
# 3      1        5   2*3 - 1
# 4      0        7   2*4 - 1
#
#    *
#   ***
#  *****
# *******


#for loop to go print each line
for line in range(1, rows+1):
    #print spaces
    for space in range(rows-line):
        print " ",
    #print stars
    for j in range((2*line - 1)):
        print "*",
    print("\n")



