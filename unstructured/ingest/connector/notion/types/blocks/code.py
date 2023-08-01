# https://developers.notion.com/reference/block#code
from dataclasses import dataclass, field
from typing import List

from unstructured.ingest.connector.notion.interfaces import BlockBase
from unstructured.ingest.connector.notion.types.rich_text import RichText


@dataclass
class Code(BlockBase):
    language: str
    rich_text: List[RichText] = field(default_factory=list)
    caption: List[RichText] = field(default_factory=list)

    @staticmethod
    def can_have_children() -> bool:
        return False

    @classmethod
    def from_dict(cls, data: dict):
        rich_text = data.pop("rich_text", [])
        caption = data.pop("caption", [])
        return cls(
            language=data["language"],
            rich_text=[RichText.from_dict(rt) for rt in rich_text],
            caption=[RichText.from_dict(c) for c in caption],
        )
