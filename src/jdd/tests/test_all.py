import filecmp
from jdd.tools.badges import create_file as badges_create
from jdd.tools.signing_lists import create_file as signing_create
from jdd.tools.stats import make_stats
from jdd.main import create_namefiles, read_file

TEST_DIR = "src/jdd/tests/"
TESTFILE = TEST_DIR + "tests_participants.xlsx"

TEST_NAME_ENSMA = TEST_DIR + 'test_ensma'
TEST_NAME_UP = TEST_DIR + 'test_up'
TEST_NAME_ALL = TEST_DIR + 'test_all'

TRUE_NAME_ALL = TEST_DIR + "true_noms_complet.csv"
TRUE_NAME_ENSMA = TEST_DIR + "true_noms_ensma.csv"
TRUE_NAME_UP = TEST_DIR + "true_noms_up.csv"
TRUE_STATS = TEST_DIR + "true_stats.txt"
TRUE_BADGES = TEST_DIR + 'true_badges.tex'
TRUE_LIST_ENSMA = TEST_DIR + 'true_list_ensma.tex'
TRUE_LIST_UP = TEST_DIR + 'true_list_up.tex'

def test_names():
    df_participants, df_ensma, df_up = read_file(TESTFILE, 'ENSMA', 'UP')
    create_namefiles(df_participants, TEST_NAME_ALL)
    assert filecmp.cmp(TEST_NAME_ALL + ".csv", TRUE_NAME_ALL, shallow=False), "Test Name all FAILED"
    create_namefiles(df_ensma, TEST_NAME_ENSMA)
    assert filecmp.cmp(TEST_NAME_ENSMA + ".csv", TRUE_NAME_ENSMA, shallow=False), "Test Name ENSMA FAILED"
    create_namefiles(df_up, TEST_NAME_UP)
    assert filecmp.cmp(TEST_NAME_UP + ".csv", TRUE_NAME_UP, shallow=False), "Test Name UP FAILED"

def test_badges():
    badges_create(TRUE_NAME_ALL, TEST_DIR + "test_badges.tex")
    assert filecmp.cmp(TEST_DIR + "test_badges.tex", TRUE_BADGES), "Test BADGES FAILED"

def test_stats():
    df_participants, df_ensma, df_up = read_file(TESTFILE, 'ENSMA', 'UP')
    make_stats(df_participants, TEST_DIR)
    assert filecmp.cmp(TEST_DIR + "stats.txt", TRUE_STATS), "Test STATS FAILED"

def test_signing_lists():
    signing_create(TRUE_NAME_ENSMA, TEST_DIR + 'test_list_ensma.tex')
    assert filecmp.cmp(TRUE_LIST_ENSMA, TEST_DIR + 'test_list_ensma.tex')
    signing_create(TRUE_NAME_UP, TEST_DIR + 'test_list_up.tex')
    assert filecmp.cmp(TRUE_LIST_UP, TEST_DIR + 'test_list_up.tex')

