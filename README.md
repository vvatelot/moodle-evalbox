# `moodle_evalbox`

Extract questions from a Moodle xml file

## Requirements

- Python 3.8+
- [Poetry](https://python-poetry.org/)

## Installation

```console
poetry install
```

## Use

**Usage**:

```console
convert-moodle-file [OPTIONS] FILE_PATH
```

**Arguments**:

- `FILE_PATH`: You have to provide the full path of your Moodle XML File here [required]

**Options**:

- `--display / --no-display`: If you want to display the result in the terminal, set it to True [default: False]
- `--install-completion`: Install completion for the current shell.
- `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
- `--help`: Show this message and exit.

## Example

```console
convert-moodle-file /home/user/my_moodle_file.xml
```

This generates a file `my_moodle_file.txt` in the current directory

## Tests

```console
pytest
```
