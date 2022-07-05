import math

which_side = str(input("""
Which of the Sides do you want to Find

        |\\
        | \\
        |  \ Hypotenuse
Height  |   \\
        |    \\
        |     \\
        |______\\
          Base\


"""))

which_side = which_side.lower()


if which_side == "hypotenuse":
        height = int(input("Height Of the Triangle: "))
        base = int(input("Base of the Triangle: "))

        c_height = height * height
        c_base = base * base
        cZero_hypo = c_height + c_base
        c_hypo = math.sqrt(cZero_hypo)
        c_hypo = str(c_hypo)
        print("Hypotenuse: " + c_hypo)

elif which_side == "height":
        hypo = int(input("Hypotenuse of the Triangle: "))
        base = int(input("Base of the Triangle: "))

        c_hypo = hypo * hypo
        c_base = base * base
        cZero_height = c_hypo - c_base
        c_height = math.sqrt(cZero_height)
        c_height = str(c_height)
        print("Height: " + c_height)

elif which_side == "base":
        hypo = int(input("Hypotenuse of the Triangle: "))
        height = int(input("Height Of the Triangle: "))

        c_hypo = hypo * hypo
        c_height = height * height
        cZero_base = c_hypo - c_height
        c_base = math.sqrt(cZero_base)
        c_base = str(c_base)
        print("Base: " + c_base)