import sys

def doc_to_text_foundational_with_options(doc):
    choices = [doc["option_a"], doc["option_b"], doc["option_c"], doc["option_d"]]
    if doc["option_e"] != None:
        choices.append(doc["option_e"])

    string = "Întrebare: {0}\nVariante:\n".format(doc["instruction"])
    for i, choice in enumerate(choices):
        string += "- {0}\n".format(choice)
    # string = string[:-1]
    string += "Răspuns: [/INST]"
    return string

# [INST] <<SYS>>
# Ești un asistent care răspunde la întrebări cu variante de răspuns. Alege răspunsul corect din variantele disponibile.
# <</SYS>>

# Întrebare: Rosaria a descoperit un tip de structură pe care nu a putut-o identifica într-o probă de apă dintr-un iaz. Profesoara ei s-a uitat în microscop și i-a explicat că erau zigote produse de unul dintre protiștii din proba ei. La care protist aparțin zigotii?
# Variante:
# - ameba
# - euglena
# - paramecium
# - volvox
# Răspuns: [/INST] volvox


def doc_to_text_chat(doc):
    return "[INST] {0} [/INST]".format(doc["instruction"])

def doc_to_choice(doc): 
    choices = [doc["option_a"], doc["option_b"], doc["option_c"]]#, doc["option_d"]]

    if doc["option_d"] != None:
        choices.append(doc["option_d"])
    if doc["option_e"] != None:
        choices.append(doc["option_e"])

    return choices      

def doc_to_target(doc):
    return doc["option_{0}".format(doc["answer"].lower())]
    