from pydantic import BaseModel
from typing import List


class IntentSchema(BaseModel):
    app_name: str
    modules: List[str]
    roles: List[str]
    features: List[str]