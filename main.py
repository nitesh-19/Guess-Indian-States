from screen_handler import ScreenHandler

MAP_DATA_DICT = {'Andhra Pradesh': (-113.0, -200.0), 'Arunachal Pradesh': (327.0, 194.0), 'Assam': (271.0, 132.0),
                 'Bihar': (87.0, 104.0), 'Chhattisgarh': (-20.0, -9.0), 'Goa': (-239.0, -187.0),
                 'Gujarat': (-291.0, 35.0), 'Haryana': (-171.0, 205.0), 'Himachal Pradesh': (-145.0, 287.0),
                 'Jharkhand': (61.0, 52.0), 'Karnataka': (-203.0, -214.0), 'Kerala': (-177.0, -326.0),
                 'Madhya Pradesh': (-132.0, 32.0), 'Maharashtra': (-214.0, -80.0), 'Manipur': (301.0, 84.0),
                 'Meghalaya': (222.0, 103.0), 'Mizoram': (274.0, 38.0), 'Nagaland': (322.0, 125.0),
                 'Odisha': (55.0, -38.0), 'Punjab': (-195.0, 252.0), 'Rajasthan': (-243.0, 133.0),
                 'Sikkim': (152.0, 162.0), 'Tamil Nadu': (-122.0, -307.0), 'Telangana': (-96.0, -121.0),
                 'Tripura': (240.0, 53.0), 'Uttar Pradesh': (-36.0, 128.0), 'Uttarakhand': (-92.0, 238.0),
                 'West Bengal': (135.0, 36.0)}

screen = ScreenHandler()
game_over = False

states_guessed = []
while not game_over:
    response = screen.prompt(len(states_guessed))
    print(f"Last input: {response}")
    if response in states_guessed:
        print("Already guessed! Try a different one.")
    elif response in MAP_DATA_DICT:
        screen.write_text(text=response, coordinates=MAP_DATA_DICT[response])
        states_guessed.append(response)
        if len(states_guessed) == len(MAP_DATA_DICT):
            print("All states guessed. You Win!")
            game_over = True
    elif response == 'Exit':
        with open("missed_states.csv", "w") as missed_file:
            for key in MAP_DATA_DICT:
                if key in states_guessed:
                    pass
                else:
                    missed_file.write(f"{key} \n")
        game_over = True
    else:
        print("Wrong input, check your spelling.")

screen.display.mainloop()