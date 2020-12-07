import pandas as pd
import re

f = open('day7/input.txt', 'r')
input = f.read().split('\n')[:-1]

contain_dict = {i.split(' bags')[0]: {re.search('\d (.*) bag', j).group(1): int(j.split(' ')[0]) for j in i.split('bags contain ')[1].replace('.', '').split(', ') if bool(re.match('^\d', j))} for i in input}

# Answer to Q1
def get_contains_bag(color, contain_dict, bags_containers):
    bags = [key for key, value in contain_dict.items() if color in value.keys()]
    new_bags = [i for i in bags if i not in bags_containers]
    bags_containers = bags_containers + new_bags
    if len(new_bags) > 0:
        for bag in new_bags:
            if bag in list(contain_dict.keys()):
                bags_containers = get_contains_bag(bag, contain_dict, bags_containers)
    return bags_containers

print(f"Bag colors that can contain at least one shiny gold : {len(get_contains_bag('shiny gold', contain_dict, []))}")


# Answer to Q2
def get_number_of_bags_to_contain(color, contain_dict):
    count = 0
    #bags = list(df.columns[pd.notna(df.loc[color])])
    bags = list(contain_dict[color].keys())
    for bag in bags:
        if bag in contain_dict.keys():
            count += contain_dict[color][bag]*(1 + get_number_of_bags_to_contain(bag, contain_dict))
        else:
            count += contain_dict[color][bag]
    return count

print(f"A shiny gold gold should contain {get_number_of_bags_to_contain('shiny gold', contain_dict)} bags")
