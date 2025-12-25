from typing import Any

from task.tools.deployment.base_agent_tool import BaseAgentTool


class WebSearchAgentTool(BaseAgentTool):

    #TODO:
    # Provide implementations of deployment_name (in core config), name, description and parameters.
    # Don't forget to mark them as @property
    # Parameters:
    #   - prompt: string. Required.
    #   - propagate_history: boolean

    @property
    def deployment_name(self) -> str:
        return "web-search-agent"

    @property
    def name(self) -> str:
        return "web-search-agent"

    @property
    def description(self) -> str:
        return ("WEB Search Agent. Performs research in WEB based on the user request. "
                "Equipped with: WEB search (DuckDuckGo via MCP) and is able to fetch WEB pages content.")

    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The query or instruction to send to the Content Management Agent."
                },
                "propagate_history": {
                    "type": "boolean",
                    "default": False,
                    "description":
                        "Include previous conversation history between the current agent and Calculations Agent. "
                }
            },
            "required": ["prompt"]
        }
