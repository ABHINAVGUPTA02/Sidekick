from typing import Annotated
from langgraph.graph.message import add_messages
from typing import TypedDict, List, Any, Optional

class State(TypedDict):
    messages: Annotated[List[Any], add_messages]
    success_criteria: str
    feedback_on_work: Optional[str]
    success_criteria_met: bool
    user_input_needed: bool
