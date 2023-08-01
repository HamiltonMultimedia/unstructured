# https://developers.notion.com/reference/block#to-do
from dataclasses import dataclass, field
from typing import List

from unstructured.ingest.connector.notion.interfaces import BlockBase
from unstructured.ingest.connector.notion.types.rich_text import RichText


@dataclass
class ToDo(BlockBase):
    color: str
    checked: bool = False
    rich_text: List[RichText] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict):
        rich_text = data.pop("rich_text", [])
        todo = cls(**data)
        todo.rich_text = [RichText.from_dict(rt) for rt in rich_text]
        return todo
