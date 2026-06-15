from pydantic import BaseModel
from typing import List


class Component(BaseModel):
    id: str
    dependencies: List[str] = []


class SystemGraph(BaseModel):
    components: List[Component]