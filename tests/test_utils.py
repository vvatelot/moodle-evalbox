from moodle_evalbox.utils import clean_html_text


def test_clean_html_text():
    assert clean_html_text("<p>Hello World</p>") == "Hello World"
    assert (
        clean_html_text("<p>Text with another line</p>\n<p></p>")
        == "Text with another line\n"
    )
