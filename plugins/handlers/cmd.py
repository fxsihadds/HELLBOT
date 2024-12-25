from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import wget
import requests as re
import os, asyncio, time
from ..extra.temp import buttons_l, msg_buttons
from ..handlers.rnd import regenerate_callback
from helpers.forcesub import ForceSub
from database.mongodbs import adduser, is_exsist
from ..handlers.ocr import ocr_image_single
from helpers._ocr_helpers import sub_images
from helpers.video_meta_data import META
from helpers.display_progress import progress_for_pyrogram
from ..handlers.testline import find_strings_from_txt
from pprint import pformat

# Define the InlineKeyboardMarkup
_cmd_button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ᵀᵒᵒˡ", callback_data="tool"),
            InlineKeyboardButton("ᶜʰᵉᶜᵏᵉʳˢ", callback_data="checkers"),
            InlineKeyboardButton("ᴳᵃᵗᵉˢ", callback_data="gates"),
        ],
        [
            InlineKeyboardButton("ᴬᵈᵐⁱⁿ", callback_data="admin"),
            InlineKeyboardButton("ᶜˡᵒˢᵉ", callback_data="closed"),
        ],
    ]
)

tools_Click = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ᶜʰᵉᶜᵏᵉʳˢ", callback_data="checkers"),
            InlineKeyboardButton("ᴳᵃᵗᵉˢ", callback_data="gates"),
            InlineKeyboardButton("ᴼᵗʰᵉʳˢ", callback_data="others"),
        ],
        [
            InlineKeyboardButton("ᴬᵈᵐⁱⁿ", callback_data="admin"),
            InlineKeyboardButton("ᶜˡᵒˢᵉ", callback_data="closed"),
        ],
    ]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Generate", callback_data="generate"),
            InlineKeyboardButton("Refresh", callback_data="refresh"),
            InlineKeyboardButton("Close", callback_data="close"),
        ]
    ]
)


tools = """<i>𝔄𝔳𝔞𝔦𝔩𝔞𝔟𝔩𝔢 𝔠𝔬𝔪𝔫𝔞𝔫𝔡𝔰:</i>\n
<b>/𝔤𝔰𝔠𝔯</b> - ℬ𝔬𝔪𝔟𝔬 𝔖𝔠𝔯𝔞𝔭𝔢\n
<b>/𝔲𝔰𝔠𝔯</b> - ℬ𝔬𝔪𝔟𝔬 𝔲𝔰𝔢𝔯:𝔭𝔞𝔰𝔰, 𝔫𝔲𝔪𝔟𝔢𝔯:𝔭𝔞𝔰𝔰 𝔞𝔫𝔡 𝔢𝔪𝔞𝔦𝔩:𝔭𝔞𝔰𝔰\n
<b>/𝔭𝔞𝔰𝔱𝔢</b> - ℬ𝔬𝔪𝔟𝔬 𝔸𝔫𝔶 𝔱𝔢𝔵𝔱\n
<b>/𝔲𝔫𝔷𝔦𝔭</b> - ℬ𝔬𝔪𝔟𝔬 𝔲𝔫𝔷𝔦𝔭 𝔸 𝔣𝔦𝔩𝔢\n
<b>/𝔦𝔭</b> - ℬ𝔬𝔪𝔟𝔬 𝔠𝔥𝔢𝔠𝔨 𝔶𝔬𝔲𝔯 𝔦𝔭 𝔞𝔡𝔭𝔯𝔢𝔰𝔰\n
<b>/𝔯𝔞𝔫𝔡</b> - ℬ𝔬𝔪𝔟𝔬 𝔣𝔞𝔨𝔢 𝔯𝔞𝔫𝔡𝔬𝔪 𝔡𝔢𝔱𝔞𝔦𝔩𝔰\n
<b>/𝔟𝔬𝔪𝔟</b> - ℬ𝔬𝔪𝔟𝔬 𝔡𝔦𝔰𝔱𝔲𝔯𝔟 𝔶𝔬𝔲𝔯 𝔣𝔯𝔦𝔢𝔫𝔡\n
<b>/𝔱𝔢𝔪𝔭</b> - ℬ𝔬𝔪𝔟𝔬 𝔱𝔢𝔪𝔭 𝔪𝔞𝔦𝔩\n
<b>/𝔱𝔵𝔱</b> - ℬ𝔬𝔪𝔟𝔬 𝔪𝔞𝔨𝔢 𝔽𝔦𝔩𝔢\n
<b>/𝔫𝔦𝔡</b> - ℬ𝔬𝔪𝔟𝔬 𝔣𝔬𝔯 𝔫𝔦𝔡 𝔡𝔢𝔞𝔩𝔰\n
<b>/𝔰𝔲𝔯𝔩</b> - ℬ𝔬𝔪𝔟𝔬 𝔣𝔬𝔯 𝔰𝔥𝔬𝔯𝔱 𝔲𝔯𝔩\n
 """

