import json

def _code_block(text):
    return '```\n'+text+'\n```'

def _it(text):
    return '*'+text+'*'

def _b(text):
    return '**'+text+'**'

def _h1(text):
    return '# '+text

def _h2(text):
    return '## '+text

def _h3(text):
    return '### '+text

def _h4(text):
    return '#### '+text

def _h5(text):
    return '##### '+text

def _h6(text):
    return '##### '+text

def get_human_readable_text(resp):
    '''
    Function for retrieving human readable text from request response.
    '''
    result = ''
    d = resp['data']

    for key in d:
        result += str(key) + ' -> ' + str(d[key]) + '\n'
    return _code_block(result)
    
