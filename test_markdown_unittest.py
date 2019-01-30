'''
Test markdown.py with unittest
To run tests:
    python test_markdown_unittest.py
'''

import unittest
from markdown_adapter import run_markdown

class TestMarkdownPy(unittest.TestCase):

    def setUp(self):
        pass

    def test_non_marked_lines(self):
        '''
        Non-marked lines should only get 'p' tags around all input
        '''
        self.assertEqual( 
                run_markdown('this line has no special handling'), 
                '<p>this line has no special handling</p>')

    def test_em(self):
        '''
        Lines surrounded by asterisks should be wrapped in 'em' tags
        '''
        self.assertEqual( 
                run_markdown('*this should be wrapped in em tags*'),
                '<p><em>this should be wrapped in em tags</em></p>')

    def test_strong(self):
        '''
        Lines surrounded by double asterisks should be wrapped in 'strong' tags
        '''
        self.assertEqual( 
                run_markdown('**this should be wrapped in strong tags**'),
                '<p><strong>this should be wrapped in strong tags</strong></p>')
    
    def test_h1(self):
        '''
        Lines beginning with a single '#' should become 'h1' tags
        '''
        self.assertEqual(
                run_markdown('# This is a header'),
                '<h1>This is a header</h1>')
    
    def test_h2(self):
        '''
        Lines beginning with two '#' should become 'h2' tags
        '''
        self.assertEqual(
                run_markdown('## This is an h2 tag'),
                '<h2>This is an h2 tag</h2>')
    
    def test_h3(self):
        '''
        Lines beginning with three '#' should become 'h3' tags
        '''
        self.assertEqual(
               run_markdown('### This is an h3 tag'),
                '<h3>This is an h3 tag</h3>')
    
    def test_header_whitespace(self):
        '''
        Header '#' declarations should strip extraneous whitespace in line
        '''
        self.assertEqual(
                run_markdown('#        extra   space     '),
                '<h1>extra   space</h1>')
    
    def test_blockquote(self):
        '''
        Blockquote '>' declarations should convert to <blockquote> tags
        '''
        self.assertEqual(
                run_markdown('> a\n> b\n> c\n'),
                '<blockquote><p>a</p>\n<p>b</p>\n<p>c</p>\n</blockquote>')

if __name__ == '__main__':
    unittest.main()