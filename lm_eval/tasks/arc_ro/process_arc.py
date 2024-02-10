import sys

def doc_to_text_foundational_with_options(doc):
    choices = [doc["option_a"], doc["option_b"], doc["option_c"], doc["option_d"]]
    if doc["option_e"] != None:
        choices.append(doc["option_e"])

    string = "Întrebare: {0}\nVariante:\n".format(doc["instruction"])
    for i, choice in enumerate(choices):
        string += "- {0}\n".format(choice)
    # string = string[:-1]
    string += "Răspuns:"
    return string

def doc_to_text_chat(doc):
    return "[INST] {0} [/INST]".format(doc["instruction"])

def doc_to_choice(doc): 
    choices = [doc["option_a"], doc["option_b"], doc["option_c"], doc["option_d"]]
    if doc["option_e"] != None:
        choices.append(doc["option_e"])
    return choices      

def doc_to_target(doc):
    return doc["option_{0}".format(doc["answer"].lower())]
    