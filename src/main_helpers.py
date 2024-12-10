import os
import shutil
from pathlib import Path
from convert import markdown_to_html_node

def copy_recursive(source, destination):
    for item in os.listdir(source):
        src_item_path = os.path.join(source, item)
        dst_item_path = os.path.join(destination, item)
        if os.path.isdir(src_item_path):
            os.mkdir(dst_item_path)
            copy_recursive(src_item_path, dst_item_path)
        else:
            print(f"Copying {src_item_path} to {dst_item_path}")
            shutil.copy(src_item_path, dst_item_path)

def copyStatic(source, destination):
    if os.path.exists(destination):
        print("public directory existed - is now deleted")
        shutil.rmtree(destination)
    os.mkdir(destination)
    copy_recursive(source, destination)

def extract_title(markdown):
    for line in markdown.split("\n"):
        isThisHash = line.split(" ")
        if isThisHash[0] == "#":
            return line[2:]
        else:
            raise Exception("Markdown must contain h1 heading")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    #Read the markdown file at from_path and store the contents in a variable.
    dest_path = Path(dest_path)
    scrFile = Path(from_path).read_text()
    template = Path(template_path).read_text()
    html = markdown_to_html_node(scrFile).to_html()
    title = extract_title(scrFile)
    output_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    dest_path.parent.mkdir(parents=True, exist_ok=True)  # Create directories if needed
    dest_path.write_text(output_html, encoding='utf-8')  # Write content directly