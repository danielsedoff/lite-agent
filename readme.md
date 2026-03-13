# capi-agent

This is a lightweight Python agent written for my own hardware which is an average CPU-only PC. It expects llama.cpp running locally. Before using this agent I start the llm server with the `llama-server` shell command.

## Components

### `agent.py`

`agent.py` collects commandline arguments together as text. It looks for an LLM running on `localhost:8080`. If the LLM is found, the agent feeds the prompt to it and waits for a response. If the only CLI argument for this script is `clear`, then it removes `context.json`.

### `context.json`

If not present, this file is created by `agent.py` at its first run. This json file contains a system prompt and a series of prompts and responses from and to the agent stored as `role:user` and `role:assistant` which together represent the context.

### `browse.py`

This script uses Playwright to open a web page and process hyperlinks in it. This one is for sample purposes. It does not run fast and will not allow public web service abuse. the output of this script can be redirected into a file, e.g. `$ python browse.py oxford dictionary > dictionary.log`

### `schedule.py`

Reads `schedule.json` and runs shell commands according to it. If there is not `schedule.json` then it is created at first run. Every entry is either a timeout, i.e. run once after waiting a certain time, or an interval, i.e. run and repeat every `x` seconds.

## Installation

- clone the repository.
- create a new venv, e.g. run: `python3 -m venv venv`.
- activate the environment, e.g. `source venv/bin/activate`.
- install requirements, e.g. `pip install -r requirements.txt`. 
