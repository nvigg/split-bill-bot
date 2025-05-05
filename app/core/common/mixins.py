from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class IDMixin:
    id: UUID | None = field(default=None, kw_only=True)