checkers = """<i>𝔄𝔳𝔞𝔦𝔩𝔞𝔟𝔩𝔢 𝔠𝔬𝔪𝔪𝔞𝔫𝔡𝔰:</i>\n
<b>/𝔥𝔬𝔦</b> - ℭ𝔥𝔢𝔠𝔨 𝔜𝔬𝔲𝔯 𝔙𝔞𝔩𝔦𝔡 ℌ𝔬𝔦𝔠𝔥𝔬𝔦 ℭ𝔬𝔪𝔟𝔬\n
<b>/𝔠𝔯𝔲𝔫</b> - ℭ𝔥𝔢𝔠𝔨 𝔜𝔬𝔲𝔯 𝔙𝔞𝔩𝔦𝔡 ℭ𝔯𝔲𝔫𝔠𝔥𝔶𝔯𝔬𝔩𝔩 ℭ𝔬𝔪𝔟𝔬\n
<b>/𝔠𝔥𝔞𝔲𝔭𝔞𝔩</b> - ℭ𝔥𝔢𝔠𝔨 𝔜𝔬𝔲𝔯 𝔙𝔞𝔩𝔦𝔡 𝔠𝔥𝔞𝔲𝔭𝔞𝔩 ℭ𝔬𝔪𝔟𝔬\n
<b>/𝔠𝔥𝔬𝔯</b> - ℭ𝔥𝔢𝔠𝔨 𝔜𝔬𝔲𝔯 𝔙𝔞𝔩𝔦𝔡 ℭ𝔥𝔬𝔯𝔨𝔦 ℭ𝔬𝔪𝔟𝔬\n
"""


others = """<i>𝔄𝔳𝔞𝔦𝔩𝔞𝔟𝔩𝔢 𝔠𝔬𝔪𝔫𝔞𝔫𝔡𝔰:</i>\n
<code>/𝔟𝔦𝔫</code> - ℭ𝔥𝔢𝔠𝔨 𝔜𝔬𝔲𝔯 𝔅𝔦𝔫\n
<code>/𝔟𝔶𝔭𝔞𝔰𝔰</code> - 𝔅𝔶𝔭𝔞𝔰𝔰 𝔖𝔥𝔬𝔯𝔱 𝔘𝔯𝔩!\n
<code>/𝔯𝔢𝔪𝔳</code> - ℜ𝔢𝔪𝔬𝔳𝔢 𝔅𝔞𝔠𝔨𝔤𝔯𝔬𝔲𝔫𝔡 𝔣𝔯𝔬𝔪 𝔓𝔥𝔬𝔭𝔥𝔬𝔱𝔬\n
<code>/𝔤𝔢𝔪𝔦</code> - 𝔊𝔬𝔬𝔤𝔩𝔢 𝔄𝔦 𝔉𝔬𝔯 ℑ𝔪𝔞𝔤𝔢𝔰 𝔞𝔫𝔡 𝔗𝔢𝔵𝔱 𝔓𝔯𝔬𝔠𝔢𝔰𝔰𝔦𝔫𝔤\n
<code>/𝔯𝔢𝔡𝔢𝔢𝔪</code> - 𝔅𝔲𝔶 𝔓𝔯𝔢𝔪𝔦𝔲𝔪</b>\n
"""

