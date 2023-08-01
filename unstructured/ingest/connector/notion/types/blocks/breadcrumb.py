# https://developers.notion.com/reference/block#breadcrumb
from dataclasses import dataclass

from unstructured.ingest.connector.notion.interfaces import BlockBase


@dataclass
class Breadcrumb(BlockBase):
    @staticmethod
    def can_have_children() -> bool:
        return False

    @classmethod
    def from_dict(cls, data: dict):
        return cls()
