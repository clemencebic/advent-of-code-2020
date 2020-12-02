import pandas as pd

input = pd.read_csv('input.txt', sep=' ', header=None)
input.columns = ['occurrence', 'letter', 'password']
input.letter = input.letter.str[0]
input['min_occurrence'] = input.occurrence.apply(lambda x: x.split('-')[0]).astype('int')
input['max_occurrence'] = input.occurrence.apply(lambda x: x.split('-')[1]).astype('int')
input['count_appearance'] = input[['letter', 'password']].apply(lambda x: x[1].count(x[0]), axis=1)
input['password_correct'] = (input.count_appearance >= input.min_occurrence) & \
                            (input.count_appearance <= input.max_occurrence)

# Answer to Q1
input['count_appearance'] = input[['letter', 'password']].apply(lambda x: x[1].count(x[0]), axis=1)
input['password_correct'] = (input.count_appearance >= input.min_occurrence) & \
                            (input.count_appearance <= input.max_occurrence)
print(f'Number of correct passwords : {input.password_correct.sum()}')


# Answer to Q2
input['correct_first_pos'] = input[['letter',
                                      'password',
                                      'min_occurrence']].apply(lambda x: (x[1][x[2]-1] == x[0]), axis=1)
input['correct_second_pos'] = input[['letter',
                                      'password',
                                      'max_occurrence']].apply(lambda x: (x[1][x[2]-1] == x[0]), axis=1)

input['password_correct_Q2'] = (input.correct_first_pos != input.correct_second_pos)
print(f'Number of correct passwords : {input.password_correct_Q2.sum()}')