Gates = """<i>𝔄𝔳𝔞𝔦𝔩𝔞𝔟𝔩𝔢 𝔠𝔬𝔮𝔫𝔞𝔡𝔰:</i>\n
<b>/𝔳𝔟𝔳</b> - ℬ𝔬𝔪𝔟𝔬 𝔠𝔥𝔢𝔠𝔨 𝔶𝔬𝔲𝔯 3𝔡𝔰 𝔠𝔞𝔯𝔡\n
<b>/3𝔡𝔰</b> - ℬ𝔬𝔪𝔟𝔬 𝔠𝔥𝔢𝔠𝔨 𝔶𝔬𝔲𝔯 3𝔡𝔰 𝔠𝔞𝔯𝔡\n
<b>/𝔟3</b> - ℬ𝔬𝔪𝔟𝔬 𝔟𝔯𝔞𝔦𝔫𝔱𝔯𝔢 𝔞𝔲𝔱𝔥\n
<b>/𝔠𝔥𝔨</b> - ℬ𝔬𝔪𝔟𝔬 𝔯𝔢𝔪𝔬𝔳𝔢 𝔟𝔞𝔠𝔨𝔤𝔯𝔬𝔲𝔫𝔡 𝔣𝔯𝔬𝔪 𝔭𝔥𝔬𝔱𝔬\n
<b>/𝔞𝔲𝔱𝔥</b> - ℬ𝔬𝔪𝔟𝔬 𝔤𝔬𝔬𝔤𝔩𝔢 𝔞𝔦 𝔣𝔬𝔯 𝔦𝔮𝔞𝔤𝔢𝔰 𝔞𝔫𝔡 𝔱𝔢𝔵𝔱 𝔭𝔯𝔬𝔠𝔢𝔰𝔰𝔦𝔫𝔤\n
<b>/𝔞𝔶𝔡𝔢𝔫</b> - ℬ𝔬𝔪𝔟𝔬 𝔟𝔲𝔶 𝔭𝔯𝔢𝔪𝔦𝔲𝔪\n
"""

admin = """<i>𝔄𝔳𝔞𝔦𝔩𝔞𝔟𝔩𝔢 𝔠𝔬𝔮𝔫𝔞𝔡𝔰:</i> 
<b>/𝔯𝔢𝔤𝔦𝔰𝔱𝔢𝔯</b> - <i>𝔄𝔡𝔡 𝔲𝔰𝔢𝔯𝔰</i>\n
<b>/𝔲𝔫𝔯𝔢𝔤𝔦𝔰𝔱𝔢𝔯</b> - <i>ℜ𝔢𝔪𝔬𝔳𝔢 𝔲𝔰𝔢𝔯𝔰</i>\n
<b>/𝔲𝔰𝔢𝔯𝔩𝔦𝔰𝔱</b> - <i>𝔖𝔥𝔬𝔴 𝔲𝔰𝔢𝔯𝔰</i>\n
<b>/𝔯𝔢𝔰𝔱𝔞𝔯𝔱</b> - <i>ℜ𝔢𝔰𝔱ᵃʳ𝔱 ʸᵒᵘʳ 𝔭ʳᵒᵍʳᵃᵐ</i>\n
<b>/𝔰𝔭𝔢𝔢𝔡𝔱𝔢𝔰𝔱</b> - <i>𝔗𝔢𝔰𝔱 ʸᵒᵘʳ 𝔰ᵉʳᵛᵉʳ 𝔰𝔭𝔢𝔢𝔡!</i>\n
"""


@Client.on_message(filters.command(["help", "start"]) & filters.incoming)
async def help_command(Client, message):
    user_id = message.from_user.id
    # force_sub = await ForceSub(Client, message)
    is_exsists = is_exsist(user_id)
    # if force_sub == 400: return
    if not is_exsists:
        await message.reply_text("<code>𝖈𝖔𝖒𝖒𝖆𝖓𝖉𝖘: </code>", reply_markup=_cmd_button)
        adduser(bot=Client, cmd=message)
    else:
        await message.reply_text("<code>𝖈𝖔𝖒𝖒𝖆𝖓𝖉𝖘: </code>", reply_markup=_cmd_button)
    global main_admin
    with open(
        file="plugins/ExtraMod/users/admin.txt", mode="r+", encoding="utf-8"
    ) as admin:
        main_admin = admin.readlines()


email = ""


