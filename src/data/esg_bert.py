from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd

tokenizer = AutoTokenizer.from_pretrained("nbroad/ESG-BERT")

model = AutoModelForSequenceClassification.from_pretrained("nbroad/ESG-BERT")

#list of 26 ESG metrics which ESGBert can classify a text into. 
topic_list = ['Business_Ethics',
 'Data_Security',
 'Access_And_Affordability',
 'Business_Model_Resilience',
 'Competitive_Behavior',
 'Critical_Incident_Risk_Management',
 'Customer_Welfare',
 'Director_Removal',
 'Employee_Engagement_Inclusion_And_Diversity',
 'Employee_Health_And_Safety',
 'Human_Rights_And_Community_Relations',
 'Labor_Practices',
 'Management_Of_Legal_And_Regulatory_Framework',
 'Physical_Impacts_Of_Climate_Change',
 'Product_Quality_And_Safety',
 'Product_Design_And_Lifecycle_Management',
 'Selling_Practices_And_Product_Labeling',
 'Supply_Chain_Management',
 'Systemic_Risk_Management',
 'Waste_And_Hazardous_Materials_Management',
 'Water_And_Wastewater_Management',
 'Air_Quality',
 'Customer_Privacy',
 'Ecological_Impacts',
 'Energy_Management',
 'GHG_Emissions']

def score_sentences(list_of_sentences: list) -> dict:
    # the below dictionary is the outer one, where the keys are the sentences, and the values are the inner dictionary (nested)
    topic_probs_outer_dict = {}
    for sentence in list_of_sentences:
        topic_probs_dictionary = {}
        # Get topic probabilities for each document
        encoded_docs = tokenizer.batch_encode_plus([sentence], padding=True, truncation=True, return_tensors='pt')
        outputs = model(encoded_docs['input_ids'], attention_mask=encoded_docs['attention_mask'])
        probs = outputs[0].softmax(dim=1)
        probability_list = list(probs[0].detach().numpy())
        for topic, probability in zip(topic_list, probability_list):
            topic_probs_dictionary[topic] = probability
            topic_probs_outer_dict[sentence] = topic_probs_dictionary
    return topic_probs_outer_dict



def score_sentences_put_in_df(list_of_sentences: list) -> pd.DataFrame:
    topic_probs_dict = score_sentences(list_of_sentences)
    df = pd.DataFrame.from_dict(topic_probs_dict,  orient = 'index').reset_index().rename(columns={'index':'sentence'})
    return df
