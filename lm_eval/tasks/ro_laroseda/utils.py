import datasets
import evaluate
def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
        doc["rating"] = "pozitivă" if doc["starRating"] > 3 else "negativă" 
        return doc

    return dataset.map(_helper) # returns back a datasets.Dataset object

def doc_to_target_bc(doc):
    if doc["rating"] == "pozitivă":
        return 1
    return 0

def doc_to_target_mc(doc):
    return [1, 2, 4, 5].index(doc["starRating"])

def micro_f1_score(items):
    f1_metric = evaluate.load("f1")
    golds, preds = list(zip(*items))
    f1_score = f1_metric.compute(references=golds, predictions=preds, average="micro")[
        "f1"
    ]
    return f1_score

def weighted_f1_score(items):
    f1_metric = evaluate.load("f1")
    golds, preds = list(zip(*items))
    f1_score = f1_metric.compute(references=golds, predictions=preds, average="weighed")[
        "f1"
    ]
    return f1_score