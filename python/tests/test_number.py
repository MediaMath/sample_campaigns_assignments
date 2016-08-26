from .context import NumberFormat

def test_stringify_number_sub20():
    assert NumberFormat.stringify_number(1) == "one"
    assert  NumberFormat.stringify_number(5) == "five"
    assert  NumberFormat.stringify_number(10) == "ten"
    assert  NumberFormat.stringify_number(16) == "sixteen"

def test_stringify_number_sub100():
    assert NumberFormat.stringify_number(20) == "twenty"
    assert NumberFormat.stringify_number(21) == "twenty-one"
    assert NumberFormat.stringify_number(33) == "thirty-three"
    assert NumberFormat.stringify_number(90) == "ninety"


def test_stringify_number_sub1K():
    assert NumberFormat.stringify_number(100) == "one hundred"
    assert NumberFormat.stringify_number(101) == "one hundred one"
    assert NumberFormat.stringify_number(120) == "one hundred twenty"
    assert NumberFormat.stringify_number(221) == "two hundred twenty-one"
    assert NumberFormat.stringify_number(333) == "three hundred thirty-three"

def test_stringify_number_sub1M():
    assert NumberFormat.stringify_number(1000) == "one thousand"
    assert NumberFormat.stringify_number(1100) == "one thousand one hundred"
    assert NumberFormat.stringify_number(1101) == "one thousand one hundred one"
    assert NumberFormat.stringify_number(1120) == "one thousand one hundred twenty"
    assert NumberFormat.stringify_number(2221) == "two thousand two hundred twenty-one"
    assert NumberFormat.stringify_number(3333) == "three thousand three hundred thirty-three"
    assert NumberFormat.stringify_number(10000) == "ten thousand"
    assert NumberFormat.stringify_number(10005) == "ten thousand five"
    assert NumberFormat.stringify_number(22005) == "twenty-two thousand five"
    assert NumberFormat.stringify_number(35315) == "thirty-five thousand three hundred fifteen"
    assert NumberFormat.stringify_number(935315) == "nine hundred thirty-five thousand three hundred fifteen"

def test_stringify_number_sub1B():
    assert NumberFormat.stringify_number(1000000) == "one million"
    assert NumberFormat.stringify_number(1001000) == "one million one thousand"
    assert NumberFormat.stringify_number(123456789) == "one hundred twenty-three million four hundred fifty-six thousand seven hundred eighty-nine"

def test_stringify_number_sub1T():
    assert NumberFormat.stringify_number(1000000000) == "one billion"
    assert NumberFormat.stringify_number(1001001001) == "one billion one million one thousand one"
    assert NumberFormat.stringify_number(501123456789) == "five hundred one billion one hundred twenty-three million four hundred fifty-six thousand seven hundred eighty-nine"
    assert NumberFormat.stringify_number(999999999999) == "nine hundred ninety-nine billion nine hundred ninety-nine million nine hundred ninety-nine thousand nine hundred ninety-nine"
