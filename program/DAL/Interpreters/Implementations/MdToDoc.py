from dataclasses import dataclass
from program.Utils import MDHelper as md
from program.DLL import Doc
from typing import List, Tuple
import re

def parse(md_string):
    return _parse_markdown(md_string)


# WARNING. this function is recursive
# Creates a new DOC and remove its contents from the existing string (do NOT remove the children) 
def _create_doc( type : md.MD_TYPE, text : str ) -> Tuple[Doc, str]:
    (content, remainder) = md.extract_content(type, text)
    doc = Doc(
        linkId= type.name,
        type = type.name,
        text = content,
        content=[],
        children = []
    )
    
    if type.process_content and len(content) > 0:
        doc.content = _get_all_children(0, doc.text)
    
    if len(remainder) > 0:
        (doc.children, remainder) = _get_all_children(type.level, remainder)
    
    return (doc, remainder)


# WARNING. this function is recursive.
def _get_all_children(current_depth : int, text : str) -> Tuple[List[Doc], str]:
    
    children, remainder = [], text 
    last_computed_len = -1
    
    while len(remainder) > 0 and len(remainder) != last_computed_len:
        comp = md.get_next_component(remainder)
            
        if comp.level <= current_depth:
            break
        
        (doc, rem) = _create_doc(comp, remainder)
        
        children.append( doc )
        last_computed_len = len(remainder)
        remainder = rem
    
    return (children, remainder)
    
    

def _parse_markdown(text):
    (docs, remainder) = _get_all_children(0, text)
    
    if len(remainder) != 0:
        raise (f"A unkown problem has occured. unable to process the remainder of the .md file (MdToDoc.py): \n\"{remainder}\"")
    
    return docs
    
    
    
    
    
    
    
# @dataclass
# class MD_TYPE:
#     identifier : str
#     name: str
#     priority: int
#     end_on: List[str]
#     process_content : bool = False

# # .|\n|$ = anything
# # (^|\n) = start of the string or new line
# # (\n|$) = new line or end of the string
# # (\n|^) {0,3} = new line or start of the string, Followed by a maximum of 3 spaces

# MD_TYPES = [
#     MD_TYPE(r"(^|\n)#", "h1", 1,                [] ),
#     MD_TYPE(r"(^|\n) *---[ \t]*\n", "br", 1,  [r".|\n|$"] ), # [ \t]* = any number of spaces or tabs 
#     MD_TYPE(r"(^|\n)##", "h2", 2,           [r"\n"] ),
#     MD_TYPE(r"(^|\n)###", "h3", 3,          [r"\n"] ),
#     MD_TYPE(r"(^|\n)####", "h4", 4,         [r"\n"] ),
#     MD_TYPE(r"(^|\n)#####", "h5", 5,        [r"\n"] ),
#     MD_TYPE(r"(^|\n)######", "h6", 6,       [r"\n"] ),
    
#     MD_TYPE(r"(^|\n)> ", "callout", 7,      [r"\n[ \t]*\n"] ), # [ \t]* = any number of spaces or tabs 
#     MD_TYPE(r"(^|\n)```", "code-block", 7,         [r"\n```\n"]),
    
#     MD_TYPE(r"(^|\n)\d+\. ", "oi", 8,        [r"\n"]),
#     MD_TYPE(r"(^|\n)- ", "ui", 8,           [r"\n"]),
    
#     MD_TYPE(r"(?<=^|\n)( {4,7}|\t)", "indent", 8, []), # (?<=^|\n) = Only if PREceded by sapace, tab or \n
#     MD_TYPE(r"(^|\n)(?! {4}|\t)", "p", 8,      [r"\n[ \t]*\n"]),  # [ \t]* = any number of spaces or tabs 
    
#     MD_TYPE(r"<\w", "tag", 8, [r">"]), 
#     MD_TYPE(r"<\\\w", "closing-tag", 8, [r">"]), 
#     MD_TYPE(r"(^|\n\n)(\|[^\n\|]*)+\| *\n(\|[ -]*)+\| *(\n|$)", "table", 8, []), 
#     MD_TYPE(r"(^|\n)!\[\[(?=[^\n]*(\]\]) *\n+)", "expanded-link", 8,     []), # (?=[^\n]*(\]\]) *\n+) = Only if PROceded by: anything_but_a_newline + ]] + (optional) space + \n
    
#     MD_TYPE(r"\*\*(?! |\t|\n)", "b", 9,  [r"(?<! |\t|\n)\*\*"]), # (?! |\t|\n) = Only if not PROceded by sapace, tab or \n
#     MD_TYPE(r"\*(?! |\t|\n)", "i", 9,    [r"(?<! |\t|\n)\*"]), # (?<! |\t|\n) = Only if not PREceded by space, tab or \n 
#     MD_TYPE(r"~~", "cut", 9,        [r"~~"]),  
#     MD_TYPE(r"==", "highlight", 9,     [r"=="]), 
#     MD_TYPE(r"\[\[", "link", 9,     [r"\]\]"]), 
#     MD_TYPE(r"\[\^", "footnote", 9, [r"\]"]), 
#     MD_TYPE(r"`", "code", 9, [r"`", r"\n"]), 
    
# ]