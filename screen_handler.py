from turtle import Turtle, Screen


class ScreenHandler:
    def __init__(self):
        """
        Initializes the background screen with a map.
        """
        self.response = None
        self.display = Screen()
        self.display.setup(width=800, height=914)
        self.display.bgpic(picname="MapOfIndia.gif")

    def prompt(self, states_guessed):
        """
        Prompt for a user input.
        :param states_guessed: number of states already gueesed by the user
        :return: response of the user
        """
        if states_guessed == 0:
            self.response = self.display.textinput(title="Guess the States",
                                                   prompt="Guess the name of a state.").title()

        elif states_guessed > 0:
            self.response = self.display.textinput(title=f"{states_guessed}/28 States Correct",
                                                   prompt="What's your next guess?").title()
        return self.response

    def write_text(self, text, coordinates):
        """
        Write the supplied text on the given coordinates on the screen.
        :param text:
        :param coordinates:
        :return:
        """
        my_turtle = Turtle()
        my_turtle.hideturtle()
        my_turtle.penup()
        my_turtle.color("purple")
        my_turtle.goto(coordinates)
        my_turtle.write(text, True, align="center", font=("calibri", 10, "bold"))
