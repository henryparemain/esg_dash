
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd


# def create_list_of_google_searches(string_of_sentences: list(str)) -> list(str):
#     """
#     used to create a bunch of phrases that can be searched in a news api thing and retrieve headlines relevant to the 
#     company and content of the report and the sasb metric in question.
#     """



#     # Tokenize and remove stopwords
#     stop_words = set(stopwords.words("english"))
#     tokenized_words = [word for sentence in sentences for word in word_tokenize(sentence.lower()) if word.isalpha() and word not in stop_words]

#     # Calculate word frequencies
#     freq_dist = FreqDist(tokenized_words)

#     # Extract top keywords
#     top_keywords = [word for word, freq in freq_dist.most_common(10)]

#     # Combine keywords to create search phrases
#     search_phrases = [' '.join(top_keywords[i:i+2]) for i in range(0, len(top_keywords), 2)]

#     return search_phrases




def find_number_of_pages(company_name):
    response = requests.get(f'https://www.esgtoday.com/page/1/?s={company_name}', headers=headers)  
    soup = BeautifulSoup(response.text, 'html.parser')
    res = soup.find_all(class_='number')
    numbers = []
    for i in res:
        numbers.append(int(i.get_text()))
    return max(numbers)
  

def obtain_article_urls(number_of_pages,company_name):
    hrefs = []
    dates = []
    for i in list(range(1,number_of_pages+1)):
        response = requests.get(f'https://www.esgtoday.com/page/{i}/?s={company_name}', headers=headers)  
        soup = BeautifulSoup(response.text, 'html.parser')
        main_section = soup.find('main', class_='tf_clearfix')

        article_divs = main_section.find_all(class_="post-title entry-title")
        time_stamps = main_section.find_all('time')

        for div in article_divs:
            anchor_tag = div.find('a')  # Find the anchor tag within the div
            if anchor_tag:
                hrefs.append(anchor_tag.get('href'))
        
        for time in time_stamps:
            datetime_string = time['datetime']  # Get the value of the 'datetime' attribute
            # formatted_datetime = datetime.strptime(datetime_string, "%Y-%m-%d")
            dates.append(datetime_string)

    return hrefs, dates

def create_list_of_dictionaries_with_url_and_date(dates,urls):
    dic = {}
    list_of_dics = []

    for date, url in zip(dates,urls):
        dic = {}
        # print(date,url)
        dic['url']=url
        dic['date'] =date
        list_of_dics.append(dic)

    return list_of_dics

def create_para_data_dataframe(list_of_dics):
    para_date_dic = {}
    list_of_para_date_dics = []
    for dic in list_of_dics:
        url = dic['url']
        date = dic['date']
        article_body = fetch_article_text(url)
        for para in article_body:
            if 'Honeywell' in para or 'honeywell' in para:
                para_date_dic = {
                    'para':para,
                    'date':date
                }
                list_of_para_date_dics.append(para_date_dic)
    df = pd.DataFrame.from_dict(list_of_para_date_dics)
    return df

def fetch_article_text(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)  
    soup = BeautifulSoup(response.text, 'html.parser')
    main_section = soup.find('div', class_='entry-content')
    # Find all <p> tags within the article content
    paragraph_tags = main_section.find_all('p')
    article_text = [p.get_text().strip() for p in paragraph_tags]
    return article_text



def main(company_name):
    company_name = company_name.lower()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    number_of_pages = find_number_of_pages(company_name)
    urls,dates = obtain_article_urls(number_of_pages,company_name)
    list_of_dics = create_list_of_dictionaries_with_url_and_date(dates,urls)
    df = create_para_data_dataframe(list_of_dics)
    return df


