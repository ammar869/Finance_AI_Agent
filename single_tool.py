from src.llm.llm_file import llm
from src.tools.currency import get_exchange_rate
from src.tools.percentage import calculate_percentage
from langchain_core.messages import ToolMessage


# Available tools
tools = [
    get_exchange_rate,
    calculate_percentage
]
tool_map = {
    tool.name: tool
    for tool in tools
}

# Bind both tools to ONE LLM
llm_with_tools = llm.bind_tools(tools)


# User asks a question
#user_message = "What is the current USD to PKR exchange rate?"
user_message = "What is 15 percent of 2000?"
response = llm_with_tools.invoke(user_message)

print("Tool calls:")
print(response.tool_calls)


# Get the tool call selected by the LLM
tool_call = response.tool_calls[0]


# Execute the selected tool
tool_result = get_exchange_rate.invoke(tool_call["args"])

print("Tool result:")
print(tool_result)


# Create ToolMessage
tool_message = ToolMessage(
    content=str(tool_result),
    tool_call_id=tool_call["id"]
)


# Send result back to LLM
final_response = llm_with_tools.invoke([
    user_message,
    response,
    tool_message
])


print("Final answer:")
print(final_response.content)