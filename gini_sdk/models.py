from enum import Enum
from pydantic import BaseModel
import base64
from pathlib import Path

class MessageType(Enum):
    system = "system"
    human = "human"
    gini = "gini"
    tool = "tool"
    error = "error"


class Attachment(BaseModel):
    name: str
    localPath: str
    base64: str
    
    @classmethod
    def from_path(cls, file_path: str) -> "Attachment":
        path = Path(file_path)
        with open(path, 'rb') as f:
            content = base64.b64encode(f.read()).decode('utf-8')
        return cls(
            name=path.name,
            base64=content,
            localPath=file_path
        )


from typing import Any, Dict, Optional
from pydantic import BaseModel
import json

class GiniRequest(BaseModel):
    action: str
    data: Dict[str, Any]
    
    def json(self) -> str:
        """Convert the request to a JSON string"""
        return json.dumps({
            "action": self.action,
            "data": self.data
        })


class GiniResponse(BaseModel):
    status: str
    response: Optional[Dict[str, Any]] = None
    error: Optional[str] = None 