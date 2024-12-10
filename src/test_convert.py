import unittest

#from textnode import TextNode, TextType, text_node_to_html_node
from convert import *


class TestConvert(unittest.TestCase):
    def test_convert1(self):
        markdown = """# Heading1 h1

## Heading h2"""
        html = markdown_to_html_node(markdown)
        print(html)
        #self.assertEqual(node, node2)
        return
    
    def test_convert2(self):
        markdown = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        html = markdown_to_html_node(markdown)
        print(html)
        return
    
    def test_convert3(self):
        markdown = """- one item
- two item"""
        html = markdown_to_html_node(markdown)
        print(html)
        return
    
    def test_convert_definitive(self):
        markdown = """# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

- unordered item 1
- unordered item 2

1. ordered item 1
2. ordered item 2

This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"""
        html = markdown_to_html_node(markdown)
        referenceOutput = """HTMLNode(html, None, [HTMLNode(h1, Heading 1, None, None), HTMLNode(h2, Heading 2, None, None), HTMLNode(h3, Heading 3, None, None), HTMLNode(h4, Heading 4, None, None), HTMLNode(h5, Heading 5, None, None), HTMLNode(h6, Heading 6, None, None), HTMLNode(ul, None, [HTMLNode(li, unordered item 1, None, None), HTMLNode(li, unordered item 2, None, None)], None), HTMLNode(ol, None, [HTMLNode(li,  ordered item 1, None, None), HTMLNode(li,  ordered item 2, None, None)], None), HTMLNode(p, None, [HTMLNode(, This is , None, None), HTMLNode(b, text, None, None), HTMLNode(,  with an , None, None), HTMLNode(i, italic, None, None), HTMLNode(,  word and a , None, None), HTMLNode(code, code block, None, None), HTMLNode(,  and an , None, None), HTMLNode(img, , None, src="https://i.imgur.com/fJRm4Vk.jpeg" alt="obi wan image"), HTMLNode(,  and a , None, None), HTMLNode(a, link, None, href="url")], None)], None)"""
        print(html)
        self.assertEqual(str(html), referenceOutput)