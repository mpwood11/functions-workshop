def main():
    sentence = input("Enter you sentence: ")
    most_freq_letter = find_most_freq_letter(sentence)
    avg_word_len = calc_avg_word_len(sentence)
    sentence_report = create_sentence_report(
        sentence,
        most_freq_letter,
        avg_word_len
        )
    return sentence_report

def find_most_freq_letter(sentence):

    letter_counter = {}

    for char in sentence.lower():
        if char.isalpha():
            letter_counter[char] = letter_counter.get(char, 0) + 1

    most_freq_letter = max(letter_counter, key=letter_counter.get)

    return most_freq_letter.upper()

def calc_avg_word_len(sentence):

    # sanitize the sentence of any non-alphabetic characters to avoid miscounting
    sanitized_sentence = "".join([char for char in sentence if char.isalpha() or char.isspace()])
    words = sanitized_sentence.split()
    char_sum = sum(len(word) for word in words if word.isalpha())
    num_words = len(words)

    return round(char_sum/num_words)

def create_sentence_report(sentence, most_freq_letter, avg_word_len):
    print(
        " --------------------------",
        "\nSENTENCE REPORT\n",
        "--------------------------"
        )
    print("Sentence: ", sentence)
    print("Most frequent letter: ", most_freq_letter)
    print("Average word length: ", avg_word_len)

if __name__ == "__main__":
    #if you run python sentence-statistics.py, then this is true
    main()