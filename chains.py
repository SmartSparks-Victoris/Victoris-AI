from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

api_key = 'AIzaSyAieF1HdSxfaXm1_CqGpzsGSbS3u5IRybQ'
llm = ChatGoogleGenerativeAI(api_key=api_key, model='gemini-pro', temperature=0.7)

# --- Summarization Chain (unchanged) ---
summary_prompt = PromptTemplate(
    input_variables=["chat_history"],
    template="Summarize the following chat in one sentence:\n\n{chat_history}",
)

summary_chain = LLMChain(llm=llm, prompt=summary_prompt)


# --- Sentiment Analysis Chain (modified) ---
sentiment_prompt = PromptTemplate(
    input_variables=["chat_history"],
    template="""
    Analyze the sentiment of the following chat and rate it from -5 to 5, 
    where -5 indicates highly negative and 5 indicates highly positive.
    
    Chat: {chat_history}
    
    Sentiment Score: 
    """
)

sentiment_chain = LLMChain(llm=llm, prompt=sentiment_prompt)


chat_history = "User: Hi, I have a complaint.\nAI: Hello, we are sorry for that. What happened?"
summary = summary_chain.run(chat_history)
print(f"Chat Summary: {summary}")

sentiment_output = sentiment_chain.run(chat_history)
score_str = sentiment_output.split("Sentiment Score: ")[-1].strip()  

score = float(score_str)

sentiment_parsed = {
    "type": "positive" if score > 0 else "negative",  
    "score": score
}

print(f"Sentiment (JSON): {sentiment_parsed}")