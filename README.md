# time-tool

## Primary Contact
- **Name:** Parth Jade
- **Telegram:** @parth

## Team Name
- Solo

## Project Title
- time-tool

## One-Sentence Elevator Pitch
Simple MCP tool that returns the current UTC time in ISO 8601 format via a lightweight API.

## Detailed Project Description
This MCP tool provides a simple read-only API that returns the current UTC time in ISO 8601 format.  
It includes two endpoints:  
- `/time` – fetches the current UTC time in ISO 8601 format.  
- `/health` – returns a basic status check (`{"ok": true}`).  

The tool is lightweight, fast, and easy to integrate into AI agents, chatbots, or any application needing accurate timestamps.  
It serves as a minimal example MCP service and can be extended with additional time/date utilities.

## Install Steps
```bash
# Create and activate virtual environment
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\activate
# macOS/Linux/WSL:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
