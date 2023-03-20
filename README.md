# Shirley's Sumerian Translation Attempt
The Sumerian Translation Attempt: to collate all existing corpuses and train a model sufficiently competent at Sumerian-English translation. 

# Note on Readings of Grammar and Morphology

- As I attempt rule-based parsing and translation of Sumerian before doing anything even related to word embeddings or other standard MT-NLP techniques, it is important to understand the grammar and morphology of Sumerian. 
- My initial reference here is Foxvog's "Introduction To Sumerian Grammar", and Zolyomi's book of nearly the same name, as a starting point for parsing most simple sentences. Especially with the Russian-doll-like syntactic structure of noun phrases, which makes the translation of certain types of sentences almost trivial with the same techniques that are used in compilers. It provides a good balance between coverage of edge cases, and broad understanding of the language structure.
- Reference for more detailed understanding is "Manual of Sumerian Grammar and Texts" by John L Hayes, which I understand to be quite thorough and practical for understanding Sumerian grammar for the purposes of translation. Since it uses mostly real Ur III examples for demonstrating grammar rules, the step-by-step translation and additional commentary is a very good source of information specifically for understanding the grammatical rules of the same era as the corpus. It should also help in quickly refining the rules constructed when reading through the introduction
- Bram Jagersma's "A Descriptive Grammar of Sumerian" as a final boss for refining the grammar rules understood so far. It has everything: nouns, noun phrases, cases, pronouns, numerals, to various forms of prefixes, suffixes, copula, verb forms, nominal clauses, and a vast arsenal of phonological analysis.

# Shortcomings of Previous Approaches

- will elaborate soon


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
- while phrase lists and sign lists exist, they are not complete, and often not digitally available. However, several transliterations include the direct translation of most nouns within the XML tags, which should prove useful for constructing a dictionary. More data analysis on the words used in the corpus needs to be done.
- Iterate through all the N-gram lists and phrase lists, line-wise, replacing the phrase in the translation, and mark the delta in accuracy
- Anything over a certain threshold of improved accuracy gets marked as a relevant phrase
- Several common phrases like [gu3 mu-na-de2-e]"poured voice" being translated to "said", [kug]"shining" -> "Holy" should get caught in this
- Grammar-based direct translation comes here. Need more analysis of the corpus to find out the distribution of the complexity of sentences, and see if constructing a grammar-based rulebook is possible. Foxvog's texts give me hope.
- Go through the sentence network graphs for Sumerian and English, and construct grammar rules for translation
- Given that Sumerian is a very low-resource language, it would be more reasonable[compared to word embeddings or Sumerian-English transformers based on other languages, since Sumerian is a language isolate] to parse and translate the words(after suffix/prefix parsing) to English in a particular format, and finetune a transformer to rearrange the words in a more understandable and correct sentence for the English reader

