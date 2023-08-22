import pandas as pd
import turtle
from screen_handler import ScreenHandler

screen = ScreenHandler()
states = pd.read_csv("states.csv")
states["Coordinates"] = 0
coordinates = []
MAP_DATA_DICT = {}
count = 0


def add_coordinates(current_count):
    """
    Makes a dictionary of state names and their x,y location.

    :param current_count: Number of times the function has been called, Used to iterate over the dataframe to get
    corresponding state name after the user clicks on the screen.
    :return: None
    """

    global count
    MAP_DATA_DICT[states.iloc[current_count, 0]] = coordinates[current_count]
    count += 1


def get_mouse_click_coor(x, y):
    """
    Makes a list and appends to it the coordinates clicked on screen by the user.

    :param x: x coordinate clicked on screen supplied by the onscreenclick() function
    :param y: y coordinate clicked on screen supplied by the onscreenclick() function
    :return: None
    """
    coordinates.append((x, y))
    add_coordinates(count)
    print(coordinates)
    print(f"Click on {states.States[count]}.")


print(f"Click on {states.States[count]}.")
turtle.onscreenclick(get_mouse_click_coor)

screen.display.mainloop()

# Append the dictionary created into a text file after converting it into a string.
with open("mapped_dictionary.txt", "a") as dictionary_file:
    dictionary_file.write(str(f"\n{MAP_DATA_DICT}\n"))
