from flake8_todo import check_todo_notes

T000 = "T000 Todo note found."


def test_todo():
    assert check_todo_notes("TODO this line") == (0, T000)
    assert check_todo_notes("# TODO in comment") == (2, T000)
    assert check_todo_notes("# FIXME") == (2, T000)
    assert check_todo_notes("# XXX") == (2, T000)


def test_todo_multiple():
    assert check_todo_notes("# TODO FIXME") == (2, T000)


def test_todo_word_boundaries():
    assert check_todo_notes("# MASTODON") == (5, T000)
