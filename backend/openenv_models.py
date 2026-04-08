from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Observation(BaseModel):
    state: str = Field(..., description="The current state of the environment (e.g. 'ready', 'analyzing', 'complete')")
    task_description: str = Field(..., description="Description of the design review task")
    design_metadata: Dict[str, Any] = Field(default_factory=dict, description="Metadata about the design being reviewed (domain, process, material)")
    audit_log: List[str] = Field(default_factory=list, description="A log of actions taken in the environment")

class Action(BaseModel):
    action_type: str = Field(..., description="The type of action: 'query', 'submit_audit', or 'reset'")
    content: Optional[str] = Field(None, description="The content of the action (e.g. audit report JSON or inquiry string)")

class Reward(BaseModel):
    value: float = Field(..., ge=0.0, le=1.0, description="The reward value from 0.0 to 1.0")
    feedback: Optional[str] = Field(None, description="Detailed feedback on the agent's performance")

class OpenEnvState(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: Dict[str, Any]
