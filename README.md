# Polish Verb Wizard

**Simplify Polish Verb Classification and Conjugation Learning**

## 📖 Introduction

Are you learning Polish and struggling with the complexities of verb aspects and conjugations? **Polish Verb Wizard** is here to help! This simple program automates the classification of Polish verbs and assists you in understanding their conjugation patterns, making your language learning journey smoother and more efficient.

## 🚀 Features

**Three files are generated from the verb list that the user provides**

1. **Verb Classification**

   - **Automatic Analysis**: Upload a file containing a list of Polish verbs in infinitive, and the program will analyze each one.
   - **Detailed Categorization**: Generates a `1_verb_simple.txt` file where verbs are sorted into four categories:
     - **Imperfective**
     - **Perfective**
     - **Both** (verbs that can be both imperfective and perfective)
     - **Unrecognized** (verbs that couldn't be classified)

2. **Conjugation Patterns Learning**
   
   - **Conjugation Details**: The program will as well generate a `2_verb_conjugation.txt` which contains the same list as the first file but this one includes conjugation information.
   - **Enhanced Learning**: Outputs the first and third person singular forms in the present tense. This information helps learners identify the conjugation group of each verb and their patterns.

3. **Speed Up Flashcard Creation**
   
   - **SCSV File**: Lastly, a third file called `3_verb_SCSV.txt` will be also generated in a SCSV format.
   - **Streamlined Flashcard Creation** With this last file, you will be able to import the data to your favorite flashcard app easily.

## 🛠 Installation

First, install the necessary dependencies:

```bash
pip install morfeusz2
```
Second, proceed to execute:
```bash
python main.py
```
