from telegram.constants import ParseMode

from util.exceptions import InvalidParseMode
from util.formatter_helper import _ul, escape
from util.constants import MsgLabelsMD, MsgLabelsHTML
from util.time_helper import get_iso_utc_time_from_posix
class HotspotActivityFormatter:
    
    def get_message(data, parse_mode = ParseMode.MARKDOWN):
        """! Returns formatted single activity as message in either MD, MDv2 or HTML."""
        if(parse_mode == ParseMode.MARKDOWN or parse_mode == ParseMode.MARKDOWN_V2):
            markdown_message = f'''
    {MsgLabelsMD.TYPE}: {data['type']}
    {MsgLabelsMD.ROLE}: {data['role']}
    {MsgLabelsMD.HEIGHT}: {data['height']}
    {MsgLabelsMD.TIME}: {escape(get_iso_utc_time_from_posix(data['time']))}
    '''
            return markdown_message

        elif(parse_mode == ParseMode.HTML):
            # if html
            html_message = f'''
    {MsgLabelsHTML.TYPE}: {data['type']}
    {MsgLabelsHTML.ROLE}: {data['role']}
    {MsgLabelsHTML.HEIGHT}: {data['height']}
    {MsgLabelsMD.TIME}: {escape(get_iso_utc_time_from_posix(data['time']))}
    '''
            return html_message
        else:
            raise InvalidParseMode('Invalid parse_mode specified!')