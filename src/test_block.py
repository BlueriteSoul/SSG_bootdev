import unittest

from block import *


class TestSplitBlocks(unittest.TestCase):
    def test1(self):
        input = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item'''
        blocks = markdown_to_blocks(input)
        #print(blocks)
        self.assertEqual(str(blocks), "['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\\n* This is a list item\\n* This is another list item']")

class TestBlockToBlockType(unittest.TestCase):
    def test_hedingss(self):
        input1 = "# This is a heading h1"
        input2 = "## This is a heading h2"
        input3 = "### This is a heading h3"
        input4 = "#### This is a heading h4"
        input5 = "##### This is a heading h5"
        input6 = "###### This is a heading h6"
        input7 = "####### This is a paragraph"
        blockType = []
        for input in [input1, input2, input3, input4, input5, input6, input7]:
            blockType.append(block_to_block_type(input))
        self.assertEqual(str(blockType), "['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']")

    def test_quote(self):
        input1 = """> This is a quote
> on multiple lines"""
        input2 = """> This starts like a quote
but actuallly its a paragraph"""
        blockType = []
        for input in [input1, input2]:
            blockType.append(block_to_block_type(input))
        self.assertEqual(str(blockType), "['quote', 'p']")

    def test_code(self):
        input1 = """```this is code
correct code```"""
        input2 = """```not code
starts with 3backtiks"""
        input3 = """not code
ends with 3 backticks```"""
        blockType = []
        for input in [input1, input2, input3]:
            blockType.append(block_to_block_type(input))
        self.assertEqual(str(blockType), "['code', 'p', 'p']")

    def test_un_lst(self):
        input1 = """- one item
- two item"""
        input2 = """* 1 item
* 2 item"""
        input3 = """* should
- work"""
        blockType = []
        for input in [input1, input2, input3]:
            blockType.append(block_to_block_type(input))
        self.assertEqual(str(blockType), "['unordered_list', 'unordered_list', 'unordered_list']")

    def test_or_lst(self):
        input1 = """1. one item
2. two item"""
        input2 = """2. 1 item
3. 2 item"""
        input3 = """ should
- work"""
        blockType = []
        for input in [input1, input2, input3]:
            blockType.append(block_to_block_type(input))
        self.assertEqual(str(blockType), "['ordered_list', 'p', 'p']")