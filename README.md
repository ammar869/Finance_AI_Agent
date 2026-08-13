# 💰 Finance AI Agent

A tool-using AI financial assistant built with **Python, LangChain, Groq, and SQLite**.

The project demonstrates how an LLM can understand a user's financial request, select the appropriate tool, execute it, and use the result to generate a final response.

## 🚀 Features

- 💱 **Currency Conversion**
  - Fetches real-time exchange rates.
  - Example: USD → PKR

- 🧮 **Percentage Calculations**
  - Calculates percentages using a dedicated tool.
  - Example: 15% of 2000

- 🌐 **Web Search**
  - Uses DuckDuckGo to retrieve current information from the web.

- 🗄️ **SQL Database Integration**
  - Uses `SQLDatabaseToolkit`.
  - Connects the AI agent to a SQLite finance database.
  - Can inspect tables, check SQL queries, and execute SQL queries.

- 🤖 **LLM Tool Calling**
  - Uses one LLM with multiple tools.
  - The LLM decides which tool is appropriate for a user's request.

- 🔄 **Tool Execution Flow**
  - Demonstrates how tool calls and tool results are passed between the LLM and external tools.

## 🧠 Architecture

```text
                    User
                      │
                      ▼
                   LLM
                      │
              ┌───────┴────────┐
              │  Tool Selection │
              └───────┬────────┘
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
 Currency         Percentage      Web Search
   Tool              Tool            Tool
       │              │              │
       └──────────────┼──────────────┘
                      │
                      ▼
                SQL Database
                / SQL Tools
                      │
                      ▼
                 Tool Result
                      │
                      ▼
                    LLM
                      │
                      ▼
                Final Answer