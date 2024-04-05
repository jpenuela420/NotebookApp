from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class Note:
    code: int
    title: str
    text: str
    importance: str
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"
    creation_date: datetime = field(default=datetime.now)
    tags: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        return (f"Code: {self.code}\n"
                f"Creation date: {self.creation_date}\n"
                f" title: {self.text}")

    def add_tag(self, tag: str):
        if tag in self.tags:
            return
        else:
            self.tags.append(tag)
            return

class Notebook:
    def __init__(self):
        self.notes = dict[int, Note] = {}

    def add_note(self, title: str, text: str, importance: str):
        code = len(self.notes) + 1
        self.notes[code] = Note(code, title, text, importance)
        return

    def important_notes(self):
        return [i for i in self.notes.values() if i.importance in [Note.HIGH, Note.MEDIUM]]

    def tags_note_count(self) -> dict[str, int]:
        tags_count: dict[str, int] = {}
        for i in self.notes.values():
            for j in i.tags:
                tags_count[j] = tags_count.get(j, 0) + 1
        return tags_count
