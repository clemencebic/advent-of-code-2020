import pandas as pd
import numpy as np

input = pd.read_csv('day5/input.txt', header=None).rename(columns={0: 'seat_binary_code'})

def get_seat_position(code):
    code_list = list(code)
    row_pos = (0, 127)
    col_pos = (0, 7)
    for i in code_list[:7]:
        row_pos = compute_new_position(row_pos, i)
    for i in code_list[7:]:
        col_pos = compute_new_position(col_pos, i)
    return pd.Series([row_pos[0], col_pos[0]])

def compute_new_position(pos, i):
    if (i == 'B') | (i == 'R'):
        new_pos = (pos[0]+(pos[1]-pos[0] + 1)/2, pos[1])
    else:
        new_pos = (pos[0], pos[1]-(pos[1]-pos[0] + 1)/2)
    return new_pos

input[['row_position', 'col_position']] = input['seat_binary_code'].apply(lambda x: get_seat_position(x))
input['seat_id'] = input.row_position*8 + input.col_position

input.sort_values('seat_id', inplace=True)
input['next_is_missing'] = (np.roll(input.seat_id, -1) == input.seat_id + 2)
print(f'Seat ID : {input[input.next_is_missing].seat_id.iloc[0] + 1}')