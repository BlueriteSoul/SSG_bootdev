import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.LINK, "mama.com")
        node2 = TextNode("This is a text node", TextType.LINK, "mama.com")
    def test_eq3(self):
        node = TextNode("This is a(){} text node", TextType.CODE, "mama.com")
        node2 = TextNode("This is a(){} text node", TextType.CODE, "mama.com")
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "evil.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text nosde", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_not_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text nosde", TextType.IMAGE)
        self.assertNotEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test1(self):
        tn1 = TextNode("Slightly less serious test", "text")
        self.assertEqual(text_node_to_html_node(tn1).to_html(), "Slightly less serious test")
    def test2(self):
        tn2 = TextNode("Second serious test", "bold")
        self.assertEqual(text_node_to_html_node(tn2).to_html(), "<b>Second serious test</b>")
    def test3(self):
        with self.assertRaises(ValueError):
            tn2 = TextNode("Second serious test", "lilatic")
            print(tn2)
    def test4(self):
        tn3 = TextNode("Third serious test", "italic")
        self.assertEqual(text_node_to_html_node(tn3).to_html(), "<i>Third serious test</i>")
    def test5(self):
        tn4 = TextNode("Fourth serious test", "code")
        self.assertEqual(text_node_to_html_node(tn4).to_html(), "<pre><code>Fourth serious test</code></pre>")
    def test6(self):
        tn5 = TextNode("Fifth serious test", "image", "obrazek.com")
        self.assertEqual(text_node_to_html_node(tn5).to_html(), '<img src="obrazek.com" alt="Fifth serious test"></img>')

if __name__ == "__main__":
    unittest.main()