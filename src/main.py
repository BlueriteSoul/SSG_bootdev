from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_link, split_nodes_image, text_to_textnodes
from block import markdown_to_blocks, block_to_block_type
from convert import markdown_to_html_node
from main_helpers import copyStatic, generate_pages_recursive


    


def main():
    copyStatic("static", "public")
    generate_pages_recursive("content", "template.html", "public")


main()