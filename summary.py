from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

api_key = 'AIzaSyAyRTXsvRY8uzNSwTOecU9VODPHpsu1ky8'
llm = ChatGoogleGenerativeAI(api_key=api_key, model='gemini-pro', temperature=0.7)


summary_prompt = PromptTemplate(
    input_variables=["chat"],
    template="""
    Provide a clear and easy to understand , summary of the following chat in no more than 50 words:

    Chat:
    {chat}
    """
)

summary_chain = LLMChain(llm=llm, prompt=summary_prompt)


chat = """Customer: Hi, can I ask something?
Admin: Hello, how can I help you today?
Customer: Can you help me? I can't log in to my account.
Admin: Sure, I can help you with that."""


summary_result = summary_chain.run(chat=chat)
print(f"Summary: {summary_result}")