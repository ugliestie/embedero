from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject

from keyboards.start import kb_start

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message, command: CommandObject):
	if message.chat.type == 'private':
		if command.args == 'services':
			await message.reply("""
currently supported:

tiktok
twitter posts (twitter.com and x.com links)
instagram posts and stories
pinterest
bluesky
                      		""")
		else:
			await message.reply("""
hi, my name is embedero!

i make social media links more readable for ones, who want stay here, on telegram, and go nowhere else
simply type my username (@embederobot) and your link and i transfer it to readable one!
i promise you. i never collect what you want send to a friend.
but if you dont believe me... <a href="https://github.com/ugliestie/embedero">read my source code</a>

tap button below to test it and see supported services on /services!
							""",
       		reply_markup=kb_start(),
       		disable_web_page_preview=True)
	else:
		return
  
@router.message(Command("services"))
async def cmd_help(message: Message):
	if message.chat.type == 'private':
		await message.reply("""
currently supported:

tiktok
twitter posts (twitter.com and x.com links)
instagram posts and stories
pinterest
bluesky
                      		""")
	else:
		return