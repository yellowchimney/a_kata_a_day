"""
Function takes a string and returns a hashtag of no more than 140 characters,
if the string is empty or the hashtag is longer than 140 characters,
it returns False. All valid hashtags are returned in CamelCase.
"""
def generate_hashtag(s):
    if 0 < len(s):
        capitalized = s.title()
        lst = capitalized.split(" ")
        hashtag = "#" + "".join(lst)
        if len(hashtag) < 141:
            return hashtag
        else: return False
    else: return False
