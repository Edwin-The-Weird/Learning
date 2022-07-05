import math

which_side = str(input("""
Which of the Sides do you want to Find

        |\
        | \
        |  \ Hypotenuse
Height  |   \
        |    \
        |     \
        |______\
          Base


"""))

which_side = which_side.lower()


if which_side == "hypotenuse":
        height = int(input("Height Of the Triangle: "))
        base = int(input("Base of the Triangle: "))

        c_height = height * height
        c_base = base * base
        cZero_hypo = c_height + c_base
        print(math.sqrt(cZero_hypo)) 






