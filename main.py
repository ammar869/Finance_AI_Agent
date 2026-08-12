from src.llm.llm_file import llm
from src.tools.currency import get_exchange_rate
from src.tools.percentage import calculate_percentage
from langchain_core.messages import ToolMessage
llm_with_tools = llm.bind_tools([get_exchange_rate])

# 1. User asks question
user_message = "What is the current USD to PKR exchange rate?"
response = llm_with_tools.invoke(user_message)


tool_call = response.tool_calls[0]


tools = [
    get_exchange_rate,
    calculate_percentage
]

tool_result = get_exchange_rate.invoke(tool_call["args"])

print(tool_result)


tool_message = ToolMessage(
    content=str(tool_result),
    tool_call_id=tool_call["id"]
)

# 6. Send everything back to the LLM
final_response = llm_with_tools.invoke([
    user_message,
    response,
    tool_message
])
# 7. Final answer
print("Final answer:")
print(final_response.content)