from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from google.api_core.exceptions import ResourceExhausted
import random
import pandas as pd
import time
import json
import re

def sentiment_model(chat_history):
    api_keys = [
        "AIzaSyA2Zxvvgy1qbYADGni4QCmC4pA7ZTIIU-c",
        "AIzaSyDSgcHg94NTkjSeIwptOssRV7UWi58HreE",
        "AIzaSyBPifh4rqyEeDiHYwbPqEdLQtowJbVsHlY",
        "AIzaSyA270F6pxFKngmrCag9F0ecFwKiyi5GAN4",
        "AIzaSyCxs-HliBGec0HKZb6AxqTPHDNUpGutbPs",
        "AIzaSyAC72Z3Ctvg1Ku-IgRCPE2Cwbc_HD37ejM",
        "AIzaSyD6AFY37W-CyUByFaXI4wqLWxmq6QH90dk",
        "AIzaSyAHxw57s8PmjFtlphi9SjbnhA71vXWRG9o",
        "AIzaSyBUmDlertCkmbEBnts3d1g2wm0FDPHbWwE",
        "AIzaSyDNDwZW4ldyDTbAxrZlnhg8qHwrjcKoNnA"
    ]

    sentiment_prompt = PromptTemplate(
        template="""
        Analyze the following conversation and determine the sentiment. Output whether it is "positive", "negative", or "neutral",
        along with the degree of sentiment on a scale from 1 to 5 (for positive), -1 to -5 (for negative), or 0 (for neutral). 
        CAUTION!! customers often use the Egyptian Arabic. Please take care 

        Chat:
        {chat}

        Output format:
        {{ "type": [positive/negative/neutral], "degree": [1-5/-1 to -5/0] }}
        make sure to output this format only without any explaination or additional words. don"t mention the word "json" in any result
                
        """
    )

    model_name = "gemini-1.5-flash"
    random_api_key = random.choice(api_keys)  # Randomly choose an API key from the list

    # Instantiate the LLM and the chain
    llm = ChatGoogleGenerativeAI(api_key=random_api_key, model=model_name, temperature=0.1)
    sentiment_chain = LLMChain(llm=llm, prompt=sentiment_prompt)
    
    # Attempt the sentiment analysis with retries
    retry_attempts = 3
    for attempt in range(retry_attempts):
        try:
            result = sentiment_chain.run(chat=chat_history, verbose=False)
            # Parse the result directly
            sentiment_data = json.loads(result)
            return sentiment_data["type"], sentiment_data["degree"]
        except (ResourceExhausted, json.JSONDecodeError) as e:
            if attempt < retry_attempts - 1:
                print(f"Resource exhausted or JSON parse error. Retrying... ({attempt + 1}/{retry_attempts})")
                time.sleep(5)  # Wait before retrying
            else:
                print(f"Failed after {retry_attempts} attempts. Skipping this chat.")
                return "Error", 0
            
def classification_model(chat_history, classes):
    print(chat_history, classes)
    api_keys = {"AIzaSyA2Zxvvgy1qbYADGni4QCmC4pA7ZTIIU-c",
                "AIzaSyDSgcHg94NTkjSeIwptOssRV7UWi58HreE",
                "AIzaSyBPifh4rqyEeDiHYwbPqEdLQtowJbVsHlY",
                "AIzaSyA270F6pxFKngmrCag9F0ecFwKiyi5GAN4",
                "AIzaSyCxs-HliBGec0HKZb6AxqTPHDNUpGutbPs",

                "AIzaSyAC72Z3Ctvg1Ku-IgRCPE2Cwbc_HD37ejM",
                "AIzaSyD6AFY37W-CyUByFaXI4wqLWxmq6QH90dk",
                "AIzaSyAHxw57s8PmjFtlphi9SjbnhA71vXWRG9o",
                "AIzaSyBUmDlertCkmbEBnts3d1g2wm0FDPHbWwE",
                "AIzaSyDNDwZW4ldyDTbAxrZlnhg8qHwrjcKoNnA"}
    classification_prompt = PromptTemplate(
    template="""
                Analyze the following conversation and determine which class it belongs to. Choose from the given options.

                Available Classes: {classes}

                Conversation:
                {chat}

                Output the class as one word only.

                example :
                chat:
                Customer: Hi Can i ask something?
                Admin: Hello How can i help you today?
                customer : can you help me i can"t login to my account?
                Admin:sure i can help you .

                the output will be one of the available classes

                make sure to output the class only in one word and in one line without any explaination or special chars.
                """ 
                )
    model_name = "gemini-1.5-flash"
    random_api_key = random.choice(list(api_keys))
    llm = ChatGoogleGenerativeAI(api_key=random_api_key, model=model_name, temperature=0.1)
    classification_chain = LLMChain(llm=llm, prompt=classification_prompt)
    classification_result = classification_chain.run(chat=chat_history, classes=classes, verbose=False)
    print(classification_result)
    return classification_result

