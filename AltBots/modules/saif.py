from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.url(" 𝐌ᴜsɪᴄ ", "chla jaa xd"),
        Button.url("𝐎ᴡɴᴇʀ", "https://t.me/Homosapienhu")
    ],
    [
        Button.url(" 𝐂н𝙰𝙽𝙽𝙴𝙻 ", "https://t.me/sudeokeliyeaajaobclog"),
        Button.url(" 𝐒𝚄𝙿𝙿𝙾𝚃  ", "https://t.me/sudeokeliyeaajaobclog")
    ],
    [
        Button.url("𝐑ᴇᴘᴏ ", "CHLA JAA RANDI KE BACCHE ☔"),
      
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [wandering_soul](https://t.me/Homosapienhu)**\n\n"
        TEXT += f"» **ᴡᴀɴᴅᴇʀɪɴɢ ʙᴏᴛ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://telegra.ph/file/7020ac6ebd771d2a8d050.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
)
