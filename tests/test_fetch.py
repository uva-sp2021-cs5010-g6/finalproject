
import pytest

import project01.fetch as fetch
import tempfile


@pytest.fixture
def tempfile_setup():
    with tempfile.NamedTemporaryFile(mode="w") as tf:
        yield tf


def test_constructor(tempfile_setup):
    fetcher = fetch.Fetcher(uris=tempfile_setup.name, base="testbase", feedback=False)
    assert fetcher._uris == []
    assert fetcher._base == "testbase"
    assert fetcher._feedback == False


def test_parse_file(tempfile_setup):
    print(tempfile_setup)
    tempfile_setup.write("Testlinegood\n")
    tempfile_setup.write("#Commented line\n")
    tempfile_setup.write("2Testlinegood")
    tempfile_setup.flush()
    fetcher = fetch.Fetcher(uris=tempfile_setup.name)
    assert fetcher._uris == ["Testlinegood", "2Testlinegood"] 


def test_add_uri(tempfile_setup):
    tempfile_setup.write("Testlinegood\n")
    tempfile_setup.flush()
    fetcher = fetch.Fetcher(uris=tempfile_setup.name)
    fetcher.add_uri("next-line")
    assert fetcher._uris == ["Testlinegood", "next-line"]


def test_fetch():
    # Will need to spy this
    pass
