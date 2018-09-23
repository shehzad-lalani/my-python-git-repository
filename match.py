import re

pattern = re.compile('hell')
print(pattern.match('hello world'))
print(pattern.match('New hello world', 4))

print(pattern.search('New hello world'))
print(pattern.search('New hello world', 5))
