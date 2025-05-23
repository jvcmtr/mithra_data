

def parse():
    pass
    
# GERADO USANDO IA
def parse_markdown(lines):
    stack = []  # Stack to manage hierarchy
    root = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith('#'):
            level = len(line.split(' ')[0])  # Count '#' for level
            text = line[level:].strip()
            node = {
                "type": f"h{level}",
                "text": text,
                "content": []
            }

            # Find where to insert based on header level
            while stack and stack[-1][0] >= level:
                stack.pop()
            if stack:
                stack[-1][1]["content"].append(node)
            else:
                root.append(node)
            stack.append((level, node))

        else:
            # It's a paragraph
            node = {
                "type": "p",
                "text": line,
                "content": []
            }
            if stack:
                stack[-1][1]["content"].append(node)
            else:
                root.append(node)

    return root