from ..urlprint import url_print


def test_url(capsys):
    url_print('ggg', 'smit', 'cool.com')
    data = capsys.readouterr()
    expected_url = 'ggg://smit.cool.com\n'
    assert data.out == expected_url
