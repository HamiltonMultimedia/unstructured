# https://developers.notion.com/reference/block#equation
from dataclasses import dataclass

from unstructured.ingest.connector.notion.interfaces import BlockBase


@dataclass
class Equation(BlockBase):
    expression: str

    @staticmethod
    def can_have_children() -> bool:
        return False

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
