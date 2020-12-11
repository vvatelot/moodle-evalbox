from moodle_evalbox.evalbox import generate_evalbox_txt
from moodle_evalbox.models import Answer, Question

questions = [
    Question(
        id=12,
        type="multichoice",
        question_text="First question is here",
        default_grade=1,
        default_penalty=0.3,
        hidden=0,
        single=True,
        answer_numbering="abc",
        answer=[
            Answer(answer_text="First answer", fraction=-33.3, valid=False),
            Answer(answer_text="Second answer", fraction=-33.3, valid=False),
            Answer(answer_text="Third and good one answer", fraction=100, valid=True),
        ],
    ),
    Question(
        id=13,
        type="multichoice",
        question_text="Hey, this is another question",
        default_grade=1,
        default_penalty=0.3,
        hidden=0,
        single=True,
        answer_numbering="abc",
        answer=[
            Answer(
                answer_text="OK, so this is a valid answer", fraction=50, valid=True
            ),
            Answer(
                answer_text="And here is another valid answer", fraction=50, valid=True
            ),
            Answer(answer_text="Wrong", fraction=-50, valid=False),
            Answer(answer_text="Try again", fraction=-50, valid=False),
        ],
    ),
]


def test_generate_evalbox_txt():
    generated_txt = generate_evalbox_txt(questions=questions)
    assert generated_txt == (
        "First question is here\n"
        "- First answer\n"
        "- Second answer\n"
        "+ Third and good one answer\n"
        "====\n"
        "Hey, this is another question\n"
        "+ OK, so this is a valid answer\n"
        "+ And here is another valid answer\n"
        "- Wrong\n"
        "- Try again\n"
        "====\n"
    )
