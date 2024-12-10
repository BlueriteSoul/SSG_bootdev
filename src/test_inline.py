import unittest

from inline import *


class TestSplitNodesDelimiter(unittest.TestCase):
    def test1(self):
        node = TextNode("This is` text with a` code block word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(result), "[TextNode(This is, text, None), TextNode( text with a, code, None), TextNode( code block word, text, None)]")

    def test2(self):
        node = TextNode("`This is` text with a code block word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(result), "[TextNode(This is, code, None), TextNode( text with a code block word, text, None)]")

    def test3(self):
        node = TextNode("`This is` text with a code block word", TextType.TEXT)
        node2 = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        result = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        #print(result)
        self.assertEqual(str(result), "[TextNode(`This is` text with a code block word, text, None), TextNode(This is text with a , text, None), TextNode(bolded phrase, bold, None), TextNode( in the middle, text, None)]")

    def test4(self):
        node = TextNode("`This is` text with a code block word", TextType.TEXT)
        node2 = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        result = split_nodes_delimiter([node, node2], "`", TextType.CODE)
        #print(result)
        self.assertEqual(str(result), "[TextNode(This is, code, None), TextNode( text with a code block word, text, None), TextNode(This is text with a **bolded phrase** in the middle, text, None)]")

    def test5(self):
        node = TextNode("This is code block: `code here``more code here`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)        
        #print(result)
        self.assertEqual(str(result), "[TextNode(This is code block: , text, None), TextNode(code here, code, None), TextNode(more code here, code, None)]")

class TestExtract(unittest.TestCase):
    def test1img(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
    
    def test1link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

class TestLinkSplit(unittest.TestCase):
    def test_split_nodes_link_basic(self):
        node = TextNode("Hello [world](https://example.com)!", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(str(result), "[TextNode(Hello , text, None), TextNode(world, link, https://example.com), TextNode(!, text, None)]")

    def test_split_nodes_link_empty(self):
        node = TextNode("[world](https://example.com)", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(str(result), "[TextNode(world, link, https://example.com)]")

    def test_split_nodes_link_multiple(self):
        node = TextNode(
            "This has [two](url1) different [links](url2)", 
            TextType.TEXT
        )
        result = split_nodes_link([node])
        self.assertEqual(str(result), "[TextNode(This has , text, None), TextNode(two, link, url1), TextNode( different , text, None), TextNode(links, link, url2)]")

    def test_split_nodes_link_no_links(self):
        node = TextNode("Hello world!", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(str(result), "[TextNode(Hello world!, text, None)]")

    def test_split_nodes_with_multiple_nodes(self):
        node = TextNode("Hello world!", TextType.TEXT)
        node2 = TextNode("[world](https://example.com)", TextType.TEXT)
        result = split_nodes_link([node, node2])
        self.assertEqual(str(result), "[TextNode(Hello world!, text, None), TextNode(world, link, https://example.com)]")

class TestImageSplit(unittest.TestCase):
    def test_split_nodes_image_basic(self):
        node = TextNode("Hello ![world](https://example.com/img.png)!", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(str(result), "[TextNode(Hello , text, None), TextNode(world, image, https://example.com/img.png), TextNode(!, text, None)]")

    def test_split_nodes_image_empty(self):
        node = TextNode("![world](https://example.com/img.png)", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(str(result), "[TextNode(world, image, https://example.com/img.png)]")

    def test_split_nodes_image_multiple(self):
        node = TextNode("This has ![two](url1.png) different ![images](url2.png)", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(str(result), "[TextNode(This has , text, None), TextNode(two, image, url1.png), TextNode( different , text, None), TextNode(images, image, url2.png)]")

    def test_split_nodes_image_no_images(self):
        node = TextNode("Hello world!", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(str(result), "[TextNode(Hello world!, text, None)]")

    def test_split_nodes_image_with_multiple_nodes(self):
        node = TextNode("![world](https://example.com/img.png)", TextType.TEXT)
        node2 = TextNode("Hello world!", TextType.TEXT)
        result = split_nodes_image([node, node2])
        self.assertEqual(str(result), "[TextNode(world, image, https://example.com/img.png), TextNode(Hello world!, text, None)]")

class TestTextToNodes(unittest.TestCase):
    def test(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(nodes, [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
])

if __name__ == "__main__":
    unittest.main()