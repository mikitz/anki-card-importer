# Anki-Helper-Bot
## Description
This Python notebook does:
    Study Method:
        * It reads a TXT file to determine whether I do listening or reading for the day and then writes to the same TXT file that day's activity.
        * It scans the databases of all languages and pulls new words that were inserted into the DBs 14 days ago.
            * I then write sentences using these words.
    For Anki:
        * It takes the input of words from a user-defined language within Flashcards.xlsx.
        * Next, it uses those words and that defined language to determine what website to scrape.
        * After than, it scrapes sentences from the appropriate website, then saves them to an XLSX file.
        * It uses the words found in Flashcards.xlsx to create two types of notes within Anki: a custom front-back type note and a custom cloze type note.
        * Finally, it imports these newly created cards into the local instance of Anki using the AnkiConnect add-on. (https://github.com/FooSoft/anki-connect)
  
