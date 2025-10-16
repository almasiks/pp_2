
import re
"""
pattern = r'ab*'
test_strings = ['a', 'ab', 'abb', 'ac', 'b', 'aab']

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")
#________________________________________________

pattern = r'ab{2,3}'
test_strings = ['abb', 'abbb', 'abbbb', 'ab', 'a']

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")


#________________________________________________

pattern = r'[a-z]+_[a-z]+'   
text = "hello_world not_valid_123"

matches = re.findall(pattern, text)
print("Matches:", matches)


#________________________________________________

pattern = r'[A-Z][a-z]+'   
text = " My name is Almas and I Love ython."

matches = re.findall(pattern, text)
print("Matches:", matches)


#________________________________________________

pattern = r'a.*b'
test_strings = ['ab', 'a123b', 'axxb', 'a-b', 'ac']

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")

#________________________________________________

text = "Python is, an. awesome language"
result = re.sub(r"[ ,.]", ":", text)
print(result)


#________________________________________________

def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

text = "this_is_a_snake_case_string"
print(snake_to_camel(text))

#________________________________________________

text = "SplitAtUpperCaseLettersExample"
result = re.findall(r'[A-Z][^A-Z]*', text)
print(result)


#________________________________________________

text = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
result = re.sub(r'(?=[A-Z])', ' ', text).strip()
print(result)


#________________________________________________

def camel(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    snake = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    return snake

text = "camelCaseStringExample"
print(camel(text))

""" 
