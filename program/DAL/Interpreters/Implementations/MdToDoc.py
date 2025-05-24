

def parse(md_string):
    return _parse_markdown(md_string)
    
# GERADO USANDO IA
# TA UMA MERDA PUTA QUE PARIU QUE BICHO BURRO DA PORRA
# VOU TER QUE FAZER NA MÃO
def _parse_markdown(lines):
    root = {}
    stack = [(0, root)]  # (level, current_dict)

    for line in lines:
        stripped = line.strip()
        if not stripped.startswith('#'):
            continue

        # Determine the header level
        level = len(stripped.split(' ')[0])
        header_text = stripped[level:].strip()

        # Create new nested dict for this header
        new_dict = {}

        # Pop from the stack until we find the correct parent level
        while stack and stack[-1][0] >= level:
            stack.pop()

        # Insert into the parent dictionary
        parent_level, parent_dict = stack[-1]
        parent_dict[header_text] = new_dict

        # Push the new dict to the stack
        stack.append((level, new_dict))

    return root
