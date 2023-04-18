# https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

# Enter your code here. Read input from STDIN. Print output to STDOUT

from sys import stdin

while(True):
    input_value = stdin.readline().strip().split(';')
    if len(input_value) == 1: break
    split_combine = input_value[0]
    method_class_variable = input_value[1]
    words = input_value[2]

    answer = ""

    if split_combine == 'S':
        if method_class_variable == 'C':
            answer += words[0].lower()
            for c in words[1:]:
                if 'A'<=c<='Z': 
                    answer += " " 
                    answer += c.lower()
                elif 'a'<=c<='z': 
                    answer += c
        else:
            for c in words:
                if 'A'<=c<='Z': 
                    answer += " " 
                    answer += c.lower()
                elif 'a'<=c<='z': 
                    answer += c
    elif split_combine == 'C':
        split_words = words.split()
        if method_class_variable == 'V':
            answer += split_words[0]
            for word in split_words[1:]:
                answer += word[0].upper() + word[1:]
        elif method_class_variable == 'C':
            for word in split_words:
                answer += word[0].upper() + word[1:]
        elif method_class_variable == 'M':
            answer += split_words[0]
            for word in split_words[1:]:
                answer += word[0].upper() + word[1:]
            answer += "()"  
            
    print(answer)
