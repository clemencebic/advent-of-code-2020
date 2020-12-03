import pandas as pd

input = pd.read_csv('input.txt', sep='', header=None)
input[0].str.split('', expand=True)

df = pd.DataFrame(index=range(len(input)))
df[[i for i in range(len(input[0].iloc[0]))]] = input[0].apply(lambda x: pd.Series(list(x)))

# Answer to Q1
pos = (0, 0)
nb_trees = 0
end = len(df)

while pos[0] < len(df)-1:
    pos = (pos[0]+1, (pos[1]+3) % df.shape[1])
    nb_trees += int(df.loc[pos] == '#')

# Answer to Q2

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
final_nb_trees = 1
for slope in slopes:
    pos = (0, 0)
    nb_trees = 0
    end = len(df)

    while pos[0] < len(df) - slope[0]:
        pos = (pos[0] + slope[0], (pos[1] + slope[1]) % df.shape[1])
        nb_trees += int(df.loc[pos] == '#')

    final_nb_trees *= nb_trees

