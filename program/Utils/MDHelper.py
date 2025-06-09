from dataclasses import dataclass
from typing import List, Tuple
import re

# _________________________________________________________________________________________________ DATA CLASS
@dataclass
class MD_TYPE:
    identifier : str
    name: str
    level: int # Level in the doc hierarchy
    end_on: List[str]
    priority : int = 0
    process_content : bool = False # Tells if the content of this entry should be processed as a md string
    




# _________________________________________________________________________________________________ REGEX HELPERS
spaces = r"[ \t]*"          # regex for any number of spaces
tab = r"( {4,7}|\t)"        # regex that captures 1 set of spaces or \t
next_char = r".|\n|$"       # regex that match any character

ln_start = r"(\n|^)"        # regex for a new line OR the start of the string
ln_end = spaces + r"(\n|\Z)" # regex for a line end OR the end of a string

# proceded_by     = lambda *args: "|".join([ f"(?={x})" for x in args])    # Uses regex to lookahead without actualy capturing the element
# not_proceded_by     = lambda *args: "|".join([ f"(?=!{x})" for x in args])    # Uses regex to lookahead without actualy capturing the element
# preceded_by     = lambda *args: "|".join([ f"(?<={x})" for x in args])    # Uses regex to lookahead without actualy capturing the element
# not_preceded_by     = lambda *args: "|".join([ f"(?<!{x})" for x in args])    # Uses regex to lookahead without actualy capturing the element


proceded_by     = lambda *args: r"(?=" + "|".join(args) + ")" # Uses regex to lookahead without actualy capturing the element
not_proceded_by = lambda *args: r"(?=!" + "|".join(args) + ")"
preceded_by     = lambda *args: r"(?<=" + "|".join(args) + ")" 
not_preceded_by = lambda *args: r"(?<!" + "|".join(args) + ")"
no_capture = lambda *args: r"(?:" + "|".join(args) + ")"

proceded_by     = lambda *args: r"(?=" + "|".join(args) + ")" # Uses regex to lookahead without actualy capturing the element
not_proceded_by = lambda *args: r"(?=!" + "|".join(args) + ")"
preceded_by     = lambda *args: r"(?<=" + "|".join(args) + ")" 
not_preceded_by = lambda *args: r"(?<!" + "|".join(args) + ")"
no_capture = lambda *args: r"(?:" + "|".join(args) + ")"


obsidian_table_regex = r"(^|\n\n|^\n)" + r"(\|[^\n\|]*)+\| *\n" + r"(\|[ -]*)+\| *\n?" + r"((\|[^\n\|]*)+\| *\n)*" + r"(\n|\Z)"
    #   (^|\n\n|^\n)            => double new lines 
    #   (\|[^\n\|]*)     => any number of texts surrounded by '|'. Exemple: "|some | text |"
    #   +\| *\n                  => an extra trailing "| \n" .
    #   (\|[ -]*)        => a new line with "---" separated by '|'
    #   \| *(\n|\Z)        => an extra trailing "| \n" or the end of the string 





# _________________________________________________________________________________________________ AVAILABLE TYPES

