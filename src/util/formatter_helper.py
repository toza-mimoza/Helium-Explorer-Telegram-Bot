from telegram.constants import ParseMode


def _code_block(text, code_lang: str = None, parse_mode = ParseMode.MARKDOWN):
    if(parse_mode == ParseMode.MARKDOWN or parse_mode == ParseMode.MARKDOWN_V2):
        return '```'+text+'```'
    elif(parse_mode == ParseMode.HTML):
        if(code_lang):
            return f'<pre><code class="language-{code_lang.lower()}">'+text+'</code></pre>'
        return f'<pre><code>'+text+'</code></pre>'

def _it(text, parse_mode = ParseMode.MARKDOWN):
    if(parse_mode == ParseMode.MARKDOWN or parse_mode == ParseMode.MARKDOWN_V2):
        return '_'+text+'_'
    elif(parse_mode == ParseMode.HTML):
        return '<i>'+text+'</i>'

def _bit(text, parse_mode = ParseMode.MARKDOWN):
    if(parse_mode == ParseMode.MARKDOWN or parse_mode == ParseMode.MARKDOWN_V2):
        return '*_'+text+'_*'
    elif(parse_mode == ParseMode.HTML):
        return '<i><b>'+text+'</b></i>'


def _b(text, parse_mode = ParseMode.MARKDOWN):
    if(parse_mode == ParseMode.MARKDOWN or parse_mode == ParseMode.MARKDOWN_V2):
        return '*'+text+'*'
    elif(parse_mode == ParseMode.HTML):
        return '<b>'+text+'</b>'

def _st(text, parse_mode = ParseMode.MARKDOWN):
    if(parse_mode == ParseMode.MARKDOWN or parse_mode == ParseMode.MARKDOWN_V2):
        return '~'+text+'~'
    elif(parse_mode == ParseMode.HTML):
        return '<s>'+text+'</s>'

def _ul(text, parse_mode = ParseMode.MARKDOWN):
    if(parse_mode == ParseMode.MARKDOWN or parse_mode == ParseMode.MARKDOWN_V2):
        return '__'+text+'__'
    elif(parse_mode == ParseMode.HTML):
        return '<u>'+text+'</u>'
        

def escape(text):
    return str(text).replace(".", "\.").replace("_", "\\_").replace("*", "\\*").replace("[", "\\[").replace("`", "\\`").replace('-', '\\-').replace('(', '\\(').replace(')', '\\)')