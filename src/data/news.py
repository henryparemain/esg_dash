
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def create_list_of_google_searches(string_of_sentences: list(str)) -> list(str):
    """
    used to create a bunch of phrases that can be searched in a news api thing and retrieve headlines relevant to the 
    company and content of the report and the sasb metric in question.
    """



    # Tokenize and remove stopwords
    stop_words = set(stopwords.words("english"))
    tokenized_words = [word for sentence in sentences for word in word_tokenize(sentence.lower()) if word.isalpha() and word not in stop_words]

    # Calculate word frequencies
    freq_dist = FreqDist(tokenized_words)

    # Extract top keywords
    top_keywords = [word for word, freq in freq_dist.most_common(10)]

    # Combine keywords to create search phrases
    search_phrases = [' '.join(top_keywords[i:i+2]) for i in range(0, len(top_keywords), 2)]

    return search_phrases

