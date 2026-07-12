from aiogram import Router, F
from aiogram.types import InlineQuery, InlineQueryResultArticle, \
    					InlineQueryResultsButton, InputTextMessageContent, \
						LinkPreviewOptions

from utils.links_changer import change_link, InvalidQuery, NotSupported

import logging

logger = logging.getLogger(__name__)

router = Router()

@router.inline_query(F.query)
async def inline(inline_query: InlineQuery):
	try:
		link = await change_link(inline_query.query)
		result = InlineQueryResultArticle(
			id='ughidk',
			title='send embed link :3',
			input_message_content=InputTextMessageContent(
				message_text=f"{link}",
				parse_mode="HTML"
			)
		)
		await inline_query.answer([result], is_personal=True)
	except NotSupported:
		button = InlineQueryResultsButton(text="see all supported services", start_parameter='services')
		result = InlineQueryResultArticle(
			id='ughidk',
			title='there is nothing supported here, sorry :<',
			input_message_content=InputTextMessageContent(
				message_text=f"owo",
				parse_mode="HTML"
			)
		)
		await inline_query.answer([result], button=button, is_personal=True)			
	except InvalidQuery:
		button = InlineQueryResultsButton(text="see all supported services", start_parameter='services')
		result = InlineQueryResultArticle(
			id='ughidk',
			title='i think thats not a link :<',
			input_message_content=InputTextMessageContent(
				message_text=f"owo",
				link_preview_options=LinkPreviewOptions(show_above_text=True)
				parse_mode="HTML"
			)
		)
		await inline_query.answer([result], button=button, is_personal=True)