# Readme
Personal Note: I am not keeping this work in the main DAI-Techstack-ALL repo because the aider need different repository which it will use to update the code while working with aider. And I don't but to slow down the process of experiments or make unwanted changed in that main work.

## What is Aider?
Aider is AI pair programming in your terminal
Aider lets you pair program with LLMs, to edit code in your local git repository. Start a new project or work with an existing code base. Aider works best with Claude 3.5 Sonnet, DeepSeek V3, o1 & GPT-4o and can connect to almost any LLM.

https://aider.chat/

## Aider Modes 
/chat-mode code - Aider will make changes to your code to satisfy your requests.   
/chat-mode architect - Aider will first propose a solution, then ask if you want it to turn that proposal into edits to your files.   
/chat-mode ask - Aider will answer questions about your code, but never edit it.   
/chat-mode help - Aider will answer questions about using aider, configuring, troubleshooting, etc.   

## Gettomg Started
```
python -m pip install aider-install
aider-install

# Change directory into your code base
cd /to/your/project

# Work with Claude 3.5 Sonnet on your code
aider --model sonnet --anthropic-api-key your-key-goes-here

# Work with GPT-4o on your code
aider --model gpt-4o --openai-api-key your-key-goes-here
```

## Connect with deepseek 
```
python -m pip install -U aider-chat

export DEEPSEEK_API_KEY=<key> # Mac/Linux
setx   DEEPSEEK_API_KEY <key> # Windows, restart shell after setx

# Use DeepSeek Coder V2
aider --deepseek
```

## Connect with local Ollama 
```
# Pull the model
ollama pull <model>

# Start your ollama server
ollama serve

# In another terminal window...
python -m pip install -U aider-chat

export OLLAMA_API_BASE=http://127.0.0.1:11434 # Mac/Linux
setx   OLLAMA_API_BASE http://127.0.0.1:11434 # Windows, restart shell after setx

aider --model ollama_chat/<model>
```

## Connect with Gemini 
```
python -m pip install -U aider-chat

# You may need to install google-generativeai
pip install -U google-generativeai

# Or with pipx...
pipx inject aider-chat google-generativeai

export GEMINI_API_KEY=<key> # Mac/Linux
setx   GEMINI_API_KEY <key> # Windows, restart shell after setx

aider --model gemini/gemini-1.5-pro-latest

# List models available from Gemini
aider --list-models gemini/
```

## Connect with Antropic 
```
python -m pip install -U aider-chat

export ANTHROPIC_API_KEY=<key> # Mac/Linux
setx   ANTHROPIC_API_KEY <key> # Windows, restart shell after setx

# Aider uses Claude 3.5 Sonnet by default (or use --sonnet)
aider

# Claude 3 Opus
aider --opus

# List models available from Anthropic
aider --list-models anthropic/
```

## Connect with openai-api-key
```
python -m pip install -U aider-chat

export OPENAI_API_KEY=<key> # Mac/Linux
setx   OPENAI_API_KEY <key> # Windows, restart shell after setx

# Aider uses gpt-4o by default (or use --4o)
aider

# GPT-4o
aider --4o

# GPT-3.5 Turbo
aider --35-turbo

# o1-mini
aider --model o1-mini

# o1-preview
aider --model o1-preview

# List models available from OpenAI
aider --list-models openai/

```
## Connect with GROQ
```
python -m pip install -U aider-chat

export GROQ_API_KEY=<key> # Mac/Linux
setx   GROQ_API_KEY <key> # Windows, restart shell after setx

aider --model groq/llama3-70b-8192

# List models available from Groq
aider --list-models groq/

```