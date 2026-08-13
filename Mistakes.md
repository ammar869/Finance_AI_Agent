# Challenges in this project 

phly sari libraries or installation, phly saaari intalltion kar ke rakho

uv ko seekha, kh wo kesey venv se bhtr he 

phly hamen .gitignore bnaani he, phir env keys dal kar gitignore ko update karna he 
then 
github ma kaafi masley aye
phit phla tool bnaya: cureency
api ko bulana seekha or kesey tool ke sath kaam karta he 
phir binding seekhi 
phir calling se tool msg nikala
phir sarey msgs ko ikhata kar ke ik ma dala t kh llm proper answer de sakey words ma 

dusra tool bnaya 
buildin tool bnaya 

masla yhan pr aya kh :
chotey chotey errors ki wajha se kaam kharab hua.
last ma jab ziada tools ho gaey they to 
errors a rhy they, 
wo asla ma tools abstraction ka koi scean tha 

folders or files ke name different rakhney hen

from src.llm.llm_file import llm
from src.tools.exchange_rate import get_exchange_rate

code ma phly kia aana he baad ma kia aana he is ko zarri squenece ma le kr aana he

response
   ↓
response.tool_calls[0]
   ↓
tool_call
   ↓
tool_call["args"]
   ↓
{"base_currency": "USD", "target_currency": "PKR"}
   ↓
get_exchange_rate.invoke(...)
   ↓
Real exchange rate


dusri files ko import karna he 

Structure
LLM
 ↓
understands question
 ↓
decides a tool is needed
 ↓
generates tool call
 ↓
YOUR CODE executes the tool


