from spellchecker import SpellChecker
spell = SpellChecker()

def shuffle(char_list):
    #     if len(char_list) == 2:
#         if char_list[0] == char_list[1]:
#             return([[char_list[0], char_list[1]]])
#         else:
#             return([[char_list[0], char_list[1]],[char_list[1], char_list[0]]])
    if len(char_list) == 1:
        return([char_list])
    else:
        shuffle_list = []
        for char in set(char_list):
            sub_char_list = char_list[:char_list.index(char)]+char_list[char_list.index(char)+1:]
            for char_shuffled in shuffle(sub_char_list):
                shuffle_list.append([char] + char_shuffled)
    return(shuffle_list)
def generate_sub_list(char_list, size = 1):
    if size == 1:
        return([[char] for char in set(char_list)])
    else:
        sub_lists = []
        used_chars = []
        for char in set(char_list):
            sub_list = char_list[:char_list.index(char)]+char_list[char_list.index(char)+1:]
            for used_char in used_chars:
                sub_list = sub_list.replace(used_char, '')
            for clist in generate_sub_list(sub_list, size - 1):
                sub_lists.append([char] + clist)
            used_chars.append(char)
    return(sub_lists) 
def shuffle_all(char_list, min_n = 2, max_n = None):
    words = []
    if max_n is None:
        max_n = len(char_list)
    for i in range(min_n, max_n+1):
        sub_char_lists = generate_sub_list(char_list, i)
        for sub_char_list in sub_char_lists:
            for word in [''.join(chars) for chars in shuffle(sub_char_list)]:
                words.append(word)
    return(words)


words = shuffle_all('igbnne', 4, 7)
for word in sorted(words):
    for i in range(4, 7):
        if (
            len(word) == i #and
#             word[-2] == 'e' and 
#             word[1] == 'r'
           ):
            if spell.known([word]):
                print(word)