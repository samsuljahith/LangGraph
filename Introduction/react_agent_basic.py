from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.agents import initialize_agent,tool,AgentType



load_dotenv()
@tool
def web_search_tool(query: str) -> str:
    """Search the web for the given query and return results."""
    # Placeholder for web search functionality
    return f"Results for '{query}' from web search."
tools=[web_search_tool]
llm = ChatGroq(model="compound-beta", temperature=0)
agent= initialize_agent(llm=llm, tools=tools, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

result=agent.invoke({"input":"Give me a tweet about today wheather in chennai"})
print(result)
