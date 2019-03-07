from flake8_todo import check_todo_notes

TOD000 = "TOD000 Todo note found (TODO)"
TOD001 = "TOD001 Todo note found (FIXME)"
TOD002 = "TOD002 Todo note found (XXX)"


def _check(line):
    return list(check_todo_notes(line))


def test_todo():
    assert _check("TODO this line") == [(0, TOD000)]
    assert _check("# TODO in comment") == [(2, TOD000)]
    assert _check("# FIXME") == [(2, TOD001)]
    assert _check("# XXX") == [(2, TOD002)]


def test_todo_multiple():
    assert _check("# TODO FIXME") == [(2, TOD000), (7, TOD001)]


def test_todo_word_boundaries():
    assert _check("# MASTODON") == []
    assert _check("#TODO") == [(1, TOD000)]


def test_noqa():
    assert _check("TODO # noqa") == []
