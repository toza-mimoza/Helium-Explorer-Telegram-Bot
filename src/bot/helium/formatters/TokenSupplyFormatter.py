from telegram.constants import ParseMode

from util.exceptions import InvalidParseMode

from util.formatter_helper import _ul, escape
from util.constants import MsgLabelsMD, MsgLabelsHTML

class TokenSupplyFormatter:
    
    def get_message(raw_response, parse_mode = ParseMode.MARKDOWN):
        # format the message here
        data = raw_response['data']
        token_supply = data['token_supply']

        title_md=_ul('Token Supply')         
        title_html = _ul('Token Supply', ParseMode.HTML)

        if(parse_mode == ParseMode.MARKDOWN):

            # format the message here
            
            markdown_message = f'''{title_md}
    {MsgLabelsMD.TOKEN_SUPPLY}: {token_supply}
    '''
            return markdown_message 
        
        if(parse_mode == ParseMode.MARKDOWN_V2):
            # format the message here
            
            markdownv2_message = f'''{title_md}
    {MsgLabelsMD.TOKEN_SUPPLY}: {escape(token_supply)}
    
    '''
            return markdownv2_message 

        elif(parse_mode == ParseMode.HTML):
            # if markdown
            html_message = f'''
                    {title_html}
            {MsgLabelsHTML.TOKEN_SUPPLY}: {token_supply}
            
           '''
            return html_message
        else:
            raise InvalidParseMode('Invalid parse_mode specified!')