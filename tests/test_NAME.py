# import NAME


def setup():
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"


def test_basic():
    assert 1 + 1 == 2
    print "I RAN!"
