from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

api_key = 'AIzaSyAyRTXsvRY8uzNSwTOecU9VODPHpsu1ky8'
llm = ChatGoogleGenerativeAI(api_key=api_key, model='gemini-pro', temperature=0.7)
classes = [ "complaint", "feedback", "support", "login"]
chat = ''
classification_prompt = PromptTemplate(
    input_variables=[chat, classes],
    template="""
Analyze the following conversation and determine which class it belongs to. Choose from the given options.

Available Classes: {classes}

Conversation:
{chat}

Output the class as one word only.

exmple :
chat:
 Customer: Hi Can i ask something?
 Admin: Hello How can i help you today?
 customer : can you help me i can't login to my account?
 Admin:sure i can help you .

the output will be :
(login)


    """
)

classification_chain = LLMChain(llm=llm, prompt=classification_prompt)

def calculate_accuracy(predictions, true_labels):
    correct = sum(p == t for p, t in zip(predictions, true_labels))
    return correct / len(true_labels) if true_labels else 0

test_chats = [
 "Customer: I can't log in to my account. Admin: Let me assist you.",
  "Customer: I love your service! Admin: Thank you!",
   "Customer: I'm not happy with my order. Admin: I'm sorry to hear that."
]

true_labels = ["complaint", "feedback", "support", "login"]
predictions = []
for chat_history in test_chats:
    classification_result = classification_chain.run(chat=chat_history, classes=classes)
    predictions.append(classification_result.strip())

accuracy = calculate_accuracy(predictions, true_labels)
#print(f"Predictions: {predictions}")
#print(f"Accuracy: {accuracy * 100:.2f}%")


chat_history = '''Customer: The app won’t let me log in.
 Admin: Have you tried resetting your password?

'''

classification_result = classification_chain.run(chat=chat_history, classes=classes)
print(f"Classification Result: {classification_result}")