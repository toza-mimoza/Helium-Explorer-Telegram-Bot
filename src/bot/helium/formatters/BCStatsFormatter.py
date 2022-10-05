from telegram.constants import ParseMode

from util.exceptions import InvalidParseMode
from util.formatter_helper import _ul, escape
from util.constants import MsgLabelsMD, MsgLabelsHTML

class BCStatsFormatter:
    
    def get_message(raw_response, parse_mode = ParseMode.MARKDOWN):
        # format the message here
        data = raw_response['data']
        token_supply = data['token_supply']
        election_times = data['election_times']
        counts = data['counts']
        challenge_counts = data['challenge_counts']
        block_times = data['block_times']
        title_md=_ul('Blockchain statistics')         
        title_html = _ul('Blockchain statistics', ParseMode.HTML)

        if(parse_mode == ParseMode.MARKDOWN):

            # format the message here
            
            markdown_message = f'''{title_md}
    {MsgLabelsMD.TOKEN_SUPPLY}: {token_supply}
    
    {MsgLabelsMD.ELECTION_TIMES}: 
        {MsgLabelsMD.LAST_HOUR}: 
            {MsgLabelsMD.STDDEV}: {election_times['last_hour']['stddev']}
            {MsgLabelsMD.AVG}: {election_times['last_hour']['avg']} 
        {MsgLabelsMD.LAST_DAY}: 
            {MsgLabelsMD.STDDEV}: {election_times['last_day']['stddev']}
            {MsgLabelsMD.AVG}: {election_times['last_day']['avg']} 
        {MsgLabelsMD.LAST_WEEK}: 
            {MsgLabelsMD.STDDEV}: {election_times['last_week']['stddev']}
            {MsgLabelsMD.AVG}: {election_times['last_week']['avg']}
        {MsgLabelsMD.LAST_MONTH}: 
            {MsgLabelsMD.STDDEV}: {election_times['last_month']['stddev']}
            {MsgLabelsMD.AVG}: {election_times['last_month']['avg']}           
            
    {MsgLabelsMD.COUNTS}: 
        {MsgLabelsMD.VALIDATORS}: {counts['validators']}
        {MsgLabelsMD.TRANSACTIONS}: {counts['transactions']}
        {MsgLabelsMD.OUIS}: {counts['ouis']}
        {MsgLabelsMD.HOTSPOTS_ONLINE}: {counts['hotspots_online']}
        {MsgLabelsMD.HOTSPOTS_DATA_ONLY}: {counts['hotspots_dataonly']}
        {MsgLabelsMD.HOTSPOTS}: {counts['hotspots']}
        {MsgLabelsMD.COUNTRIES}: {counts['countries']}
        {MsgLabelsMD.CONSENSUS_GROUPS}: {counts['consensus_groups']}
        {MsgLabelsMD.COINGECKO_PRICE_USD}: {counts['coingecko_price_usd']}
        {MsgLabelsMD.COINGECKO_PRICE_GBP}: {counts['coingecko_price_gbp']}
        {MsgLabelsMD.COINGECKO_PRICE_EUR}: {counts['coingecko_price_eur']}
        {MsgLabelsMD.CITIES}: {counts['cities']}
        {MsgLabelsMD.CHALLENGES}: {counts['challenges']}
        {MsgLabelsMD.BLOCKS}: {counts['blocks']}

    {MsgLabelsMD.CHALLENGE_COUNTS}: 
        {MsgLabelsMD.LAST_DAY}: {challenge_counts['last_day']}
        {MsgLabelsMD.ACTIVE}: {challenge_counts['active']}

    {MsgLabelsMD.BLOCK_TIMES}: 
        {MsgLabelsMD.LAST_HOUR}: 
            {MsgLabelsMD.STDDEV}: {block_times['last_hour']['stddev']}
            {MsgLabelsMD.AVG}: {block_times['last_hour']['avg']}
        {MsgLabelsMD.LAST_DAY}: 
            {MsgLabelsMD.STDDEV}: {block_times['last_day']['stddev']}
            {MsgLabelsMD.AVG}: {block_times['last_day']['avg']}
        {MsgLabelsMD.LAST_WEEK}: 
            {MsgLabelsMD.STDDEV}: {block_times['last_week']['stddev']}
            {MsgLabelsMD.AVG}: {block_times['last_week']['avg']}
        {MsgLabelsMD.LAST_MONTH}: 
            {MsgLabelsMD.STDDEV}: {block_times['last_month']['stddev']}
            {MsgLabelsMD.AVG}: {block_times['last_month']['avg']}
'''

            return markdown_message 
        
        if(parse_mode == ParseMode.MARKDOWN_V2):
            # format the message here
            
            markdownv2_message = f'''{title_md}
    {MsgLabelsMD.TOKEN_SUPPLY}: {escape(token_supply)}
    
    {MsgLabelsMD.ELECTION_TIMES}: 
        {MsgLabelsMD.LAST_HOUR}: 
            {MsgLabelsMD.STDDEV}: {escape(election_times['last_hour']['stddev'])}
            {MsgLabelsMD.AVG}: {escape(election_times['last_hour']['avg'])} 
        {MsgLabelsMD.LAST_DAY}: 
            {MsgLabelsMD.STDDEV}: {escape(election_times['last_day']['stddev'])}
            {MsgLabelsMD.AVG}: {escape(election_times['last_day']['avg'])} 
        {MsgLabelsMD.LAST_WEEK}: 
            {MsgLabelsMD.STDDEV}: {escape(election_times['last_week']['stddev'])}
            {MsgLabelsMD.AVG}: {escape(election_times['last_week']['avg'])}
        {MsgLabelsMD.LAST_MONTH}: 
            {MsgLabelsMD.STDDEV}: {escape(election_times['last_month']['stddev'])}
            {MsgLabelsMD.AVG}: {escape(election_times['last_month']['avg'])}           
            
    {MsgLabelsMD.COUNTS}: 
        {MsgLabelsMD.VALIDATORS}: {counts['validators']}
        {MsgLabelsMD.TRANSACTIONS}: {counts['transactions']}
        {MsgLabelsMD.OUIS}: {counts['ouis']}
        {MsgLabelsMD.HOTSPOTS_ONLINE}: {counts['hotspots_online']}
        {MsgLabelsMD.HOTSPOTS_DATA_ONLY}: {counts['hotspots_dataonly']}
        {MsgLabelsMD.HOTSPOTS}: {counts['hotspots']}
        {MsgLabelsMD.COUNTRIES}: {counts['countries']}
        {MsgLabelsMD.CONSENSUS_GROUPS}: {counts['consensus_groups']}
        {MsgLabelsMD.COINGECKO_PRICE_USD}: {escape(counts['coingecko_price_usd'])}
        {MsgLabelsMD.COINGECKO_PRICE_GBP}: {escape(counts['coingecko_price_gbp'])}
        {MsgLabelsMD.COINGECKO_PRICE_EUR}: {escape(counts['coingecko_price_eur'])}
        {MsgLabelsMD.CITIES}: {counts['cities']}
        {MsgLabelsMD.CHALLENGES}: {counts['challenges']}
        {MsgLabelsMD.BLOCKS}: {counts['blocks']}

    {MsgLabelsMD.CHALLENGE_COUNTS}: 
        {MsgLabelsMD.LAST_DAY}: {challenge_counts['last_day']}
        {MsgLabelsMD.ACTIVE}: {challenge_counts['active']}

    {MsgLabelsMD.BLOCK_TIMES}: 
        {MsgLabelsMD.LAST_HOUR}: 
            {MsgLabelsMD.STDDEV}: {escape(block_times['last_hour']['stddev'])}
            {MsgLabelsMD.AVG}: {escape(block_times['last_hour']['avg'])}
        {MsgLabelsMD.LAST_DAY}: 
            {MsgLabelsMD.STDDEV}: {escape(block_times['last_day']['stddev'])}
            {MsgLabelsMD.AVG}: {escape(block_times['last_day']['avg'])}
        {MsgLabelsMD.LAST_WEEK}: 
            {MsgLabelsMD.STDDEV}: {escape(block_times['last_week']['stddev'])}
            {MsgLabelsMD.AVG}: {escape(block_times['last_week']['avg'])}
        {MsgLabelsMD.LAST_MONTH}: 
            {MsgLabelsMD.STDDEV}: {escape(block_times['last_month']['stddev'])}
            {MsgLabelsMD.AVG}: {escape(block_times['last_month']['avg'])}
'''

            return markdownv2_message 

        elif(parse_mode == ParseMode.HTML):
            # if markdown
            html_message = f'''
                    {title_html}
            {MsgLabelsHTML.TOKEN_SUPPLY}: {token_supply}
            
            {MsgLabelsHTML.ELECTION_TIMES}: 
                {MsgLabelsHTML.LAST_HOUR}: 
                    {MsgLabelsHTML.STDDEV}: {election_times['last_hour']['stddev']}
                    {MsgLabelsHTML.AVG}: {election_times['last_hour']['avg']} 
                {MsgLabelsHTML.LAST_DAY}: 
                    {MsgLabelsHTML.STDDEV}: {election_times['last_day']['stddev']}
                    {MsgLabelsHTML.AVG}: {election_times['last_day']['avg']} 
                {MsgLabelsHTML.LAST_WEEK}: 
                    {MsgLabelsHTML.STDDEV}: {election_times['last_week']['stddev']}
                    {MsgLabelsHTML.AVG}: {election_times['last_week']['avg']}
                {MsgLabelsHTML.LAST_MONTH}: 
                    {MsgLabelsHTML.STDDEV}: {election_times['last_month']['stddev']}
                    {MsgLabelsHTML.AVG}: {election_times['last_month']['avg']}           
                    
            {MsgLabelsHTML.COUNTS}: 
                {MsgLabelsHTML.VALIDATORS}: {counts['validators']}
                {MsgLabelsHTML.TRANSACTIONS}: {counts['transactions']}
                {MsgLabelsHTML.OUIS}: {counts['ouis']}
                {MsgLabelsHTML.HOTSPOTS_ONLINE}: {counts['hotspots_online']}
                {MsgLabelsHTML.HOTSPOTS_DATA_ONLY}: {counts['hotspots_dataonly']}
                {MsgLabelsHTML.HOTSPOTS}: {counts['hotspots']}
                {MsgLabelsHTML.COUNTRIES}: {counts['countries']}
                {MsgLabelsHTML.CONSENSUS_GROUPS}: {counts['consensus_groups']}
                {MsgLabelsHTML.COINGECKO_PRICE_USD}: {counts['coingecko_price_usd']}
                {MsgLabelsHTML.COINGECKO_PRICE_GBP}: {counts['coingecko_price_gbp']}
                {MsgLabelsHTML.COINGECKO_PRICE_EUR}: {counts['coingecko_price_eur']}
                {MsgLabelsHTML.CITIES}: {counts['cities']}
                {MsgLabelsHTML.CHALLENGES}: {counts['challenges']}
                {MsgLabelsHTML.BLOCKS}: {counts['blocks']}

            {MsgLabelsHTML.CHALLENGE_COUNTS}: 
                {MsgLabelsHTML.LAST_DAY}: {challenge_counts['last_day']}
                {MsgLabelsHTML.ACTIVE}: {challenge_counts['active']}

            {MsgLabelsHTML.BLOCK_TIMES}: 
                {MsgLabelsHTML.LAST_HOUR}: 
                    {MsgLabelsHTML.STDDEV}: {block_times['last_hour']['stddev']}
                    {MsgLabelsHTML.AVG}: {block_times['last_hour']['avg']}
                {MsgLabelsHTML.LAST_DAY}: 
                    {MsgLabelsHTML.STDDEV}: {block_times['last_day']['stddev']}
                    {MsgLabelsHTML.AVG}: {block_times['last_day']['avg']}
                {MsgLabelsHTML.LAST_WEEK}: 
                    {MsgLabelsHTML.STDDEV}: {block_times['last_week']['stddev']}
                    {MsgLabelsHTML.AVG}: {block_times['last_week']['avg']}
                {MsgLabelsHTML.LAST_MONTH}: 
                    {MsgLabelsHTML.STDDEV}: {block_times['last_month']['stddev']}
                    {MsgLabelsHTML.AVG}: {block_times['last_month']['avg']}
            '''
            return html_message
        else:
            raise InvalidParseMode('Invalid parse_mode specified!')