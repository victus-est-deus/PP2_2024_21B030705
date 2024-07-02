import re


# 1
def match_ab(text):
    pattern = 'ab*'
    if re.match(pattern, text):
        return "Found a match!"
    else:
        return "No match!"


print(match_ab("ac"))
print(match_ab("abbbb"))


# 2
def match_abb(text):
    pattern = 'ab{2,3}'
    if re.match(pattern, text):
        return "Found a match!"
    else:
        return "No match!"


print(match_abb("ab"))
print(match_abb("abbb"))


# 3
def find_sequences(text):
    return re.findall(r'[a-z]+_[a-z]+', text)


print(find_sequences("my_variable_name another_var something"))


# 4
def find_cap_sequences(text):
    return re.findall(r'[A-Z][a-z]+', text)


print(find_cap_sequences("ExampleString ForTesting"))


# 5
def match_a_anything_b(text):
    pattern = 'a.*b$'
    if re.match(pattern, text):
        return "Found a match!"
    else:
        return "No match!"


print(match_a_anything_b("aabbbdb"))
print(match_a_anything_b("aabBb"))


# 6
def replace_with_colon(text):
    return re.sub(r'[ ,.]', ':', text)


print(replace_with_colon("Hello, World. Here are: spaces, commas, and dots."))


# 7
def snake_to_camel(text):
    return ''.join(word.title() for word in text.split('_'))


print(snake_to_camel("this_is_snake_case"))


# 8
def split_at_uppercase(text):
    return re.findall('[A-Z][^A-Z]*', text)


print(split_at_uppercase("ThisIsCamelCase"))


# 9
def insert_spaces(text):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', text)


print(insert_spaces("ThisIsATestString"))


# 10
def camel_to_snake(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()


print(camel_to_snake("ThisIsCamelCase"))
