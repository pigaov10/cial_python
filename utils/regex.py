import re

def find_expression_string(string):
    searched = re.search('logo', string.get("alt"), re.IGNORECASE)
    return searched