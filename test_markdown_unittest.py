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
                run_markdown('# Big header'),
                '<h1>Big header</h1>')
    
    def test_h2(self):
        '''
        Lines beginning with '##' should become 'h2' tags
        '''
        self.assertEqual(
                run_markdown('## Small Header'),
                '<h2>Small Header</h2>')
    
    def test_h3(self):
        '''
        Lines beginning with '###' should become 'h3' tags
        '''
        self.assertEqual(
               run_markdown('### Tiny Header'),
                '<h3>Tiny Header</h3>')
    
    def test_header_whitespace(self):
        '''
        Header '#' declarations should strip extra whitespaces in line
        '''
        self.assertEqual(
                run_markdown('#          extra   spaces     '),
                '<h1>extra   spaces</h1>')
    
    def test_blockquote(self):
        '''
        Blockquote '>' declarations should convert to <blockquote> tags
        '''
        self.assertEqual(
                run_markdown('> a\n> b\n> c\n'),
                '<blockquote><p>a</p>\n<p>b</p>\n<p>c</p>\n</blockquote>')

if __name__ == '__main__':
    unittest.main()