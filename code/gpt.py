import openai
import pandas as pd
from secret_key import OPENAI_API_KEY

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
    
def gpt_function(OPENAI_API_KEY, prompt):
    openai.api_type = "azure"
    openai.api_key = OPENAI_API_KEY
    openai.api_base =  "https://api.hku.hk"
    openai.api_version = "2023-03-15-preview"
    
    # create a completion
    # engine= chatgpt-3.5 | chatgpt-4
    prompt = open_file(filepath)
    completion = openai.ChatCompletion.create(engine="chatgpt-4", 
                                            messages=[{"role": "user", "content": prompt}])

    # print the completion
    print(completion.choices[0].message.content)
    
    
if __name__ == '__main__':
    filepath = '../data/'
    df = pd.read_excel('../data/sentiment_analysis_latest.xlsx')
    prompt1 = 'Is the sentiment of this Cantonese text positive, neutral, or negative? Respond with the sentiment label only:'
    for i in df['sentiment_label']:
        prompt = prompt1 + i
        gpt_function(OPENAI_API_KEY, prompt)