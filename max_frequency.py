
def find_max_frequency_word(str):

    if str.strip() == '':
        return None

    list = str.split(' ')
    dict = {}
    max_count = 0
    max_word = None
    for i in range(0, len(list)):
        if list[i] not in dict:
            dict[list[i]] = 1
        else:
            dict[list[i]] = dict[list[i]] + 1
        if dict[list[i]] > max_count:
            max_count = dict[list[i]]
            max_word = list[i]
        
    return max_word

def main():
    str = "in the pond the frog is swimming"
    print(find_max_frequency_word(str))


    str = ""
    print(find_max_frequency_word(str))
    
if __name__ == "__main__":
    main()
    
    