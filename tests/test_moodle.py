from moodle_evalbox.models import Answer, Question
from moodle_evalbox.moodle import extract_quiz_from_quiz_object

quiz = {
    "quiz": {
        "question": [
            {
                "@type": "category",
                "category": {
                    "text": "$course$/Défaut pour Ecocertification/eco-conception"
                },
            },
            {
                "@type": "multichoice",
                "name": {"text": "0001"},
                "questiontext": {
                    "@format": "html",
                    "text": "<p>de quelle couleur est le cheval blanc d'Henry ?</p>",
                },
                "generalfeedback": {"@format": "html", "text": None},
                "defaultgrade": "1.0000000",
                "penalty": "0.3333333",
                "hidden": "0",
                "single": "true",
                "shuffleanswers": "true",
                "answernumbering": "abc",
                "correctfeedback": {
                    "@format": "html",
                    "text": "<p>Votre réponse est correcte.</p>",
                },
                "partiallycorrectfeedback": {
                    "@format": "html",
                    "text": "<p>Votre réponse est partiellement correcte.</p>",
                },
                "incorrectfeedback": {
                    "@format": "html",
                    "text": "<p>Votre réponse est incorrecte.</p>",
                },
                "shownumcorrect": None,
                "answer": [
                    {
                        "@fraction": "100",
                        "@format": "html",
                        "text": "<p>Blanc</p>",
                        "feedback": {"@format": "html", "text": None},
                    },
                    {
                        "@fraction": "-33.33333",
                        "@format": "html",
                        "text": "<p>Bleu</p>",
                        "feedback": {"@format": "html", "text": None},
                    },
                    {
                        "@fraction": "-33.33333",
                        "@format": "html",
                        "text": "<p>Rouge</p>",
                        "feedback": {"@format": "html", "text": None},
                    },
                    {
                        "@fraction": "-33.33333",
                        "@format": "html",
                        "text": "<p>C'était pas un cheval, c'était une licorne</p>",
                        "feedback": {"@format": "html", "text": None},
                    },
                ],
            },
            {
                "@type": "multichoice",
                "name": {"text": "0002"},
                "questiontext": {
                    "@format": "html",
                    "text": "<p>Pourquoi quand on se cogne, on dit `Aïe` même quand on n'a pas mal ?</p>",
                },
                "generalfeedback": {"@format": "html", "text": None},
                "defaultgrade": "1.0000000",
                "penalty": "0.3333333",
                "hidden": "0",
                "single": "false",
                "shuffleanswers": "true",
                "answernumbering": "abc",
                "correctfeedback": {
                    "@format": "html",
                    "text": "<p>Votre réponse est correcte.</p>",
                },
                "partiallycorrectfeedback": {
                    "@format": "html",
                    "text": "<p>Votre réponse est partiellement correcte.</p>",
                },
                "incorrectfeedback": {
                    "@format": "html",
                    "text": "<p>Votre réponse est incorrecte.</p>",
                },
                "shownumcorrect": None,
                "answer": [
                    {
                        "@fraction": "50",
                        "@format": "html",
                        "text": "<p>C'est un réflexe archaïque</p>",
                        "feedback": {"@format": "html", "text": None},
                    },
                    {
                        "@fraction": "-50",
                        "@format": "html",
                        "text": "<p>Python c'est trop bien</p>",
                        "feedback": {"@format": "html", "text": None},
                    },
                    {
                        "@fraction": "50",
                        "@format": "html",
                        "text": "<p>Parce que c'est comme ça</p>",
                        "feedback": {"@format": "html", "text": None},
                    },
                    {
                        "@fraction": "-50",
                        "@format": "html",
                        "text": "<p>Javascript c'est pas bien</p>",
                        "feedback": {"@format": "html", "text": None},
                    },
                ],
            },
            {
                "@type": "multichoice",
                "name": {"text": "0003"},
                "questiontext": {
                    "@format": "html",
                    "text": "<p>Pourquoi notre lit est plus confortable le matin quand on doit en sortir que le soir quand on se couche ? </p>",
                },
                "generalfeedback": {"@format": "html", "text": None},
                "defaultgrade": "1.0000000",
                "penalty": "0.3333333",
                "hidden": "0",
                "single": "false",
                "shuffleanswers": "true",
                "answernumbering": "abc",
                "correctfeedback": {
                    "@format": "html",
                    "text": "<p>Votre réponse est correcte.</p>",
                },
                "partiallycorrectfeedback": {
                    "@format": "html",
                    "text": "<p>Votre réponse est partiellement correcte.</p>",
                },
                "incorrectfeedback": {
                    "@format": "html",
                    "text": "<p>Votre réponse est incorrecte.</p>",
                },
                "shownumcorrect": None,
                "answer": [
                    {
                        "@fraction": "33.33333",
                        "@format": "html",
                        "text": "<p>Parce qu'on a perdu du poids pendant la nuit</p>",
                        "feedback": {"@format": "html", "text": None},
                    },
                    {
                        "@fraction": "33.33333",
                        "@format": "html",
                        "text": "<p>À cause d'un paradoxe spatio temporel</p>",
                        "feedback": {"@format": "html", "text": None},
                    },
                    {
                        "@fraction": "-100",
                        "@format": "html",
                        "text": "<p>Forcément à cause de Maurice</p>",
                        "feedback": {"@format": "html", "text": None},
                    },
                    {
                        "@fraction": "33.33333",
                        "@format": "html",
                        "text": "<p>La réponse D</p>",
                        "feedback": {"@format": "html", "text": None},
                    },
                ],
            },
        ]
    }
}


