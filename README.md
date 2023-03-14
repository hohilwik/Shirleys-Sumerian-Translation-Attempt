# Shirley's Sumerian Translation Attempt
The Sumerian Translation Attempt: to collate all existing corpuses and train a model sufficiently competent at Sumerian-English translation. 

# Changelog

## 002
- CDLI data is not cleaned properly. Need to write a custom parser that can deal with that. Will also attempt the suggested method using APIs
- collating grammar notes for rule-based translation based on books in Readings folder
- The lack of consistency in hyphenating words in transliterations is going to present a problem

# Datasets
- ETCSL: 36003 Sumerian-English sentence pairs
- CDLI: 112612 tablets, 1.4 million lines

# Pipeline

## Parsing

- Parse through CDLI and ETCSL datasets, create dataset with Sumerian-English sentence pairs
- small parsing issue and the Sumerian is given line by line, whereas the translation is for blocks of lines, (eg, 1-4, 4-7, etc)

## Text Analysis

- Extract stop-words list
- Extract list of Sumerian-English phrases that appear simultaneously
- Extract n-gram lists for various values of n to help with phrase-based translation later, keep phrase-wise lists of which document and which line they appear in
- Construct a dictionary from the given labels (note: different words sometimes translate to the same English but have different nuances in Sumerian)
- Construct network graphs for sentence pairs to help with rule-based grammar parsing later

## Evaluation Metric

- academics have taken liberty with the translation over the years, for example, translating poetry with repeated use of "pure" with several different synonyms in the package (this is common with Russian literature translations too, seems to be an English translator thing)
- therefore I need an evaluation metric other than docdist as training any model with several synonyms will confuse it
- plan to use Stanford's GloVe as everything involved in this part will be in English anyway

## Model Training

- first do simple dictionary-based translation and get a baseline for accuracy
- Iterate through all the N-gram lists and phrase lists, line-wise, replacing the phrase in the translation, and mark the delta in accuracy
- Anything over a certain threshold of improved accuracy gets marked as a relevant phrase
- Several common phrases like [gu3 mu-na-de2-e]"poured voice" being translated to "said", [kug]"shining" -> "Holy" should get caught in this
- Go through the sentence network graphs for Sumerian and English, and construct grammar rules for translation
- 