def summary_model(chat):
    api_keys = {"AIzaSyA2Zxvvgy1qbYADGni4QCmC4pA7ZTIIU-c",
            "AIzaSyDSgcHg94NTkjSeIwptOssRV7UWi58HreE",
            "AIzaSyBPifh4rqyEeDiHYwbPqEdLQtowJbVsHlY",
            "AIzaSyA270F6pxFKngmrCag9F0ecFwKiyi5GAN4",
            "AIzaSyCxs-HliBGec0HKZb6AxqTPHDNUpGutbPs",

            "AIzaSyAC72Z3Ctvg1Ku-IgRCPE2Cwbc_HD37ejM",
            "AIzaSyD6AFY37W-CyUByFaXI4wqLWxmq6QH90dk",
            "AIzaSyAHxw57s8PmjFtlphi9SjbnhA71vXWRG9o",
            "AIzaSyBUmDlertCkmbEBnts3d1g2wm0FDPHbWwE",
            "AIzaSyDNDwZW4ldyDTbAxrZlnhg8qHwrjcKoNnA"}
    random_api_key = random.choice(list(api_keys))
    model_name = "gemini-1.5-flash"
    llm = ChatGoogleGenerativeAI(api_key=random_api_key, model=model_name)
    summary_prompt = PromptTemplate(
        input_variables=["chat"],
        template="""
        Provide a clear and easy to understand , summary of the following chat in no more than 50 words:

        Chat:
        {chat}
        """
    )
    summary_chain = LLMChain(llm=llm, prompt=summary_prompt)
    summary_result = summary_chain.run(chat=chat)
    return summary_result
        
def label_model(chat):
    api_keys = {"AIzaSyA2Zxvvgy1qbYADGni4QCmC4pA7ZTIIU-c",
            "AIzaSyDSgcHg94NTkjSeIwptOssRV7UWi58HreE",
            "AIzaSyBPifh4rqyEeDiHYwbPqEdLQtowJbVsHlY",
            "AIzaSyA270F6pxFKngmrCag9F0ecFwKiyi5GAN4",
            "AIzaSyCxs-HliBGec0HKZb6AxqTPHDNUpGutbPs",

            "AIzaSyAC72Z3Ctvg1Ku-IgRCPE2Cwbc_HD37ejM",
            "AIzaSyD6AFY37W-CyUByFaXI4wqLWxmq6QH90dk",
            "AIzaSyAHxw57s8PmjFtlphi9SjbnhA71vXWRG9o",
            "AIzaSyBUmDlertCkmbEBnts3d1g2wm0FDPHbWwE",
            "AIzaSyDNDwZW4ldyDTbAxrZlnhg8qHwrjcKoNnA"}
    random_api_key = random.choice(list(api_keys))
    model_name = "gemini-1.5-flash"
    llm = ChatGoogleGenerativeAI(api_key=random_api_key, model=model_name)
    summary_prompt = PromptTemplate(
        input_variables=["chat"],
        template="""
        Provide a clear and easy to understand , label of the following chat one simple sentence:

        Chat:
        {chat}
        """
    )
    summary_chain = LLMChain(llm=llm, prompt=summary_prompt)
    summary_result = summary_chain.run(chat=chat)
    return summary_result


# df = pd.read_csv("Combined_Customer_Chat_Dataset.csv")
# test_list = df["chat_history"].head(5).tolist()

# for i, test in enumerate(test_list):
#     print(f"Test {i}: ", test)
#     print("Sentiment: ", sentiment_model(test))
#     print("Classification: ", classification_model(test, ["support", "feedback", "complaint", "orders", "others"]))
#     print("Summary: ", summary_model(test))
#     print("Label: ", label_model(test))
#     print("\n")

# print(classification_model("Customer:I can't log in to my account. Admin: Let me assist you.",["support", "feedback", "complaint", "orders", "others"]))