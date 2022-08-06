import turtle
import pandas
from screen_writer import ScreenWriter

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

screen_writer = ScreenWriter()

data = pandas.read_csv(filepath_or_buffer='50_states.csv')
states = data.state.to_list()

guessed_states = []
states_to_learn = []
score = 0

is_running = True
while is_running:
    answer_state = (screen.textinput(title=f'{score}/{len(states)} States Correct',
                                     prompt='Enter state name: ')).title()
    if answer_state == 'Exit':
        for state in states:
            if state not in guessed_states:
                states_to_learn.append(state)

        data_ditc = {'States to learn': states_to_learn}
        df = pandas.DataFrame(data_ditc)
        df.to_csv(path_or_buf='states_to_learn.csv')
        is_running = False

    if answer_state in states:
        score += 1
        guessed_states.append(answer_state)
        guess_from_csv = data[data.state == answer_state]
        x = int(guess_from_csv.x)
        y = int(guess_from_csv.y)
        screen_writer.write_state(x=x, y=y, answer_state=answer_state)
