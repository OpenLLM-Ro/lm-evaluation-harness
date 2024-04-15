import sys

def doc_to_choice(doc): 
    choices = [doc["option_A"], doc["option_B"]]

    if doc["option_C"] != None:
        choices.append(doc["option_C"])
    if doc["option_D"] != None:
        choices.append(doc["option_D"])
    if doc["option_E"] != None:
        choices.append(doc["option_E"])
    if doc["option_F"] != None:
        choices.append(doc["option_F"])
    if doc["option_G"] != None:
        choices.append(doc["option_G"])

    return choices      

def doc_to_target(doc):
    print(doc)
    return chr(ord("A")+doc["answer"])

def doc_to_text(doc):
    choices = [doc["option_A"], doc["option_B"]]
    if doc["option_C"] != None:
        choices.append(doc["option_C"])
    if doc["option_D"] != None:
        choices.append(doc["option_D"])
    if doc["option_E"] != None:
        choices.append(doc["option_E"])
    if doc["option_F"] != None:
        choices.append(doc["option_F"])
    if doc["option_G"] != None:
        choices.append(doc["option_G"])


    string = "Întrebare: {0}\nVariante:\n".format(doc["question"])
    for i, choice in enumerate(choices):
        string += "{0}. {1}\n".format(chr(ord("A")+i), choice)
    string += "Răspuns:"
    return string
