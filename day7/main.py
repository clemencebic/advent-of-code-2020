import pandas as pd
import re

f = open('day7/input.txt', 'r')
input = f.read().split('\n')[:-1]

idx = [i.split(' bags')[0] for i in input]
contain = [i.split('bags contain ')[1].replace('.', '').split(', ') for i in input]
contain_df = [pd.DataFrame({re.search('\d (.*) bag', j).group(1): int(j.split(' ')[0]) for j in i if bool(re.match('^\d', j))},
                           index=[idx[index]]) for index, i in enumerate(contain)]

df = pd.concat(contain_df)

# Answer to Q1
def get_contains_bag(color, df, bags_containers):
    bags = list(df[df[color] >= 1].index)
    new_bags = [i for i in bags if i not in bags_containers]
    bags_containers = bags_containers + new_bags
    if len(new_bags) > 0:
        for bag in new_bags:
            if bag in list(df.columns):
                bags_containers = get_contains_bag(bag, df, bags_containers)
    return bags_containers


print(f"Bag colors that can contain at least one shiny gold : {len(get_contains_bag('shiny gold', df, []))}")


# Answer to Q2
def get_number_of_bags_to_contain(color, df):
    count = 0
    bags = list(df.columns[pd.notna(df.loc[color])])
    for bag in bags:
        if bag in df.index:
            count += df.loc[color, bag]*(1 + get_number_of_bags_to_contain(bag, df))
        else:
            count += df.loc[color, bag]
    return count

print(f"A shiny gold gold should contain {get_number_of_bags_to_contain('shiny gold', df)} bags")
