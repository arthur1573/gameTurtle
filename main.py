import turtle
import pandas



# create a window
window = turtle.Screen()
window.title('U.S. States Game(right click open a new window to guess)')





# upload image to the window
image = 'US.gif'
window.addshape(image)
turtle.shape(image)





# get the mouse position number
def get_mouse(x, y):
    print(x, y)

# 1 = left click
turtle.onscreenclick(get_mouse, 1)









# get all states data
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()






guessed_states = []
def write_states(answer_state):
# check input to local data

    # type exit to save text
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        
        # save states to a csv file
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('these_states_need_to_learn.csv')
        turtle.bye()
        
        
    if answer_state in all_states:
        guessed_states.append(answer_state)
        print(guessed_states)
        
        # create a new turtle
        t = turtle.Turtle()
        # t.hideturtle()
        t.penup()
        # t.pendown()
        
        
        # select state information from all_states where state name = answer_state
        # data.state == answer_state ==> return one Ture, 49 False
        push_data = data[data.state == answer_state]
        
        # write state name to picture
        t.goto(int(push_data.x), int(push_data.y))
        t.write(answer_state)

        




# get the player's input state
answer_state = window.textinput(title = f"{len(guessed_states)}/50 correct guess", prompt = "aw, what is the state's name?").title()
print(answer_state)
write_states(answer_state)





# right mouse button, open a new window again
def get_prompt(title, prompt):
    answer_state = window.textinput(title = f'{len(guessed_states)}/50 correct guess', prompt = "hello again, what is the state's name?").title()
    print(answer_state)
    write_states(answer_state)
    





# 3 = right click
turtle.onscreenclick(get_prompt, 3)








# keep window open
turtle.mainloop()




