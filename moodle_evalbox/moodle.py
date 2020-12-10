from typing import Dict, List

from .models import Answer, Question


def extract_quiz_from_quiz_object(quiz: Dict) -> List[Question]:
    return [
        Question(
            id=int(q["name"]["text"]),
            type=q["@type"],
            question_text=q["questiontext"]["text"],
            default_grade=float(q["defaultgrade"]),
            default_penalty=float(q["penalty"]),
            hidden=int(q["hidden"]),
            single=bool(q["single"]),
            answer_numbering=q["answernumbering"],
            answer=[
                Answer(
                    answer_text=a["text"],
                    fraction=float(a["@fraction"]),
                    valid=True if float(a["@fraction"]) > 0 else False,
                )
                for a in q["answer"]
            ],
        )
        for q in quiz["quiz"]["question"]
        if q["@type"] != "category"
    ]
