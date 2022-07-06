class script(object):


    STRT_TXT = """<code>Hello</code> {},
<code>I am </code> <a href=https://t.me/{}>{}</a>,<code> I support both Auto filter and manual filter modules.Also you can use me as a file sharing bot☺️</code>"""
      
    START_TXT = """
Hᴇʏ {} {}👋, 

I ᴀᴍ ᴊᴜsᴛ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ Aᴜᴛᴏғɪʟᴛᴇʀ Bᴏᴛ Wɪᴛʜ ᴇxᴛʀᴀ ᴄᴀᴘᴀʙɪʟɪᴛɪᴇs.Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ ᴀɴᴅ I'ʟʟ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴛʜᴇʀᴇ❤️

I'ᴠᴇ ʙᴇᴇɴ ᴀʟɪᴠᴇ ғᴏʀ: <code>{}</code>
"""

    HELP_TXT = """Hey {}!
I am Deadpool,a fully customisable autofilter bot with lots of additional features.I support many features such as autofilter with Imdb support,manual filter, channel filter & so on. Before using me, please read all the help guide to use me with full potential.
Here is the basic help commands.

• /start - To check if I'm alive
• /help - For help
"""

    ABOUT_TXT = """○ Mʏ Nᴀᴍᴇ: {}
○ Cʀᴇᴀᴛᴏʀ: <a href=https://t.me/pubgplayer1>Walter</a>
○ Lɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org>Pʏʀᴏɢʀᴀᴍ</a>
○ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>ᴘʏᴛʜᴏɴ 𝟹</a>
○ Dᴀᴛᴀʙᴀsᴇ: <a href=https://www.mongodb.com>Mᴏɴɢᴏ DB</a>
○ Bᴏᴛ Sᴇʀᴠᴇʀ: 𝙷𝙴𝚁𝙾𝙺𝚄
○ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>V2.0.17[Beta]</code>"""

    FILESTORE_TXT = """Help: <b>File Store</b>

- File Store is a feature To Get Sharable Link For Any Telegram Media 

<b>Commands and usage</b>:
• /link - Reply to any file/media to get a sharable link.
• /plink -  Same as /link command.But if /plink is used the file cant be forwarded to any other chats.
• /batch - To create a batch of files.
• /pbatch -  To create a batch of files with forward restriction.

<b>Example:</b> /batch <code>https://t.me/testinfame/1</code> <code>https://t.me/testinfame/5</code>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Deadpool will respond whenever a keyword is found in the message

<b>NOTE:</b>
1. Deadpool should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>Add a filter in chat</code>
• /filters - <code>List all the filters of a chat</code>
• /del - <code>Delete a specific filter in chat</code>
• /delall - <code>Delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- Deadpool Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Deadpool supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
```[Button Text](buttonurl:https://t.me/AutofilterInfBot)```

<b>Alert buttons:</b>
```[Button Text](buttonalert:This is an alert message)```
"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contain any camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only group admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of Deadpool

<b>Commands and Usage:</b>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>Commands and usage:</b>
• /settings - Use this command in your group or in bot PM (you must connect your bot with bot pm using /connect)
• /set_template - Every group admin can set Imdb template by their own.For more template details read formatting.
• /set_welcome - You can set customized welcome message in each group(buttons not supported).
• /copy - Use this command in your PM for broadcasting message to your group.
• /set_fcap - To set custom file caption(NOTE: Custom file caption will not work when bot pm is enabled)
• /setchannel - Use this command to filter files to custom channel instead of bot pm."""
    
    SETTINGS_TXT = """
<b>Available Settings:-</b>

• Request Mode - Enable this mode to prevent users from clicking someone's reuqested files.
• Channel Mode - If Channel Mode enabled, files will be delivered to channel(Note: /setchannel <chatid> use this command before enabling channel mode.Otherwise the link will redirected to Bot Pm.
• Filter Button - You can set to use double/ single button for results.
• Bot PM - If enabled bot will be redirected to start the bot instead of sending directly on clicking button.
• File Secure - Enable to secure your files being forwarded to other chats. 
• IMDB -  Enable / Disable IMDb information in results shown by bot.
• Spell Check - If enabled, bot will be suggesting related movies name by searching on google.
• Welcome - Enable to welcome new users of your group.
"""
    OWNER_TXT = """Help: <b>Owner mods</b>

<b>NOTE:</b>
This module only work for my Devs.

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
"""
    DBT_TXT = """
Deadpool Now Supports Custom IMDB Templates.You can customize them as per your needs.
hit /format for more details

<b>Available vars</b>
```query``` = searched movie name,
```{message.from_user.mention}``` = To mention requested user,
```title```, ```localized_title```, ```rating```, ```votes```, ```Aka```, ```seasons```, ```box_office```, ```kind```, ```Poster```, ```url```, ```plot```, ```cast```, ```runtime```, ```release_date```, ```year```, ```countries```, ```certificates```, ```languages```, ```director```, ```writer```, ```producer```, ```composer```, ```cinematographer```, ```music_team```, ```distributors```, ```genres```
<b><u>Below values should be in small letter.</b></u>
first = First name of the user, last = Last name of the user, mention = Mention the user, chat = Group Name

<b>An Example Template:</b>
```<b>🏷 Title</b>: <a href={url}>{title}</a>
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10
📆 Release Info : {release_date}
🎛 Countries : <code>{countries}</code>
Requested by : {mention}``` """

    STATUS_TXT = """★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code>"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    NOT_TEXT = """ 
