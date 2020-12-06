import pandas as pd
import collections

f = open('day6/input.txt', 'r')
input = f.read().split('\n\n')
input[-1] = input[-1][:-2]

# answer to q1
input_q1 = [i.replace('\n', '') for i in input]
df = pd.DataFrame({'answers': input_q1})
df['nb_yes'] = df.answers.apply(lambda x: len(set(list(x))))
print(f'Sum of yes : {df.nb_yes.sum()}')


# answer to q2
df = pd.DataFrame({'answers': input})
df['nb_members'] = df.answers.apply(lambda x: len(x.split('\n')))
df['nb_yes_per_q'] = df.answers.apply(lambda x: dict(collections.Counter(x.replace('\n', ''))))
df['nb_yes'] = df[['nb_members', 'nb_yes_per_q']].apply(lambda x: list(x[1].values()).count(x[0]), axis=1)
print(f'Sum of yes : {df.nb_yes.sum()}')