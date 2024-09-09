from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

api_key = 'AIzaSyAyRTXsvRY8uzNSwTOecU9VODPHpsu1ky8'
llm = ChatGoogleGenerativeAI(api_key=api_key, model='gemini-pro', temperature=0.7)

sentiment_prompt = PromptTemplate(
    input_variables=["chat"],
    template="""
Analyze the following conversation and determine the sentiment. Output whether it is 'positive', 'negative', or 'neutral',
along with the degree of sentiment on a scale from 1 to 5 (for positive), -1 to -5 (for negative), or 0 (for neutral).

Chat:
{chat}

Output format:
Sentiment: [positive/negative/neutral]
Degree: [1-5/-1 to -5/0]
"""
)

sentiment_chain = LLMChain(llm=llm, prompt=sentiment_prompt)

chat_history = """Customer: The app works fine, but I expected more features.
Admin: I'm glad to hear that. Thank you for your feedback!"""

sentiment_result = sentiment_chain.run(chat=chat_history)
print(sentiment_result)