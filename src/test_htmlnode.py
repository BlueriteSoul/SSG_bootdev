import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "Click here.", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    def test_props_to_html2(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    def test_props_to_html3(self):
        node = HTMLNode(None, None, None, {"src": "string representing source text", "height": "500px"})
        self.assertEqual(node.props_to_html(), ' src="string representing source text" height="500px"')

class TestLeafNode(unittest.TestCase):
    def test_leafNode_to_html(self):
        node = LeafNode("a", "Click here.", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click here.</a>')
    def test_leafNode_to_html2(self):
        node = LeafNode(None, "Click here.", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), 'Click here.')

class TestParentNode(unittest.TestCase):
    def test_parentNode_to_html(self):
        node = ParentNode("p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    def test_parentNode_to_html2(self):
        node = ParentNode("h1", [ParentNode("h2", [ParentNode("h3", [ParentNode("h4", [ParentNode("h5", [ParentNode("p", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ])])])])])])
        self.assertEqual(node.to_html(), '<h1><h2><h3><h4><h5><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></h5></h4></h3></h2></h1>')


if __name__ == "__main__":
    unittest.main()