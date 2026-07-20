from pathlib import Path
from typing import Annotated

from pydantic import WithJsonSchema

from ..._base_models import BaseFrozenModel


class Note(BaseFrozenModel):
    title: str
    path: Annotated[Path, WithJsonSchema({"type": "string"})]
    tags: list[str]
