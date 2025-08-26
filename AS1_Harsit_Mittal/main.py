from huggingface_hub import InferenceClient
from datasets import load_dataset
import os

# Pick 10 examples from the dataset zeroshot/twitter-financial-news-topic
finance_dataset = load_dataset('zeroshot/twitter-financial-news-topic', split='train')
finance_dataset = finance_dataset.shuffle(seed=42).select(range(10))


# Grab the token you exported
HF_TOKEN = os.getenv('HF_TOKEN')
if not HF_TOKEN:
    raise ValueError('Please set your HF_TOKEN as environment variable')


# Set client to Gemma model (270 million parameters)
client = InferenceClient('meta-llama/Llama-3.1-8B-Instruct', token=HF_TOKEN)


# Define the system prompt
system_prompt = (
    """
    You are a highly knowledgable financial assistant. 
    When given a tweet by the user, you will classify the tweet by one of these categories:
    
    categories = [
        "Analyst Update",
        "Fed | Central Banks",
        "Company | Product News",
        "Treasuries | Corporate Debt",
        "Dividend",
        "Earnings",
        "Energy | Oil",
        "Financials",
        "Currencies",
        "General News | Opinion",
        "Gold | Metals | Materials",
        "IPO",
        "Legal | Regulation",
        "M&A | Investments",
        "Macro",
        "Markets",
        "Politics",
        "Personnel Change",
        "Stock Commentary",
        "Stock Movement",
    ].
    
    When giving your classification, give it in this format: category (category_index). For example, Analyst Update (0) or IPO (11). Add nothing else.
    
    If the tweet is not finance related, politely tell them that their topic is out of your scope.    
    """
)


# Loop through each tweet from dataset and get an AI-generated classification
for dataset_item in finance_dataset:
    tweet = dataset_item['text']
    user_prompt = f'Classify this tweet: {tweet}'
    
    response = client.chat_completion(
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ],
        max_tokens=100
    )
    
    print(f'Tweet: {tweet}')
    print(f'Model response: {response.choices[0].message['content']}')
    print('-' * 20)
    print('')