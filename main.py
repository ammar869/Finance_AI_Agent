from src.llm.llm_file import llm
from src.tools.currency import get_exchange_rate
from src.tools.percentage import calculate_percentage
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit

db = SQLDatabase.from_uri("sqlite:///finance.db")

toolkit = SQLDatabaseToolkit(
    db=db,
    llm=llm
)
sql_tools = toolkit.get_tools()

for tool in sql_tools:
    print(tool.name)

searching_tool = DuckDuckGoSearchRun()
# Available tools
tools = [
    get_exchange_rate,
    calculate_percentage,
    searching_tool,
    *sql_tools
]

# Tool name → actual tool
tool_map = {
    tool.name: tool
    for tool in tools
}


# Bind both tools to ONE LLM
llm_with_tools = llm.bind_tools(tools)


# User asks a question
#user_message = "Latest news about Pakistan, turkey, Saudia"
user_message = "How much money was spent on Food?"
response = llm_with_tools.invoke(user_message)

print("Tool calls:")
print(response.tool_calls)


# Get the tool call selected by the LLM
#tool_call = response.tool_calls[0]


# Find the correct tool
#tool = tool_map[tool_call["name"]]


# Execute the correct tool
#tool_result = tool.invoke(tool_call["args"])

for tool_call in response.tool_calls:

    tool = tool_map[tool_call["name"]]

    tool_result = tool.invoke(tool_call["args"])

    print(tool_call["name"])
    print(tool_result)
    
print("Tool result:")
print(tool_result)


# Create ToolMessage
tool_message = ToolMessage(
    content=str(tool_result),
    tool_call_id=tool_call["id"]
)


# Send result back to LLM
final_response = llm_with_tools.invoke([
    HumanMessage(content=user_message),
    response,
    tool_message
])


print("Final answer:")
print(final_response.content)