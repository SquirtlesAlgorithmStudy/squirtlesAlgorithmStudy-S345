word = list(input())

  croatia = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

   def check(word, cnt):
        if len(word) == 1:
            return print(cnt+1)
        else:
            if(word[0] == 'c') or (word[0] == 'd') or (word[0] == 'l') or (word[0] == 'n') or (word[0] == 's') or (word[0] == 'z'):
                string = ''.join(word[0:2])

                if string in croatia:
                    del word[0:2]
                    if len(word) == 0:
                        return print(cnt+1)
                    else:
                        return check(word, cnt+1)
                elif string == 'dz':
                    if len(word) == 2:
                        return print(cnt+2)
                    elif word[2] == '=':
                        del word[0:3]
                        if len(word) == 0:
                            return print(cnt+1)
                        else:
                            return check(word, cnt+1)
                    else:
                        del word[0:2]
                        if len(word) == 0:
                            return print(cnt+2)
                        else:
                            return check(word, cnt+2)
                else:
                    del word[0]
                    if len(word) == 0:
                        return print(cnt+1)
                    else:
                        return check(word, cnt+1)

            else:
                del word[0]
                if len(word) == 0:
                    return print(cnt+1)
                else:
                    return check(word, cnt+1)

    check(word, 0)
