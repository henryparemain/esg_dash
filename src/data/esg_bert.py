

from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("nbroad/ESG-BERT")

model = AutoModelForSequenceClassification.from_pretrained("nbroad/ESG-BERT")

def score_sentences(list_of_sentences: list(str)) -> dict:
    for sentence in list_of_sentences:
        # Get topic probabilities for each document
        encoded_docs = tokenizer.batch_encode_plus(sentence, padding=True, truncation=True, return_tensors='pt')
        outputs = model(encoded_docs['input_ids'], attention_mask=encoded_docs['attention_mask'])
        probs = outputs[0].softmax(dim=1)
        probability_list = list(probs[0].detach().numpy())
        probability_dictionary = 