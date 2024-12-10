from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

def text_node_to_html_node(text_node):
    match text_node.textType:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.LINK:
            return LeafNode('a', text_node.text, text_node.URL)
        case TextType.IMAGE:
            return LeafNode('img', "", {"src": f"{text_node.URL}", "alt": f"{text_node.text}"})
        case _:
            raise ValueError("invalid type")


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, textType, URL = None):
        self.text = text
        if textType not in TextType:
            raise ValueError(f"{textType} is not a valid TextType")
        else:
            self.textType = TextType(textType)
        self.URL = URL
    def get_tag(self):
        match self.textType:
            case TextType.TEXT:
                return None
            case TextType.BOLD:
                return "b"
            case TextType.ITALIC:
                return "i"
            case TextType.CODE:
                return "code"
            case TextType.IMAGE:
                return "img"
            case TextType.LINK:
                return "a"
            case _:
                raise Exception("TextNode.get_tag called incorrectly.")
            
    def get_props(self):
        match self.textType:
            case TextType.TEXT:
                return None
            case TextType.BOLD:
                return None
            case TextType.ITALIC:
                return None
            case TextType.CODE:
                return None
            case TextType.IMAGE:
                #return f'src="{self.URL}" alt="{self.text}"'
                return {"src": f"{self.URL}", "alt": f"{self.text}"}
            case TextType.LINK:
                #return f'href="url"'
                return {"href": f"{self.URL}"}
            case _:
                raise Exception("TextNode.get_tag called incorrectly.")
                
    def __eq__(self, other):
        if self.text == other.text and self.textType == other.textType and self.URL == other.URL:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.textType.value}, {self.URL})"
