from typing import Any

from task.tools.deployment.base_agent_tool import BaseAgentTool


class ContentManagementAgentTool(BaseAgentTool):

    @property
    def deployment_name(self) -> str:
        return "content-management-agent"

    @property
    def name(self) -> str:
        return "content-management-agent"

    @property
    def description(self) -> str:
        return "Content Management Agent. Equipped with: Files content extractor and RAG search (supports PDF, TXT, CSV files). Able tp generate PDF, TXT, CSV files by provided text content"

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

    #TODO:
    # Provide implementations of deployment_name (in core config), name, description and parameters.
    # Don't forget to mark them as @property
    # Parameters:
    #   - prompt: string. Required.
    #   - propagate_history: boolean

