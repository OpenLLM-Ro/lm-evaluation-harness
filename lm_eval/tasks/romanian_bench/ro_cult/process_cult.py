import sys

def doc_to_text(doc):
    choices = [doc["option_a"], doc["option_b"], doc["option_c"], doc["option_d"]]
    
    string = "Întrebare: {0}\nVariante:\n".format(doc["question"])
    for i, choice in enumerate(choices):
        string += "{1}. {0}\n".format(choice, str(chr(97 + i)).upper())
    # string = string[:-1]
    string = string + "\n"
    string += "Răspunde direct cu litera opțiunii alese.\nRăspuns: "
    return string

def doc_to_choice(doc): 
    return ["A", "B", "C", "D"]

def doc_to_target(doc):
    return doc["answer"]    