Hey {},
That's for {} 🍂
⚠️Request again⚠️
"""
    WLC_TXT = """

Help: <b>Greetings:-</b>

<b>Note:</b> Buttons not supported in welcome message.

<b>Commands and Usage:</b>
• /set_welcome - Set customised welcome message
• /cleanwelcome - Enable this Command to delete the older welcome messages.

Below values should be in small letter.Else welcome message would be error.

first = First name of the user
last = Last name of the user
mention = Mention the user
chat = Group Name

Example of usage:
/set_welcome Hello {mention}, Thank you for Joining {chat}.
"""
    FMT = """

<b><u>IMDB TEMPLATE</b></u>
You can customize them as per your needs.

Available vars
query = searched movie name
title = original imdb title
localized_title = local name of movie
rating = imdb Rating
votes = number of votes on which rating is based.
aka = also known as names
seasons =  number of seasons
box_office = box office collection
kind = movie / series / drama /feature, etc..
imdb_id =imdb Id 
poster = url of imdb poster
url = imdb url
plot = story line
cast =cast info
runtime = runtime info in minutes
release_date = date of release if available , else year
year = year of release
countries 
certificates 
languages
director 
writer 
producer
composer
cinematographer 
music_team
distributors 
genres

<b><u>Below Values Should be in small letter<b></u>
first = First Name of the user
last = Last name of the user
mention = To mention a user
chat = Group name

An Example Template:

<b>🏷 Title</b>: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)
☀️ Languages : <code>{languages}</code>
👥 Cast : <code>{cast}</code>
📀 RunTime: {runtime} Minutes
📆 Release Info : {release_date}
🎛 Countries : <code>{countries}</code>

Requested by : {mention}
"""
    FILECAP_TXT = """
<code>{file_name}</code>
<b>Size:</b> <code>{file_size}</code>

Thank You For Using [Deadpool](https://t.me/AutofilterInfBot)❣️.
"""
    GET_FILE_TXT = """
Hey {mention}👋,
<b>Your File is Ready!!!</b>
<b>Name:</b> <code>{title}</code>
<b>size:</b> <code>{size}</code>
"""
    MISC_TXT = """
Help: <b>Misc</b>

An "odds and ends" module for small, simple commands which don't really fit anywhere.

<b>Commands and Usage:</b>
• /id: Get a user's ID.
• /info: Get a user's info.
• /format: Information on how to use welcome/Imdb template formats with the bot.
"""
    PIN_TXT = """Help: <b>Pin Commands</b>

All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

<b><u>Commands and Usages:</u></b>

<b>Admin Commands</b>
• /pin - Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
• /unpin - Unpin the current pinned message. If used as a reply, unpins the replied to message.
<b>User Commands</b>
• /pinned - Get the current pinned message.
"""
    MKDWN = """
Help: <b>Formatting</b>

Deadpool supports a large number of formatting options to make your messages more expressive. Take a look!  
""" 
    SET_TXT = """Help: <b>Settings</b>

<b><u>Available Settings:</u></b>

<b>Filter Button</b> - Same As SINGLE_BUTTON config. You can set to use double/ single button for results.
<b>Bot PM</b> - If enabled bot will be redirected to start the bot instead of sending directly on clicking button.
<b>File Secure</b> - Enable to secure your files being forwarded to other chats. 
<b>IMDB</b> -  Enable / Disable IMDb information in results shown by bot.
<b>Spell Check</b> - If enabled, bot will be suggesting related movies name by searching on google.
<b>Welcome</b> - Enable to welcome new users of your group.
<b>Channel Filter</b> - Turn channel mode to filter results in to a channel, but you should /set_channel first  before enabling, else the link will goes to bot pm.
<b>Request Mode</b> - Enable Request Mode helps to stop users from using someones requested buttons.(Eg: when someone clicks on the results of another user,The bot will shows 'Thats not for you')
"""
