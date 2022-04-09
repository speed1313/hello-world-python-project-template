from speed_project.greet import hello


def test_sample() -> None:
    assert 1 + 1 == 2


def test_hello() -> None:
    assert hello.hello() is None
