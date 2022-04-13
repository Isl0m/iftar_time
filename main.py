from pyrogram import Client
from pyrogram.errors import FloodWait
import asyncio
from PrayTime import getTime 

app = Client(
    api_id = 4543915,
    api_hash = 'b3d43254073ff0ddbbfca438eb03ceb1',
    session_name = 'AgBKcB8iX5RaaOMidFiYTuy5Ytm6LBc_xpxereJCMpOnyk8Bunhbk9CK3YUfpCHpxi48cjZa4rrMicYeimHJuucUAVoZO4AVR40r1xt0Hr53I9sjqUpXLPdeCgwhMk4nWlkQKBNUu_5yvNFTvN23pJostDLv96VSoO0RRoBZu0qfdTlJe-_811eK6DTzYaNY6uegWggS-SQvqwBs0iUkMt6el9n0c70oY4BR27WT1w0jMzRCCpszHz5qEdkbRGJy2QWXBqu5kESPbsLSa1qQkeSQI-dt0e82wthqrTCTrd913n25Jalf4NXEwyOJCQVbLmVRhQ6n4HGb5ZH1mNefgVcRFpO14gA'
)
async def main_teletips():
    try:
        while True:
            if app.is_connected:
                await app.update_profile( last_name = f"{getTime()}")
                try:
                    print('try')
                except Exception:
                    pass        
                print("Profile Updated!")
            await asyncio.sleep(60)     
    except FloodWait as e:
        await asyncio.sleep(e.x)         

print("DATE TIME USERBOT IS ALIVE!")
asyncio.ensure_future(main_teletips())
app.run()