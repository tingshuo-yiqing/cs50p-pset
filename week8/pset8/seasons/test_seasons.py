import pytest
from seasons import check_birthday


def test_valid_check_birthday():
    from datetime import date
    assert check_birthday("1999-01-01") == date(1999, 1, 1)
    assert check_birthday("1999-01-11") == date(1999, 1, 11)


def test_invalid_check_birthday():
    with pytest.raises(SystemExit):  # 验证异常
        check_birthday("cat")
    
    with pytest.raises(SystemExit):
        check_birthday("Januray 1, 1999")

    with pytest.raises(SystemExit):
        check_birthday("")
    
    with pytest.raises(SystemExit):
        check_birthday("1999-2-30")