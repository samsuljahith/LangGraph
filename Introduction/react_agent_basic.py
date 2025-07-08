from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="compound-beta", temperature=0)

print(llm.invoke("What is the capital of France?"))
