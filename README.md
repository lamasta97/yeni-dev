# yeni-dev

const fs = require('fs');
const path = require('path');

function search_text_in_directory(directory, text_to_search) {
    let total_occurrences = 0;

    const files = fs.readdirSync(directory);

    for (const file of files) {
        if (file.endsWith(".js")) {
            const file_path = path.join(directory, file);
            const content = fs.readFileSync(file_path, 'utf-8');
            const occurrences = (content.match(new RegExp(text_to_search, 'g')) || []).length;
            total_occurrences += occurrences;
        }
    }

    return total_occurrences;
}

function search_multiple_words_in_project(directory, words_to_search) {
    const word_occurrences = {};

    words_to_search.forEach(word => {
        const occurrences = search_text_in_directory(directory, word);
        word_occurrences[word] = occurrences;
    });

    return word_occurrences;
}

const directory_to_search = 'C:\\Users\\hmmer\\newsapi-app';  // Your project directory path
const words_to_search = [
    'news-image', 'news-title'  // Add your list of 2400 words here
    // ... (other words)
];

const word_occurrences = search_multiple_words_in_project(directory_to_search, words_to_search);

for (const word in word_occurrences) {
    const occurrences = word_occurrences[word];
    console.log(`'${word}' used ${occurrences} times.`);
}
