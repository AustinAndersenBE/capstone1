//Javascript to handle the client side check to see if the sentence contains the vocab

document.getElementById('sentenceForm').addEventListener('submit', function(event) {
    let sentence = document.getElementById('sentence').value.toLowerCase();
    sentence = sentence.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,""); // this is to remove punctuation

    let inputVocabWords = document.getElementById('vocab_words').value.toLowerCase().split(',');
    inputVocabWords = inputVocabWords.map(word => word.trim());

    function checkVocabWords(vocabWords) {
        let missingInSentence = inputVocabWords.filter(word => !sentence.includes(word));
        let missingInVocab = inputVocabWords.filter(word => !vocabWords.includes(word));

        if (missingInSentence.length > 0) {
            alert('All vocab words must be in the sentence.');
            event.preventDefault();
            return;
        }

        if (missingInVocab.length > 0) {
            alert('All vocab words must be in the vocab words database.');
            event.preventDefault();
            return;
        }
    }

    try {
        // Attempt to get vocab words from local storage
        const cachedVocabWords = localStorage.getItem('vocabWords');
        if (cachedVocabWords) {
            checkVocabWords(JSON.parse(cachedVocabWords));
        } else {
            fetch('/api/vocab_words')
                .then(response => response.json())
                .then(vocabWords => {
                    try {
                        localStorage.setItem('vocabWords', JSON.stringify(vocabWords));
                    } catch (error) {
                        console.error("Error has occured:", error);
                        // Handle local storage limit exceeded error
                    }
                    checkVocabWords(vocabWords);
                }).catch(error => {
                    console.error("Error has occured", error);
                    // Handle network error
                });
        }
    } catch (error) {
        console.error("Error has occured", error);
    }
});
