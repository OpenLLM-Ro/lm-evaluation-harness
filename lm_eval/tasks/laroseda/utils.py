import datasets
def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
        doc["rating"] = "positive" if doc["starRating"] > 3 else "negative" 
        return doc

    return dataset.map(_helper) # returns back a datasets.Dataset object