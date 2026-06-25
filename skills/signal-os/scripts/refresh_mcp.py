#!/usr/bin/env python3
"""Refresh Composio MCP URL and update opencode config."""
import json
import os
import sys
from pathlib import Path

CONFIG_PATH = Path.home() / ".config" / "opencode" / "opencode.json"

def refresh():
    from composio import Composio
    
    api_key = os.environ.get("COMPOSIO_API_KEY")
    if not api_key:
        print("ERROR: Set COMPOSIO_API_KEY env var first")
        sys.exit(1)
    
    c = Composio()
    session = c.create(user_id="default")
    
    mcp_url = session.mcp.url
    mcp_headers = session.mcp.headers
    
    print(f"New MCP URL: {mcp_url}")
    
    # Update config
    with open(CONFIG_PATH) as f:
        config = json.load(f)
    
    config["mcp"]["composio"]["url"] = mcp_url
    config["mcp"]["composio"]["headers"] = mcp_headers
    
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)
    
    print(f"Updated {CONFIG_PATH}")

if __name__ == "__main__":
    refresh()
