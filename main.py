
def count_letters(text):
    letters_occur = {}
    for letter in text:
        if letter.isalpha():        
            if letter in letters_occur:
                letters_occur[letter] += 1
            else:
                letters_occur[letter] = 1
    return letters_occur

path_to_file = "books/frankestein.txt"
with open(path_to_file) as f:
    file_content = f.read()


letters_occur = count_letters(file_content.lower())
printing_dict = letters_occur.copy()
for i in range(0, len(letters_occur)):
    max_occurrence = max(printing_dict, key=printing_dict.get)
    print(f"The '{max_occurrence}' character was found {letters_occur[max_occurrence]} times")
    del printing_dict[max_occurrence]