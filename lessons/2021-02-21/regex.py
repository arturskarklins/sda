import re

# search -> return first occurence
# pattern = re.compile(r'[A-Z]la')
# print(pattern.search("ala ela Ola"))

# match -> return at start
# print(re.match(r"[A-Z]la", "Ala Ola Ela"))

# fullmatch -> return full string
# print(re.fullmatch(r"[A-Z]la", 'Ela'))

# findall -> find all in list
# print(re.findall(r".la", "Ola ala Ela 0la"))

# finditer -> return iter object
# iter_regex = re.finditer(r".la", "Ola XLa ala Ela 1la")
# for finds in iter_regex:
#     print(finds)

# split sample
# print(re.split(r"\W", "apple,pear,grapes,carrot.cabbage,veggies.fruit,yard|terminator-2>pokemon"))

# sub -> replace string with pattern
# print(re.sub(r"[a-z]{3}$", "dog", "Alice has cat"))

# print(re.subn(r"[a-z]{4}", "dog", "Alice has cat"))

urls = """
http://youtube.com
https://www.google.org
http://www.twitter.co.uk
https://facebook.net
http:
https://
"""

pattern = re.compile(r'(http|https)://(www.)?([a-z]+)\.([a-z.]+)')
print(type(pattern))

finds = pattern.finditer(urls)
for find in finds:
    print(find.group(4))
