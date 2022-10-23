import python_test_findingstring as finding


def test_ispresent():
    assert finding.ispresent("BO")


def test_nodigit():
    assert finding.nodigit("AS")
