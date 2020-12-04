import pandas as pd
import re

f = open('day4/input.txt', 'r')
input = f.read().split('\n\n')
input = [i.replace('\n', ' ') for i in input]
input[-1] = input[-1][:-1]
input = [{pair.split(':')[0]: [pair.split(':')[1]] for pair in row.split(' ')} for row in input]
df = pd.concat([pd.DataFrame(i) for i in input])

expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# Answer to Q1
print(f'Number of valid passports : {pd.notna(df[expected_fields]).min(axis=1).sum()}')

# Answer to Q2
df[['byr', 'iyr', 'eyr']] = df[['byr', 'iyr', 'eyr']].astype(float)
df[['hgt', 'hcl', 'ecl', 'pid']] = df[['hgt', 'hcl', 'ecl', 'pid']].astype('str')
expected_fields_and_format = {'byr': '((int(x) >= 1920) & (int(x) <= 2002)) if pd.notna(x) else False',
                              'iyr': '((int(x) >= 2010) & (int(x) <= 2020)) if pd.notna(x) else False',
                              'eyr': '((int(x) >= 2020) & (int(x) <= 2030) )if pd.notna(x) else False',
                              'hgt': "(bool(re.match('1([5-8][0-9]|9[0-3])cm', x))) | "
                                     "(bool(re.match('(59|6[0-9]|7[0-6])in', x))) ",
                              'hcl': "bool(re.match('#([a-f0-9]{6})$', x))",
                              'ecl': "x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']",
                              'pid': "bool(re.match('^\d{9}$', x))"}

for col in expected_fields:
    print(col)
    df[f'{col}_ok'] = df[col].apply(lambda x: eval(expected_fields_and_format[col]))

print(f"Number of valid passports : {df[[f'{col}_ok' for col in expected_fields]].min(axis=1).sum()}")





