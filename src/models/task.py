from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional


@dataclass
class Task:
    id: int
    title: str
    description: str
    priority: str
    status: str = "A Fazer"
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    completed_at: Optional[datetime] = None

    def complete(self):
        self.status = "Concluído"
        self.completed_at = datetime.now(timezone.utc)

