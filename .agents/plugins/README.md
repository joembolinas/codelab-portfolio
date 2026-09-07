# Workspace Plugins

This directory contains self-contained, deployable customization plugins for the workspace, explicitly registered via [`.agents/plugins.json`](../plugins.json).

## Directory Structure

Each plugin is located in its own subdirectory and contains a manifest (`plugin.json`):

```text
plugins/<plugin_name>/
├── plugin.json       # Required: Manifest declaring plugin name and state
├── mcp_config.json   # Optional: MCP servers exposed by the plugin
├── hooks.json        # Optional: Lifecycle hooks run by the plugin
├── rules/            # Optional: Rules applied when plugin is active (e.g. AGENTS.md)
└── skills/           # Optional: Skills exposed by the plugin
```

## Active Plugins

- [`codelab-tools`](codelab-tools/plugin.json): Workspace maintenance, review, and documentation bundle for Google Codelab Portfolio.
