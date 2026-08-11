from llm.llm_file import llm
from tools.currency import get_exchange_rate

llm_with_tools = llm.bind_tools([get_exchange_rate])

response = llm_with_tools.invoke(
    "What is the current USD to PKR exchange rate?"
)

print(response)