import os

def search_text_in_directory(directory, text_to_search):
    total_occurrences = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".js"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    occurrences = content.count(text_to_search)
                    total_occurrences += occurrences

    return total_occurrences

def search_multiple_words_in_project(directory, words_to_search):
    word_occurrences = {}

    for word in words_to_search:
        occurrences = search_text_in_directory(directory, word)
        word_occurrences[word] = occurrences

    return word_occurrences

directory_to_search = r"C:\Users\hmmer\newsapi-app"
words_to_search = [
    'news-image','news-title'
    # ... (other words)
]

word_occurrences = search_multiple_words_in_project(directory_to_search, words_to_search)

for word, occurrences in word_occurrences.items():
    print(f"'{word}' used {occurrences} times.")
