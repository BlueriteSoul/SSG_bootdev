from block import *
from htmlnode import *
from inline import *

def blockToTextValue(text, tag):
    match tag:
        case "h1":
            return text[2:]
        case "h2":
            return text[3:]
        case "h3":
            return text[4:]
        case "h4":
            return text[5:]
        case "h5":
            return text[6:]
        case "h6":
            return text[7:]
        case "code":
            returnText = text[3:-3]
            return returnText
        case "quote":
            lines = text.split("\n")
            returnText = ""
            for line in lines:
                returnText += line[2:]
            return returnText
        case _:
            raise Exception("Error in blockToTextValue conver.py")


def textToChildrenUnList(text):
    lines = text.split("\n")
    returnList = []
    for line in lines:
        textNodesInLine = text_to_textnodes(line[2:])
        leafList = []
        for textnode in textNodesInLine:
            leafList.append(LeafNode(textnode.get_tag(), textnode.text))
        returnList.append(ParentNode("li", leafList))
    return returnList

def textToChildrenOrList(text):
    lines = text.split("\n")
    returnList = []
    for line in lines:
        textNodesInLine = text_to_textnodes(line[3:])
        leafList = []
        for textnode in textNodesInLine:
            leafList.append(LeafNode(textnode.get_tag(), textnode.text))
        returnList.append(ParentNode("li", leafList))
    return returnList


def textToChildren(text):
    textNodes = text_to_textnodes(text)
    returnNodes = []
    for node in textNodes:
        if node.textType == TextType.IMAGE:
            returnNodes.append(LeafNode(node.get_tag(), "", node.get_props()))
            continue
        returnNodes.append(LeafNode(node.get_tag(), node.text, node.get_props()))
    return returnNodes
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html = []
    for block in blocks:
        blockTag = block_to_block_type(block)
        match blockTag:
            case "h1":
                html.append(LeafNode(blockTag, blockToTextValue(block, blockTag)))                
            case "h2":
                html.append(LeafNode(blockTag, blockToTextValue(block, blockTag)))
            case "h3":
                html.append(LeafNode(blockTag, blockToTextValue(block, blockTag)))
            case "h4":
                html.append(LeafNode(blockTag, blockToTextValue(block, blockTag)))
            case "h5":
                html.append(LeafNode(blockTag, blockToTextValue(block, blockTag)))
            case "h6":
                html.append(LeafNode(blockTag, blockToTextValue(block, blockTag)))
            case "code":                
                html.append(ParentNode("pre", [LeafNode(blockTag, blockToTextValue(block, blockTag))]))
            case "quote":
                html.append(LeafNode("blockquote", blockToTextValue(block, blockTag)))
            case "p":
                html.append(ParentNode(blockTag, textToChildren(block)))
            case "unordered_list":
                html.append(ParentNode("ul", textToChildrenUnList(block)))
            case "ordered_list":
                html.append(ParentNode("ol", textToChildrenOrList(block)))
    #print(html)
    return ParentNode("div", html)
