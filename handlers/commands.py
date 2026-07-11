from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
	if message.chat.type == 'private':
		await message.reply("""
							hi, my name is embedero
							i make social media links more readable for ones, who want stay here, on telegram, and go nowhere else
							simply type my username (@embederobot) and your link and i transfer it to readable one!
							i promise you. i never collect what you want send to a friend.
							but if you dont believe me... read my source code
       
							also, see all supported services!
							""")
	else:
		return
  
@router.message(Command("help"))
async def cmd_help(message: Message):
	if message.chat.type == 'private':
		await message.reply("""
							tba
                      		""")
	else:
		return
	