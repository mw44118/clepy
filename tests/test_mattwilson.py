# vim: set expandtab ts=4 sw=4 filetype=python:

import tempfile, unittest

from mock import Mock, patch

import clepy.mattwilson as wmw

class TestMattWilson(unittest.TestCase):

    def test_draw_ascii_spinner(self):
        wmw.draw_ascii_spinner(0.001)


m, t = Mock(), Mock()

@patch('subprocess.call', m)
@patch('tempfile.NamedTemporaryFile', t)
def test_edit_with_editor_1():

    """
    Verify we can load a blank editor.
    """

    wmw.edit_with_editor()
    assert m.called
    assert t.called


@patch('subprocess.call', m)
@patch('tempfile.NamedTemporaryFile', t)
def test_edit_with_editor_2():

    """
    Verify we can load a variable into the editor.
    """

    wmw.edit_with_editor('abcdef')
    assert m.called
    assert t.called

class TestFigureOutPager(unittest.TestCase):

    m = Mock()

    @patch('subprocess.Popen', m)
    def test_1(self):
        """
        Verify we handle when $PAGER looks like 'less -z 40'
        """

        pager = wmw.figure_out_pager({'PAGER':'less -z 40'})
        assert pager == ['less', '-z', '40'], "Got %s back" % pager

    def test_2(self):

        pager = wmw.figure_out_pager({})
        assert pager == ['less'], "Got %s back" % pager

