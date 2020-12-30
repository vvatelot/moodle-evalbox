from typing import List

from .models import Question
from .utils import clean_html_text


def generate_evalbox_txt(questions: List[Question], quiz_name: str) -> str:
    evalbox_txt = ""
    for q in questions:
        evalbox_txt += f"{clean_html_text(q.question_text)}\n"
        for a in q.answer:
            evalbox_txt += (
                f"{'+' if a.valid else '-'} {clean_html_text(a.answer_text)}\n"
            )

        evalbox_txt += f"==== {quiz_name}\n"

    return evalbox_txt
