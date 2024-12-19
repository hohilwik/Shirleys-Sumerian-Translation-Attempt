import os
import re
import xml.etree.ElementTree as ET
from collections import defaultdict

def sanitize_xml(xml_content):
    """
    Replace undefined XML entities with valid placeholders.
    """
    # Replace entities like &d; and &X; with placeholders
    return re.sub(r'&([a-zA-Z0-9]+);', r'__\1__', xml_content)

def extract_lemmas_and_labels(xml_file):
    """
    Extract lemmas and labels from a single XML file.
    """
    # Read the XML content and sanitize it
    with open(xml_file, 'r', encoding='utf-8') as file:
        xml_content = file.read()
    sanitized_content = sanitize_xml(xml_content)

    # Parse the sanitized XML
    tree = ET.ElementTree(ET.fromstring(sanitized_content))
    root = tree.getroot()

    lemma_dict = {}
    for word in root.findall('.//w'):
        lemma = word.get('lemma')
        label = word.get('label')
        if lemma and label:
            if lemma not in lemma_dict:
                lemma_dict[lemma] = set()
            lemma_dict[lemma].add(label)

    # Convert sets to lists for JSON compatibility
    return {lemma: list(labels) for lemma, labels in lemma_dict.items()}



def merge_dictionaries(dict1, dict2):

    #Merges two dictionaries, combining values of common keys.
    #
    #Args:
    #    dict1 (dict): The first dictionary.
    #    dict2 (dict): The second dictionary.
    #
    #Returns:
    #    dict: The merged dictionary.

    for key, value in dict2.items():
        dict1[key].update(value)
    return dict1

def build_lemma_dictionary_from_folder(folder_path):
    """
    Builds a lemma-to-English dictionary from all XML files in a folder.

    Args:
        folder_path (str): Path to the folder containing XML files.

    Returns:
        dict: A dictionary mapping lemmas to their English translations.
    """
    final_dict = defaultdict(set)

    # Iterate over all XML files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".xml"):
            print(file_name)
            xml_path = os.path.join(folder_path, file_name)
            file_dict = extract_lemmas_and_labels(xml_path)
            final_dict = merge_dictionaries(final_dict, file_dict)

    # Convert sets to lists for easier output or storage
    return {key: list(values) for key, values in final_dict.items()}

if __name__ == "__main__":
    current_dir = os.getcwd()
    # Get the parent directory
    parent_dir = os.path.dirname(current_dir)
    print(parent_dir)
    # Specify the folder containing the XML files
    folder = parent_dir+"/datasets/etcsl/transliterations"

    # Build the dictionary
    lemma_dict = build_lemma_dictionary_from_folder(folder)

    # Save the dictionary to a JSON file for later use
    import json
    with open("sumerian_lemma_dict.json", "w", encoding="utf-8") as json_file:
        json.dump(lemma_dict, json_file, ensure_ascii=False, indent=4)

    print("Dictionary built and saved as sumerian_lemma_dict.json")
