from transformers import pipeline 

unmasker = pipeline("fill-mask", model='bert-large-cased', top_k=50)
res = unmasker('John [MASK] Mary the ball.')

print(res)

# from transformers import BertTokenizer, BertForMaskedLM
# import torch

# tokenizer = BertTokenizer.from_pretrained('bert-large-uncased')
# model = BertForMaskedLM.from_pretrained('bert-large-uncased')

# inputs = tokenizer("The capital of France is [MASK].", return_tensors="pt")
# labels = tokenizer("The capital of France is Paris.", return_tensors="pt")["input_ids"]

# outputs = model(**inputs, labels=labels)
# loss = outputs.loss
# logits = outputs.logits