@Client.on_callback_query()
async def cmd(client, callback_query):
    response = callback_query.data
    message = callback_query.message
    try:
        if response == "tool":
            await callback_query.edit_message_text(
                f"{tools}\n", reply_markup=tools_Click
            )

        elif response == "checkers":
            await callback_query.edit_message_text(
                f"{checkers}\n", reply_markup=_cmd_button
            )

        elif response == "others":
            await callback_query.edit_message_text(
                f"{others}\n", reply_markup=_cmd_button
            )
        elif response == "gates":
            await callback_query.edit_message_text(
                f"{Gates}\n", reply_markup=_cmd_button
            )
        elif response == "admin":
            await callback_query.edit_message_text(
                f"{admin}\n", reply_markup=_cmd_button
            )
        elif response == "back":
            await callback_query.edit_message_text(
                f"{admin}\n", reply_markup=_cmd_button
            )
        elif response == "closed":
            await callback_query.message.delete()
        elif response == "NewGenerate":
            await callback_query.edit_message_text("here are our Main Gmail!")

        elif response == "extract":
            ocr_images_store = f"ocrdict{callback_query.from_user.id}"
            status = await callback_query.message.reply_text(
                "<b>⎚ `Downloading...`</b>"
            )
            download = await client.download_media(message.video)
            await sub_images(
                client, status, download, ocr_images_store
            )  # Ensure to await here
            os.remove(download)
        elif response == "metadata":
            status = await callback_query.message.reply_text(
                "<b>⎚ `Downloading...`</b>"
            )
            video_path = await client.download_media(callback_query.message.video)
            v1 = META(path=video_path)
            result = v1.mediainfo_ext()

            # Format the output for easy copying
            formatted_result = pformat(result, indent=4, width=80)
            await status.edit_text(
                f"<b>Video Information:</b>\n<pre>{formatted_result}</pre>"
            )
            os.remove(video_path)
        elif response == "extaudio":
            status = await callback_query.message.reply_text(
                "<b>⎚ `Downloading...`</b>"
            )
            video_path = await client.download_media(message.video)
            v1 = META(path=video_path)
            result = v1.ext_audio()
            send = await client.send_document(
                chat_id=message.chat.id,
                document="audio/output_audio.mp3",  # Path to the file
                caption="Here is your audio file!",  # Optional caption
            )
            await status.delete()
            os.remove("audio/output_audio.mp3")
            os.remove(video_path)
        elif response == "spvideo":
            status = await callback_query.message.reply_text(
                "<b>⎚ `Downloading...`</b>"
            )
            video_path = await client.download_media(message.video)
            v1 = META(path=video_path)
            result = v1.split_video("output_part1.mp4", "output_part2.mp4")
            part_of_video = ["output_part1.mp4", "output_part2.mp4"]
            # Assuming 'part_of_video' contains a list of file paths for the split video parts
            for idx, items in enumerate(part_of_video):
                # Send each video part
                send = await client.send_video(
                    chat_id=message.chat.id,  # Target chat
                    video=items,  # Path to the video file
                    caption=f"Here is your Video Part {idx + 1}!",  # Caption with part number
                )
                os.remove(items)

            await status.delete()
            os.remove(video_path)
        elif response == "ocrdata":
            if message.photo:
                file_path = await client.download_media(message.photo)
                recognized_text = await ocr_image_single(file_path)
                await callback_query.message.reply_text(recognized_text)
                os.remove(file_path)
                # await asyncio.sleep(2)
                await client.delete_messages(
                    chat_id=message.chat.id, message_ids=[message.id]
                )
            else:
                await callback_query.message.reply_text("No photo to process.")

        elif response == "about_gmail":
            await callback_query.edit_message_text("About Gmail!")
        elif response == "ulpextract":
            STATUS_ID = "<b>⎚ `Downloading The Text File...`</b>"
            start_time = time.time()
            file_name = message.document.file_name
            user_folder = f"downloads/{callback_query.from_user.id}"
            file_path = os.path.join(user_folder, file_name)
            if not os.path.exists(user_folder):
                os.makedirs(user_folder)

            user_res = await client.ask(message.chat.id, "WRITE YOUR KEYWORD:✍")
            # Extract the text of the response
            find_str = user_res.text
            status = await message.reply_text("<b>⎚ `Processing...`</b>")
            await message.download(
                file_name=file_path,
                progress=progress_for_pyrogram,
                progress_args=(STATUS_ID, status, file_name, start_time),
            )
            await find_strings_from_txt(find_str, file_path, status, client)
            os.remove(file_path)
            # await callback_query.message.reply_text(f"Thank you, {user_name}!")
        elif response == "trimvideo":
            # trim_video = "video"
            user_res = await client.ask(
                message.chat.id, "Write Your Second Start:end :✍"
            )
            find_str = user_res.text.split(":")
            print(find_str[0], find_str[1])
            video_path = await client.download_media(message.video)
            output_path = os.path.splitext(video_path)[0] + "_trimmed.mp4"
            v1 = META(path=video_path)
            result = v1.trim_video(output_path, int(find_str[0]), int(find_str[1]))
            send = await client.send_video(
                chat_id=message.chat.id,  # Target chat
                video=output_path,  # Path to the video file
                caption=f"Here is your Trim Video",  # Caption with part number
            )
            os.remove(output_path)
            os.remove(video_path)

        elif response == "generatetemp":
            global email
            email = re.get(
                "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
            ).json()[0]
            await callback_query.edit_message_text(
                "__**Your Temporary E-mail: **__`" + str(email) + "`",
                reply_markup=buttons_l,
            )

        elif response == "refreshtemp":
            try:
                if email == "":
                    await callback_query.edit_message_text(
                        "Generate an email", reply_markup=buttons_l
                    )
                else:
                    getmsg_endp = (
                        "https://www.1secmail.com/api/v1/?action=getMessages&login="
                        + email[: email.find("@")]
                        + "&domain="
                        + email[email.find("@") + 1 :]
                    )
                    print(getmsg_endp)
                    ref_response = re.get(getmsg_endp).json()
                    global idnum
                    idnum = str(ref_response[0]["id"])
                    from_msg = ref_response[0]["from"]
                    subject = ref_response[0]["subject"]
                    refreshrply = (
                        "You have a message from "
                        + from_msg
                        + "\n\nSubject : "
                        + subject
                    )
                    await cmd.edit_text(refreshrply, reply_markup=msg_buttons)
            except:
                await callback_query.answer(
                    "No messages were received..\nin your Mailbox " + email,
                    show_alert=True,
                )
        elif response == "view_msgtemp":
            msg = re.get(
                "https://www.1secmail.com/api/v1/?action=readMessage&login="
                + email[: email.find("@")]
                + "&domain="
                + email[email.find("@") + 1 :]
                + "&id="
                + idnum
            ).json()
            print(msg)
            from_mail = msg["from"]
            date = msg["date"]
            subjectt = msg["subject"]
            try:
                attachments = msg["attachments"][0]
            except:
                pass
            body = msg["body"]
            mailbox_view = (
                "ID No : "
                + idnum
                + "\nFrom : "
                + from_mail
                + "\nDate : "
                + date
                + "\nSubject : "
                + subjectt
                + "\nmessage : \n"
                + body
            )
            await callback_query.edit_message_text(mailbox_view, reply_markup=buttons_l)
            mailbox_view = (
                "ID No : "
                + idnum
                + "\nFrom : "
                + from_mail
                + "\nDate : "
                + date
                + "\nSubject : "
                + subjectt
                + "\nmessage : \n"
                + body
            )
            if attachments == "[]":
                await callback_query.edit_message_text(
                    mailbox_view, reply_markup=buttons_l
                )
                await callback_query.answer(
                    "No Messages Were Received..", show_alert=True
                )
            else:
                dlattach = attachments["filename"]
                attc = (
                    "https://www.1secmail.com/api/v1/?action=download&login="
                    + email[: email.find("@")]
                    + "&domain="
                    + email[email.find("@") + 1 :]
                    + "&id="
                    + idnum
                    + "&file="
                    + dlattach
                )
                print(attc)
                mailbox_vieww = (
                    "ID No : "
                    + idnum
                    + "\nFrom : "
                    + from_mail
                    + "\nDate : "
                    + date
                    + "\nSubject : "
                    + subjectt
                    + "\nmessage : \n"
                    + body
                    + "\n\n"
                    + "[Download]("
                    + attc
                    + ") Attachments"
                )
                filedl = wget.download(attc)
                await callback_query.edit_message_text(
                    mailbox_vieww, reply_markup=buttons_l
                )
                os.remove(dlattach)
        elif response == "closetemp":
            await callback_query.edit_message_text("Session Closed✅")
        elif response == "regenerateadds":
            await regenerate_callback(client, callback_query)
    except Exception as e:
        print(f"An error occurred: {e}")