MD_TYPES = [
    MD_TYPE( ln_start + "# ", "h1", 1,            [ln_end] ),
    MD_TYPE( ln_start + "## ", "h2", 2,           [ln_end] ),
    MD_TYPE( ln_start + "### ", "h3", 3,          [ln_end] ),
    MD_TYPE( ln_start + "#### ", "h4", 4,         [ln_end] ),
    MD_TYPE( ln_start + "##### ", "h5", 5,        [ln_end] ),
    MD_TYPE( ln_start + "###### ", "h6", 6,       [ln_end] ),
    
    MD_TYPE( ln_start + spaces + "---" + spaces + "\n", "br", 7,  [ln_end] ),
    MD_TYPE(ln_start + "> ", "callout", 7,      [r"\n" + ln_end] ),  
    MD_TYPE(ln_start + "```", "code-block", 7,  [r"\n```" + ln_end ]),
    
    MD_TYPE(ln_start + r"\d+\. ", "oi", 8,       ["^"]),
    MD_TYPE(ln_start + "- ", "ui", 8,           ["^"]),
    
    MD_TYPE( "<" + proceded_by(r"\w") ,      "tag", 8,           [r">", r"\\>"]), 
    MD_TYPE(r"<\\" + proceded_by(r"\w") ,    "closing-tag", 8,   [r">"]), 
    MD_TYPE( ln_start + spaces + r"!\[\[", "expanded-link", 8,  [r"\]\]" + ln_end]),
    MD_TYPE(obsidian_table_regex , "table", 8, ["^"] ),
    
    # Usar o proceded_by em vez do ln_start neste caso faz a regex não capturar a quebra de linha, 
    # ou seja, captura somente o tab e permite que a quebra de linha seja consumida na proxima iteração
    # process_content = True é importante para permitir que uma indentação possa possuir outra indentação como filho
    MD_TYPE(ln_start + tab, "indent", 8, [ln_end], 0,  True),
     
    # priority so it doesnt conflict with italic (i)
    MD_TYPE(r"\*\*" + not_proceded_by(' ',r'\t|\n'), "b", 9,  [ not_preceded_by(' ', r"\t|\n") + r"\*\*"], 1 ),    # not preceded/proceded by sapace, tab or \n
    MD_TYPE(r"\*\*" + not_proceded_by(' ',r'\t|\n'), "i", 9,  [ not_preceded_by(' ', r"\t|\n") + r"\*"] ),      # not preceded/proceded by sapace, tab or \n
    MD_TYPE(r"~~", "cut", 9,        [r"~~"]),  
    MD_TYPE(r"==", "highlight", 9,     [r"=="]), 
    MD_TYPE(r"\[\[", "link", 9,     [r"\]\]"]), 
    MD_TYPE(r"\[\^", "footnote", 9, [r"\]"]), 
    MD_TYPE(r"`", "code", 9, [r"`", r"\n"]), 
    
    # priority -1 and the "[\n]+" (not ln_end) ensures that this will just consume the \n without interfering with the other components
    MD_TYPE(ln_start + proceded_by(r"[^\s][^\n]*" + "[\n]+"), "p", 8, [ln_end], -1),
]




# _________________________________________________________________________________________________ UTIL METHODS
def _get_best(a : Tuple[int, MD_TYPE], b : Tuple[int, MD_TYPE]) ->Tuple[int, MD_TYPE]:
    return (
        a if a[0] < b[0] else
        b if a[0] > b[0] else
        a if a[1].priority > b[1].priority else
        b
    )
    
def _get_default_component(current_best : Tuple[int, MD_TYPE]):
    end_idx = f"{current_best[0]}"
    return MD_TYPE(r"^", "txt", 9, [r"^(.|\n){1,"+ end_idx +"}"]) 

def _get_terminator(offset: int, t : MD_TYPE, text : str):
     
    # ignores the text in the offset.
    # this is used so that the terminator and initializer dont overlap
    ignore_start = text[offset:] 
    
    # Loop through the terminators to find the suitable one
    terminator = re.search(r"\Z", ignore_start) 
    best = terminator.start()
    for t in t.end_on:
        temp = re.search(t, ignore_start) 
        if (not temp):
           next
        if(temp.start() <= best):
            terminator = temp
            best = temp.start()
    
    return terminator
    

def extract_content(t : MD_TYPE, text : str) -> Tuple[str, str]:
    init = re.search(t.identifier, text)
    
    if (not init):
        raise(f"A unexpected problem has occured on creating doc with type '{t.name}' while parsing indentifier regex\n\t using indentifier regex :\n\t\t\"{t.identifier}\" \n\t using terminator regex(s):\n\t\t\""+ "\n\t\t".join(t.end_on) + f"\n\t on string:\n\t\"{text}\"")
    
    if init.start() != 0:
        print(f"\n\n ERROR \n\n o componente {t} não inicia no indice 0. ele é antecedido por: {text[init.start():]}")
    
    # This is used so that the terminator and initializer dont overlap
    _offset = init.end()
    terminator = _get_terminator(init.end(), t, text)
    
    # Finds where the split should happend
    # But back the offset removed by _get_terminator(offset , a, b)
    start_split = _offset + terminator.start(); 
    end_split = _offset + terminator.end(); 
    
    
    content = re.sub( t.identifier, "", text[:start_split] )
    remainder = text[end_split:]
    return content.strip() , remainder.strip()


def get_next_component(text : str) -> MD_TYPE:
    current_best = (len(text), None)
    
    for type in MD_TYPES:
        match = re.search(type.identifier, text)
        if not match :
            continue
        
        current_best = _get_best(current_best, (match.start(), type) )
        
    if(current_best[0] != 0):
        return _get_default_component(current_best)
        
    return current_best[1]