def test_extract_quiz_from_quiz_object():
    questions = extract_quiz_from_quiz_object(quiz=quiz)

    assert len(questions) == 3

    assert questions[0] == Question(
        id=1,
        type="multichoice",
        question_text="<p>de quelle couleur est le cheval blanc d'Henry ?</p>",
        hidden=0,
        single=True,
        default_grade=1.00,
        default_penalty=0.3333333,
        answer_numbering="abc",
        answer=[
            Answer(answer_text="<p>Blanc</p>", fraction=100, valid=True),
            Answer(answer_text="<p>Bleu</p>", fraction=-33.33333, valid=False),
            Answer(answer_text="<p>Rouge</p>", fraction=-33.33333, valid=False),
            Answer(
                answer_text="<p>C'était pas un cheval, c'était une licorne</p>",
                fraction=-33.33333,
                valid=False,
            ),
        ],
    )

    assert questions[1] == Question(
        id=2,
        type="multichoice",
        question_text="<p>Pourquoi quand on se cogne, on dit `Aïe` même quand on n'a pas mal ?</p>",
        hidden=0,
        single=True,
        default_grade=1.00,
        default_penalty=0.3333333,
        answer_numbering="abc",
        answer=[
            Answer(
                answer_text="<p>C'est un réflexe archaïque</p>", fraction=50, valid=True
            ),
            Answer(
                answer_text="<p>Python c'est trop bien</p>", fraction=-50, valid=False
            ),
            Answer(
                answer_text="<p>Parce que c'est comme ça</p>", fraction=50, valid=True
            ),
            Answer(
                answer_text="<p>Javascript c'est pas bien</p>",
                fraction=-50,
                valid=False,
            ),
        ],
    )

    assert questions[2] == Question(
        id=3,
        type="multichoice",
        question_text="<p>Pourquoi notre lit est plus confortable le matin quand on doit en sortir que le soir quand on se couche ? </p>",
        hidden=0,
        single=True,
        default_grade=1.00,
        default_penalty=0.3333333,
        answer_numbering="abc",
        answer=[
            Answer(
                answer_text="<p>Parce qu'on a perdu du poids pendant la nuit</p>",
                fraction=33.33333,
                valid=True,
            ),
            Answer(
                answer_text="<p>À cause d'un paradoxe spatio temporel</p>",
                fraction=33.33333,
                valid=True,
            ),
            Answer(
                answer_text="<p>Forcément à cause de Maurice</p>",
                fraction=-100,
                valid=False,
            ),
            Answer(
                answer_text="<p>La réponse D</p>",
                fraction=33.33333,
                valid=True,
            ),
        ],
    )
