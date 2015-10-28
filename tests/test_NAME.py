import nose.tools as nt
# import NAME


def setup():
    print "SETUP!"


def teardown():
    print "TEAR DOWN!"


def test_basic():
    nt.eq_(1 + 1, 2)
    print "I RAN!"
