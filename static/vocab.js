
// Fetching words from database
const fetchWords = async (level) => {
    try {
        let vocabCache = JSON.parse(localStorage.getItem('vocabCache')) || {}; //checking to see if there is cache
        if (vocabCache[level]) {
            return vocabCache[level];
        } else {
            const response = await fetch(`/api/vocab/${level}`); //if no cache, then fetch from the server
            const data = await response.json();
            vocabCache[level] = data;

            try {
                localStorage.setItem('vocabCache', JSON.stringify(vocabCache));
            } catch (error) {
                console.error("Error has occured", error);
                // Handle local storage limit exceeded error
            }

            return data;
        }
    } catch (error) {
        console.error("Error has occured", error); //Handle fetch errors
    }
}

// After fetching words, update the word list
const updateWordList = async (words) => {
    const wordList = document.getElementById('word-list');
    wordList.innerHTML = '';

    // listItems is an array of HTML elements
    const listItems = await Promise.all(words.map(async (wordObj) => { //for each word, get the word details and create a list item
        const data = await fetchWordDetails(wordObj.word);
        return createListItem(wordObj.word, data); 
    }));

    for (const listItem of listItems) { //for each list item, append it to the word list
        wordList.appendChild(listItem);
    }
}

const fetchWordDetails = async (word) => {
    let wordDetailsCache = JSON.parse(localStorage.getItem('wordDetailsCache')) || {};
    if (wordDetailsCache[word]){
        return wordDetailsCache[word];
    } else {
        const response = await fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`);
        const data = await response.json();
        wordDetailsCache[word] = data;
        localStorage.setItem('wordDetailsCache', JSON.stringify(wordDetailsCache));
        return data;
    }
}

const createListItem = (word, data) => {
    const listItem = document.createElement('li');
    const pos = data[0].meanings[0].partOfSpeech;
    const definition = data[0].meanings[0].definitions[0].definition;
    listItem.textContent = `${word}: (${pos}) ${definition}`;
    return listItem;
}

['beginner', 'intermediate', 'advanced'].forEach(level => { //for each level, add an event listener to the button
    const button = document.getElementById(level);
    if (button) {
        button.addEventListener('click', async () => {
            const words = await fetchWords(level);
            updateWordList(words);
        });
    }
});