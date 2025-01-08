import re

def parse_int(string):
    number_mapping = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 
        'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 
        'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 
        'nineteen': 19, 'twenty': 20, 
        'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 
        'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100, 
        'thousand': 1000, 'million': 1000000
    }
    
    words = string.replace('-', ' ').split()
    nums = [number_mapping[word] for word in words if word in number_mapping]
    
    result = 0
    temp = 0
    
    for num in nums:
        if num == 1000:
            temp = (temp or 1) * 1000
            result += temp
            temp = 0
        elif num == 100:
            temp = (temp or 1) * 100
        elif num >= 1000:
            result += num
            temp = 0
        else:
            if temp >= 100:
                temp += num
            else:
                temp += num
    result += temp
    
    return result