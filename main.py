from src.llm.llm_file import llm
from src.tools.currency import get_exchange_rate
from src.tools.percentage import calculate_percentage
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage, ToolMessage


searching_tool = DuckDuckGoSearchRun
# Available tools
tools = [
    get_exchange_rate,
    calculate_percentage,
    searching_tool
]

# Tool name → actual tool
tool_map = {
    tool.name: tool
    for tool in tools
}


# Bind both tools to ONE LLM
llm_with_tools = llm.bind_tools(tools)


# User asks a question
user_message = "What is 15 percent of 2000?"

response = llm_with_tools.invoke(user_message)

print("Tool calls:")
print(response.tool_calls)


# Get the tool call selected by the LLM
tool_call = response.tool_calls[0]


# Find the correct tool
tool = tool_map[tool_call["name"]]


# Execute the correct tool
tool_result = tool.invoke(tool_call["args"])

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