#from ? import ?

def block_to_block_type(block):
    lines = block.split("\n")
    isQuote = None
    isUnLst = None
    isOrLst = None
    if len(lines) == 1:
        testString = block.split(" ", 1)
        match testString[0]:
            case "#":
                return "h1"
            case "##":
                return "h2"
            case "###":
                return "h3"
            case "####":
                return "h4"
            case "####":
                return "h4"
            case "#####":
                return "h5"
            case "######":
                return "h6"
            case _:
                pass
    if block[:3] == block[-3:]:
            if block[0] == "`":
                return "code"
    for line in lines:
        if line[0] != ">":
            isQuote = False
            break
        if line[0] == ">":
            isQuote = True
    if isQuote:
        return "quote"
    for line in lines:
        if line[:2] == "- " or  line[:2] == "* ":
            isUnLst = True
            continue
        if line[:2] != "- " or line[:2] != "* ":
            isUnLst = False
            break
        
    if isUnLst:
        return "unordered_list"
    for i, line in enumerate(lines):
        j = i + 1
        if line[:3] == f"{j}. ":
            isOrLst = True
            continue
        if line[:3] != f"{j}. ":
            isOrLst = False
            break
        
    if isOrLst:
        return "ordered_list"
    return "p"

    
        

def markdown_to_blocks(markdown):
    blocks = []
    blocks = markdown.split("\n\n")
    blocks = list(filter(None, blocks))
    for block in blocks:
        block = block.strip()
    return blocks
    
    