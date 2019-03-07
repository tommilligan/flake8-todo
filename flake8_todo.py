__version__ = "1.0"

import re

import pycodestyle

PLUGIN_ID = "TOD"


def plugin_code(code):
    return "".join((PLUGIN_ID, code))


NOTE_WORDS = {
    "TODO": {"code": plugin_code("000")},
    "FIXME": {"code": plugin_code("001")},
    "XXX": {"code": plugin_code("002")},
}

# Find any one of the note words definded above
NOTE_REGEX = re.compile("\\b({})\\b".format("|".join(NOTE_WORDS)))


def match_to_flake(match):
    note_word = match.group(1)
    note = NOTE_WORDS[note_word]
    result = (
        match.start(),
        "{} Todo note found ({})".format(note["code"], note_word),
    )
    return result


def check_todo_notes(physical_line):
    if pycodestyle.noqa(physical_line):
        return
    matches = NOTE_REGEX.finditer(physical_line)
    for result in map(match_to_flake, matches):
        yield result


check_todo_notes.name = name = "flake8-todo"
check_todo_notes.version = __version__
