import re
from textnode import *

def text_to_textnodes(text):
    nodes = []
    nodes = split_nodes_delimiter([TextNode(text, "text", None)], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    return nodes


def extract_markdown_images(text):
    matchesImage = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matchesImage

def extract_markdown_links(text):
    matchesLink = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matchesLink

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.textType != TextType.TEXT:
            result.append(node)
            continue
        extractedImgs = extract_markdown_images(node.text)
        if not extractedImgs:
            result.append(node)
            continue
        
        currentText = node.text
        for altText, url in extractedImgs:
            markdown = f"![{altText}]({url})"
            parts = currentText.split(markdown, 1)
            if parts[0] == "":
                result.append(TextNode(altText, TextType.IMAGE, url))
                currentText = parts[1]
                continue
            result.append(TextNode(parts[0], TextType.TEXT))
            result.append(TextNode(altText, TextType.IMAGE, url))
            currentText = parts[1]
        if currentText != "":
            result.append(TextNode(currentText, TextType.TEXT))
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.textType != TextType.TEXT:
            result.append(node)
            continue
        extractedLinks = extract_markdown_links(node.text)
        if not extractedLinks:
            result.append(node)
            continue
        
        currentText = node.text
        for altText, url in extractedLinks:
            markdown = f"[{altText}]({url})"
            parts = currentText.split(markdown, 1)
            if parts[0] == "":
                result.append(TextNode(altText, TextType.LINK, url))
                currentText = parts[1]
                continue
            result.append(TextNode(parts[0], TextType.TEXT))
            result.append(TextNode(altText, TextType.LINK, url))
            currentText = parts[1]
        if currentText != "":
            result.append(TextNode(currentText, TextType.TEXT))
    return result

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.textType != TextType.TEXT:
            result.append(node)
            continue
        parts = node.text.split(delimiter)  

        if len(parts) %2==0:
            raise ValueError("Unmatched delimiter in text")
        
        for i, part in enumerate(parts):
            if i % 2 == 0:
                if part == "":
                    continue
                result.append(TextNode(part,TextType.TEXT))
            else:                
                result.append(TextNode(part,text_type))


    return result

