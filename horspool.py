

def build_shift_table(pattern):
    pat_len = len(pattern)
    shift_table = {}
    for i in range(0, (pat_len - 2)):
        shift_table[pattern[i]] = pat_len - i
    return shift_table

def horspool(pattern, text, shift_table):
    patternLen = len(pattern)
    textLen = len(text) 
    textIndex = 0
    while textIndex <= textLen - patternLen:
        #check from end of pattern to start
        for patIndex in range(patternLen - 1, -1, -1):
            if [patIndex] != text[textIndex + patIndex]:
                textIndex += shift_table[text[textIndex + patternLen - 1]]
                break
            elif patIndex == 0: #we found it
                return textIndex
    return -1
        
text = '\
     Late, by Myself\n\
     Late, by myself, in the boat of myself,\n\
     no light and no land anywhere,\n\
     cloudcover thick. I try to stay\n\
     just above the surface,\n\
     yet I\'m already under\n\
     and living with the ocean\n\
     \n\
     Mewlana Jalaluddin Rumi\n\
     '
pattern1 = 'ocean'
pattern2 = 'ocean\n'
pattern3 = 'I\'m'
pattern4 = 'by myself, in the boat'

print build_shift_table(pattern1)
print build_shift_table(pattern2)
print build_shift_table(pattern3)
print build_shift_table(pattern4)
horspool(pattern1, text, build_shift_table(pattern1))
horspool(pattern2, text, build_shift_table(pattern2))
horspool(pattern3, text, build_shift_table(pattern3))
horspool(pattern4, text, build_shift_table(pattern4))
