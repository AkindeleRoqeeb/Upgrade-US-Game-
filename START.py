import turtle
import pandas

data = open("50_states.csv")
dta = pandas.read_csv(data)
print(dta)

##############################################################
print(dta["x"])
print(dta["y"])
print(dta["state"])

states = dta.state.to_list()
print(states)

###############################################################
Image = "blank_states_img.gif"
turtle.addshape(Image)
turtle.shape(Image)
turtle.title("State Game")


################################# if the guess state is in cvs########
guess_state = []

while len(guess_state) < 50:
    answer_box = turtle.textinput(title=f"{len(guess_state)}/50 guess any of the state involve in US",
                                  prompt="what's your point").title()

    if answer_box == "Exit":
        missing_states = [state for state in states if state not in guess_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missed_data")
        break

    if answer_box in states:
        guess_state.append(answer_box)
        tb = turtle.Turtle()
        tb.hideturtle()
        tb.penup()
        state_an = dta[dta.state == answer_box]
        tb.goto(int(state_an.x), int(state_an.y))
        # tb.write(answer_box)
        ############## Or ############
        tb.write(state_an.state.item())


######################################### for x and y cordinate #########
# def on_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(on_click_coor)
#####################################################


# turtle.mainloop()

# turtle.exitonclick()