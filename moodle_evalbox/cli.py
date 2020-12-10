from os.path import basename, exists
from typing import Optional

from typer import Argument, Option, Typer, colors, secho

from .evalbox import generate_evalbox_txt
from .files import create_file, read_xml_file
from .moodle import extract_quiz_from_quiz_object

app = Typer()


@app.command()
def convert_moodle_to_evalbox(
    file_path: str = Argument(
        ..., help="You have to provide the full path of your Moodle XML File here"
    ),
    display: Optional[bool] = Option(
        False,
        help="If you want to display the result in the terminal, set it to True",
    ),
):
    """
    Extract questions from a Moodle xml file
    """
    if not exists(file_path):
        secho(f"📛 File {file_path} does not exist", fg=colors.RED)
        return

    if not file_path.endswith(".xml"):
        secho(
            f"📛 File {file_path} must be an xml file with the `.xml` extension",
            fg=colors.RED,
        )
        return

    file_basename = basename(file_path)
    secho(f"✅ Working with {file_basename}...", fg=colors.GREEN)
    output_filename = f"{file_basename[0:-4]}.txt"

    moodle_quiz = read_xml_file(file_path)
    questions = extract_quiz_from_quiz_object(moodle_quiz)
    evalbox_txt = generate_evalbox_txt(questions=questions)
    if display:
        evalbox_txt

    create_file(output_filename, evalbox_txt)
    secho(
        f"🤟 File {output_filename} created successfully",
        fg=colors.GREEN,
        bold=True,
    )


if __name__ == "__main__":
    app()
