from typing import Any

from task.tools.deployment.base_agent_tool import BaseAgentTool


class CalculationsAgentTool(BaseAgentTool):

    @property
    def deployment_name(self) -> str:
        return 'calculations-agent'

    @property
    def name(self) -> str:
        return "calculations_agent"

    @property
    def description(self) -> str:
        return "Agent that process calculation"

    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The query or instruction to send to the Calculations Agent."
                },
                "propagate_history": {
                    "type": "boolean",
                    "default": False,
                    "description":
                        "Include previous conversation history between the current agent and Calculations Agent. "
                    },
            },
            "required": [
                "prompt"
            ]
        }

    #TODO:
    # Provide implementations of deployment_name (in core config), name, description and parameters.
    # Don't forget to mark them as @property
    # Parameters:
    #   - prompt: string. Required.
    #   - propagate_history: boolean

