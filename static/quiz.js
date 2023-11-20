// Load the words for the quiz
async function loadWords(level) {
    try {
        // Fetch 7 random words for the level
        const response = await fetch(`/api/vocab/${level}`);
        const words = await response.json();

        // Clear any previous lists
        const wordList = document.getElementById('word-list');
        wordList.innerHTML = '';

        // Add each word to the word list
        for (const word of words) {
            const wordElement = document.createElement('div');
            const vocabWordElement = document.createElement('strong');
            vocabWordElement.textContent = word.word;
            wordElement.appendChild(vocabWordElement); //adding the strong to the div
            wordList.appendChild(wordElement); //adding the div to the word-list

            // Fetch and add definitions for the word
            const definitions = await fetchDefinitions(word.id);
            shuffleArray(definitions); //shuffle the multiple choice responses
            for (const definition of definitions) {
                const definitionElement = createDefinitionElement(definition);
                wordList.appendChild(definitionElement);
            }
        }
    } catch (error) {
        console.error("Error has occurred:", error);
    }
}

//Fetch definitions for a word
async function fetchDefinitions(wordId) {
    try {
        let definitionsCache = JSON.parse(localStorage.getItem('definitionsCache')) || {};
        if (definitionsCache[wordId]) {
            return definitionsCache[wordId];
        } else {
            const response = await fetch(`/api/definitions/${wordId}`);
            const data = await response.json();
            definitionsCache[wordId] = data;
            localStorage.setItem('definitionsCache', JSON.stringify(definitionsCache));
            return data;
        }
    } catch (error) {
        console.error("Error has occurred:", error);
        // Handle fetch or local storage error
    }
}

//Shuffle an array
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

// Create a definition element
function createDefinitionElement(definition) {
    const definitionElement = document.createElement('p');
    definitionElement.textContent = definition.definition;
    definitionElement.style.cursor = 'pointer';
    definitionElement.addEventListener('click', () => {
        definitionElement.style.backgroundColor = definition.is_correct ? 'green' : 'red';
    });
    return definitionElement;
}

//Iterating over an array of strings and for each one, get the element in the DOM corresponding to the level
['beginner', 'intermediate', 'advanced'].forEach(level => {
    const button = document.getElementById(level);
    if (button) {
        button.addEventListener('click', () => loadWords(level));
    }
});
