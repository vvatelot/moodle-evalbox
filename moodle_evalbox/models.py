from dataclasses import dataclass
from typing import List


@dataclass
class Answer:
    answer_text: str
    fraction: float
    valid: bool


@dataclass
class Question:
    id: int
    type: str
    question_text: str
    default_grade: float
    default_penalty: float
    hidden: int
    single: bool
    answer_numbering: str
    answer: List[Answer]
