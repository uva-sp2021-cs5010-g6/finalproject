import os
import shutil

import pytest

## Fixture taken from  https://stackoverflow.com/a/29631801
## Allows for reliable references to knonw test files that match
## the test file name.
@pytest.fixture
def datadir(tmpdir, request):
    '''
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.
    '''
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        copytree(test_dir, str(tmpdir))
    return tmpdir

# Function taken from https://stackoverflow.com/a/12514470
# Pulled in to support older versions of python
# normally shutil.copytree would be used here, but when the
# directory exists, it throws an errors.  This corrects
# the behavior so that it doesn't care.
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
