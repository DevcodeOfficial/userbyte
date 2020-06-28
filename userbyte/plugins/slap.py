import pyrogram
from pyrogram import Filters
from userbyte import byte, cmd
import random

@byte.on_message(Filters.command('slap', cmd) & Filters.me)
async def slep(byte, message):
	
	if not message.reply_to_message:
		await message.edit("`📌 Reply To Any User's Message! 😈 Else I'll Slap You`")
	else:
		from_user = await byte.get_users(message.reply_to_message.from_user.id)
	
		ITEMS = [
		    "kids generator machine",
		    "egg flavored comdom",
		    "one glass of lava"
		    "large trout",
		    "baseball bat",
		    "cricket bat",
		    "wooden cane",
		    "nail",
		    "printer",
		    "shovel",
		    "CRT monitor",
		    "physics textbook",
		    "toaster",
		    "portrait of Richard Stallman",
		    "television",
		    "five ton truck",
		    "roll of duct tape",
		    "book",
		    "laptop",
		    "old television",
		    "sack of rocks",
		    "rainbow trout",
		    "rubber chicken",
		    "spiked bat",
		    "fire extinguisher",
		    "heavy rock",
		    "chunk of dirt",
		    "beehive",
		    "piece of rotten meat",
		    "bear",
		    "ton of bricks",
		    "jhony's dickkoo",
		    "potty of dinosaur",
		    "mjonir",
		    "strombreaker",
		    "cap's shield",
		    "smelly egg",
		    "hulk's hand",
		    "majnu bhai ki painting",
		    
		]
		
		THROW = [
		    "throws",
		    "flings",
		    "chucks",
		    "hurls",
		]
		
		HIT = [
		    "hits",
		    "whacks",
		    "slaps",
		    "smacks",
		    "bashes",
		    "fek ke mari",
		]
		
		hits = random.choice(HIT)
		item = random.choice(ITEMS)
		throws = random.choice(THROW)
		victim = f'[{from_user.first_name}](tg://user?id={from_user.id})'
		
		SLAP_TEMPLATES = [
		    f"{hits} {victim} with a {item}.",
		    f"{hits} {victim} in the face with a {item}.",
		    f"{hits} {victim} around a bit with a {item}.",
		    f"{throws} a {item} at {victim}.",
		    f"grabs a {item} and {throws} it at {victim}'s face.",
		    f"launches a {item} in {victim}'s general direction.",
		    f"starts slapping {victim} silly with a {item}.",
		    f"pins {victim} down and repeatedly {hits} them with a {item}.",
		    f"grabs up a {item} and {hits} {victim} with it.",
		    f"ties {victim} to a chair and {throws} a {item} at them.",
		    f"gave a friendly push to help {victim} learn to swim in lava."
		    f"ohh no i cant slap this alien {victim}",
		]
		
		slapped = random.choice(SLAP_TEMPLATES)
		await message.edit(slapped)
