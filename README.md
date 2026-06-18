# LangGraph — Introduction Examples

A beginner-friendly introduction to LangGraph, starting with a minimal ReAct agent. Uses Groq's Compound Beta model (which has built-in web search capability) so the agent can answer live questions without manual tool configuration.

## Contents

| File | Description |
|------|-------------|
| `Introduction/react_agent_basic.py` | Minimal LangGraph ReAct agent with a web search tool, backed by Groq Compound Beta |

## How It Works

The script creates a LangGraph `create_react_agent` with:
- **LLM** — Groq `compound-beta` (natively supports web search)
- **Tool** — `web_search_tool` (LangChain `@tool` decorator)
- **Agent type** — `ZERO_SHOT_REACT_DESCRIPTION`

It runs a single query about current weather as a demonstration.

## Setup

```bash
pip install langchain langchain-groq python-dotenv
```

```env
# .env
GROQ_API_KEY=your_key
```

```bash
python Introduction/react_agent_basic.py
```

## Purpose

This repo is a learning sandbox for exploring LangGraph patterns. The `Introduction/` directory is the starting point — more complex agent patterns (tool-calling, multi-agent, human-in-the-loop) can be added as additional modules.
