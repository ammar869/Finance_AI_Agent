from src.llm.llm_file import llm
from src.tools.currency import get_exchange_rate
from langchain_core.messages import HumanMessage, ToolMessage


# Bind one tool to the LLM
llm_with_tools = llm.bind_tools([get_exchange_rate])


# User asks a question
user_message = "What is the current USD to PKR exchange rate?"

response = llm_with_tools.invoke(user_message)

print("Tool call:")
print(response.tool_calls)


# Get the tool call
tool_call = response.tool_calls[0]


# Execute the tool
tool_result = get_exchange_rate.invoke(tool_call["args"])

print("Tool result:")
print(tool_result)


# Create ToolMessage
tool_message = ToolMessage(
    content=str(tool_result),
    tool_call_id=tool_call["id"]
)


# Send tool result back to LLM
final_response = llm_with_tools.invoke([
    HumanMessage(content=user_message),
    response,
    tool_message
])


# Final answer
print("Final answer:")
print(final_response.content)