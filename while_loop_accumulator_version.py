def get_starting_number():
    bottle_count = input("How many bottles of beer on the wall? ")

    while not bottle_count.isnumeric() or int(bottle_count) < 1:
        bottle_count = input("How many bottles of beer on the wall? ")

    bottle_count = int(bottle_count)
    return bottle_count

def sing(starting_number):
    bottle_count = starting_number

    while bottle_count > 0:
        next_bottle_count = bottle_count - 1

        if bottle_count == 1:
            bottle_text_current = "1 bottle"
        else:
            bottle_text_current = str(bottle_count) + " bottles"

        if next_bottle_count == 1:
            next_bottle_text = "1 bottle"
        elif next_bottle_count == 0:
            next_bottle_text = "no more bottles"
        else:
            next_bottle_text = str(next_bottle_count) + " bottles"
        print(bottle_text_current + " of beer on the wall, " + bottle_text_current + " of beer.")

        if bottle_count == 1:
            print("Take it down, pass it around, " + next_bottle_text + " of beer on the wall!")
        else:
            print("Take one down, pass it around, " + next_bottle_text + " of beer on the wall.")

        if bottle_count > 1:
            print()

        bottle_count = bottle_count - 1


