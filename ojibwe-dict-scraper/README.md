# Ojibwe Dictionary Web Scraper
> I wrote the following script to gather words and parts of speech from the Ojibwe People's Dictionary. The script also has an algorithm to combine words and parts of speech into urls to that can be used to gather additional data, such as definitions and conjugated verb forms.


## General Information

The purpose of this project is to gather words, definitions, and parts of speech of the Ojibwe language. The script then concatenates words and grammar parts into urls and loops through this list to collect definitions. The final product is a .csv file that contains 19,876 entries after null values have been filtered out ('ojibwe-dict.csv'). This project adapts a reference dictionary into a dataset.

Although the Ojibwe People's Dictionary is an excellent reference resource, the contents do not provide students with automated study tools. This leaves students to study using long-form pen and paper. With the assistance of a grammar guide, this dataset is used to develop and test algorithms to scale up the dictionary by conjugating verb forms (conjunct, conjuct changed, imperative; past, present, and future tense) and noun forms (plural, obviate, diminutive, contemplative, locative, possessive, and pejorative forms). The resulting dictionary modifications serve as a platform upon which other applications -- such as flashcard decks and conjugation tools -- can be created according to themed lesson plans or modules. Such applications are intended to support language revitalization, create automated tools to enhance language study, and increase student confidence as they develop their language skills.

I began writing this script to develop skills learned in a recent data analytics boot camp. During this course I became interested in the field of Natural Language Processing (NLP) and wanted to explore how programs such as Chat GPT function on a basic level. I chose Ojibwe for the following reasons: the writing system uses the Roman alphabet without accents or special characters, the language has wide availability of source texts from which to build a corpus, and revitalization efforts currently underway in communities and at universities across the Great Lakes Region are numerous. I recognize that gathering, cleaning, and structuring this dataset is essential to developing Large Language Models and other NLP techniques. This script is a simple, first step on that journey.

I am passionate about this project because I grew up in Michigan and my favorite places to visit derive their names from Ojibwe words and legends. I feel that learning how to build applications and write algorithms is an excellent way to develop professional skills while encouraging my life-long curiosity with languages.


## Technologies Used
- Python           : 3.9.12


## Setup
This script will run as a Jupyter Notebook as long as 'ojibwe-dict-scraper.ipynb' and 'browsers.py' share the same file path. The script can also be copied and pasted into a text editor and saved as 'ojibwe-dict-scraper.py' to run as a regular Python file.


## Project Status
Project is: No longer being worked on. Although there is always room for improvement, I don't want perfect to be the enemy of sufficient.


## Room for Improvement

Room for improvement:

I have included a copy of the dataset without errors filtered out ('ojibwe-dict-improve.csv') to help identify areas of improvement. The unfiltered dataset yields 20,692 entries. The project can be improved by editing the code to collect the 816 missing entries (or as many as possible).  Some areas of improvement include:

- The eqaul sign (=) at the beginning of a word is not taken into account when creating urls. For example, the csv does not yet capture 'friend' in all its forms:
	- =iijikiwenh nad STEM FOR: (male's) brother
	- =iijikwe nad someone's (female's) female friend
	- =iikaan nad someone's (male's) brother; someone's (male's) male friend
	- =iikaanis nad someone's (male's) brother; someone's (male's) male friend
- Some urls are not structured using a word + - + part of speech format; the script could be modified to re-run urls that only contain the scraped word.
- Some urls lack a hyphen between words with spaces; the script could be modified to ensure that hypthens are placed between both words and grammar parts that contain spaces.


## Acknowledgements

Data gathered using this script are copyrighted by The Ojibwe People's Dictionary, which can be accessed through the following link: http://ojibwe.lib.umn.edu

Please note the following:
- I am not in any way affiliated with The Ojibwe People's Dictionary.
- The script provided in this repositoy does not in any way that suggest that the The Ojibwe People's Dictionary endorses myself or my use of the data provided by the dictionary.
- The script is provided in the spirit of The Ojibwe People's Dictionary's goal to make the dictionary content available as a tool for Ojibwe language revitalization, academic scholarship and cultural awareness. Neither the data in the Ojibwe People's Dictionary nor this code are to be used for commercial purposes.


## Contact
Created by tyler.coding.projects@gmail.com - feel free to contact me!
