import discord  # calls the discord library
import random
from discord import utils
from discord.ext import commands
import asyncio

client = discord.Client()

hello_words = ['hello', 'hi', 'привет', 'даров']  # variable for getting to know the bot

bidlo_words = ['быдло']  # words for the answer "cattle"

zashibymba_words = ['как дела', 'как настроение', 'как самочувствие', 'как кок', 'что с лицом', 'где ты']
# words for everything zashibumba

gender_words = ['какой твой гендер']  # слово, которое бот будет говорить свой гендер

dushnila_words = ['главный душнила', 'кто же главный душнила', 'душнила степан', 'душнила', 'где душнила']
# suffocating words

scam_words = ['скамер гейщита', 'скам гейщита', 'скамер', 'пидман гейшина', 'скам гейшина', 'кто скамер гейщита']
# words on scammer gayshit

shlepa_words = ['хочю шлепу', 'хочу шлепу', 'хочю шлёпу', 'хочу шлёпу', 'шлепа', 'шлёпа']
# words to display pictures with a slap

gachi_words = ['билли', 'билли херингтон', 'van', 'billy', 'gachi', 'slave', 'slaves', 'boy', 'boyчик', 'коки', 'гачи']
# words for conclusion gacha photo

member_bidlo = [347707004887760896]  # id people who will be nickname redneck

channel_list = [786673508523573308, 787421195318067201, 826544138626269284, 897442790085128202, 856997399259643934, 802266369101922345]  # id of the channels that the bot will ignore

whiteList = [403970760424554498]  # User ID to whom to set reactions (insert Stepan's id here)

#monitors the voting, then to give roles
POST_ID = 897430307979022387  # id of the post where it monitors reaction voting

MAX_ROLES_PER_USER = 150.0  # the maximum number of roles a user has

ROLES = {
    '🤚': 897429665805922314,
    '🖖': 897429727323774976,
    '🤡': 897432428279377921,
    '✊': 897431677855477821,
    '🤏': 897429665805922314
}  # reactions and role id to give

EXCROLES = ()  # here which role should not be given roles


class MyClient(discord.Client):

    async def on_ready(self):  #prints to the console that the bot has started working
        print('Logged on as {0}!'.format(self.user))

    async def on_raw_reaction_add(self, payload):
        if payload.message_id == POST_ID:
            channel = self.get_channel(payload.channel_id)  # get the channel object
            message = await channel.fetch_message(payload.message_id)  # get the message object
            member = payload.member
            print(member)

            try:
                emoji = str(payload.emoji)  # emoji chosen by the user
                role = utils.get(message.guild.roles, id=ROLES[emoji])  # selected role object (if any)

                if (len([i for i in member.roles if i and i.id not in EXCROLES]) <= MAX_ROLES_PER_USER):
                    await member.add_roles(role)
                    print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('[ERROR] Too many roles for user {0.display_name}'.format(member))

            except KeyError as e:
                print('[ERROR] KeyError, no role found for ' + emoji)
            except Exception as e:
                print(repr(e))

    async def on_raw_reaction_remove(self, payload):
        channel = self.get_channel(payload.channel_id)  # get the channel object
        message = await channel.fetch_message(payload.message_id)  # get the message object
        user_id = payload.user_id  # in fact, this garbage is not needed, but just in case, do not worry
        member = await (await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
        print(member, user_id)
        try:
            emoji = str(payload.emoji)  # эмоджик который выбрал юзер
            role = utils.get(message.guild.roles, id=ROLES[emoji])  # selected role object (if any)

            await member.remove_roles(role)
            print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))


# RUN
client = MyClient()
client = commands.Bot(command_prefix='!')
# intents = intents


@client.command(pass_context=True)  # command to change the nickname of the selected participant(!justice '@nick_of_person new_nick)
async def justice(ctx, member: discord.Member, nick):
    nick_bidlo = 'Вова Fist'
    nick_default = 'Красавчек'
    await ctx.send('Спровебыдлость восстановлена')
    if member.id in member_bidlo:  # changes nicknames of people to cattle
        await member.edit(nick=nick_bidlo)
    else:  # the rest on the nickname handsome
        await member.edit(nick=nick_default)


@client.event
async def on_message(message):
    # function of reaction to the message ( message - reacts to the whole message as a whole (check it all))
    if message.author == client.user:  # if it is a bot itself, then it does nothing
        return

    if message.channel.id in channel_list:  # Channel ID to ignore
        return
    else:
        hello = message.content.lower()  # converts the user's message to lowercase
        find_hello_words = False
        for item in hello_words:
            if hello.find(item) >= 0:
                find_hello_words = True
        if (find_hello_words):
            await message.channel.send(f' {message.author.mention} Даров')

        bidlo = message.content.lower()  # converts the user's message to lowercase
        find_bidlo_words = False
        for item in bidlo_words:
            if bidlo.find(item) >= 0:
                find_bidlo_words = True
        if (find_bidlo_words):
            await message.channel.send(f' {message.author.mention} Сам быдло!')

        zashibymba = message.content.lower()  # converts the user's message to lowercase
        find_zashibymba_words = False  # this is what searched for phrases (words with a space)
        for item in zashibymba_words:
            if zashibymba.find(item) >= 0:
                find_zashibymba_words = True
        if (find_zashibymba_words):
            await message.channel.send(f' {message.author.mention} Всё зашибумба')

        gender = message.content.lower()
        find_gender_words = False
        for item in gender_words:
            if gender.find(item) >= 0:
                find_gender_words = True
        if (find_gender_words):
            await message.channel.send(f' {message.author.mention} Я боевой вертелёт Апачи!')

    if message.author.id in whiteList:  #reactions to all messages on steponka
        await message.add_reaction('🤡')
        await message.add_reaction('🆎')
        await message.add_reaction('🅾️')
        await message.add_reaction('🅱️')
        await message.add_reaction('🅰️')
        await message.add_reaction('👺')

    dushnila = message.content.lower()  # converts the user's message to lowercase
    find_dushnila_words = False  # this is what searched for phrases (words with a space)
    for item in dushnila_words:
        if dushnila.find(item) >= 0:
            find_dushnila_words = True
    if (find_dushnila_words):
        pol = '<@&856948789037236235>'  # paste here then stepan's role id
        await message.channel.send(f' {pol} Вот же он!')

    scam = message.content.lower()  # converts the user's message to lowercase
    find_scam_words = False  # this is what searched for phrases (words with a space)
    for item in scam_words:
        if scam.find(item) >= 0:
            find_scam_words = True
    if (find_scam_words):
        rol = '<@&897429035641110529>'  # insert here then the id of the role of Misha
        await message.channel.send(f' {rol} Так цэ ж он!')

    shlepa = message.content.lower()  # converts the user's message to lowercase
    find_shlepa_words = False  # this is what searched for phrases (words with a space)
    for item in shlepa_words:
        if shlepa.find(item) >= 0:
            find_shlepa_words = True
    if (find_shlepa_words):
        imgs = [
            'https://sun9-87.userapi.com/impg/dwkRc8IKbPHO4Z9C8_0Ync9uCqiFkTS983MFqw/Byp8PkeJfMA.jpg?size=1080x772&quality=95&sign=870b00493e3c673ab898bbae2ae687d8&type=album',
            'https://sun9-67.userapi.com/impg/IBOXocbFQmr07Rqys3HbgTE3oIyLz2zYr3-ywg/2IGTmSfJwWk.jpg?size=483x512&quality=95&sign=11b8864471d55f0b3d553432abdf7753&type=album',
            'https://sun9-76.userapi.com/impg/v_EaKb81lQxvtNVTk10JUmu-jy9L03DwbAhW_w/IyYanTbG7k4.jpg?size=429x604&quality=95&sign=970802264c6c81ca50c8cc7c6b4f7300&type=album',
            'https://sun9-37.userapi.com/impg/hO1oi_4kkc0KrECoV-BBEmjjkvDZ4Ylk9Vn0Rw/EJgJXD318E8.jpg?size=1080x591&quality=95&sign=e51e718c0c3eab25d76254ea311bcb1c&type=album',
            'https://sun9-80.userapi.com/impg/6rGykt8AIzdifDM6eOZrtUQaiptUcrjFtopcvQ/kXuwELVtM6Y.jpg?size=1080x723&quality=95&sign=4e2e8a96fbb40a26e3eae80ebed76216&type=album',
            'https://sun9-31.userapi.com/impg/qy1EN55jA9pomq4OGQ2M35hVTgbq1cHno7rySQ/A5dkPt7k7lk.jpg?size=1080x1058&quality=95&sign=71cbeb0de91c29511ad79c5dc403a1dd&type=album',
            'https://sun9-35.userapi.com/impg/wWoBrsP0otg3Pbpy6ddbEs-lCifl2LW-_v1zUw/tBqgp-IuuI8.jpg?size=1080x678&quality=95&sign=6edc55ea312f0ed1889ae509426d8360&type=album',
            'https://sun9-7.userapi.com/impg/sN5JHXqz431PWNdHsNZYLpb3LUYkFoJu9B9FxA/rvdQL32qIL0.jpg?size=1134x720&quality=95&sign=35cbff8df7dbad10445619b1c55ac736&type=album',
            'https://sun9-67.userapi.com/impg/SnxqTrpQ15bPEpyujb8Lo_SvYXdhReKb-ym0aw/WPqIcUqkEyM.jpg?size=1080x738&quality=95&sign=e01972062925406ee0a406124eb7e145&type=album',
            'https://sun9-55.userapi.com/impg/SupCsoDL5kOzbpMBsGZ5pXoykQN5oJsIk8w_yg/nDK4ZpUkfcM.jpg?size=949x677&quality=95&sign=feff7070376125cd066e197dc23814b9&type=album',
            'https://sun9-56.userapi.com/impg/Wm3_GxOz9Uf9AKfykl7SF2c4SSe1Rr0rKThvIw/Q3DwlfeOg6g.jpg?size=204x248&quality=95&sign=9eff95bdb79a1f9bb17d0508528d2479&type=album',
            'https://sun9-80.userapi.com/impg/lPxV75tCguCalIjPoD42F_HTg-xDOa2u_fFkfA/ofioq8GZDBU.jpg?size=512x390&quality=95&sign=4b847ff47b0f37429da4d1c4d457c911&type=album',
            'https://sun9-18.userapi.com/impg/f7H-TA1O7v9wz8ygo0F-fh55Yz59mj_LM8OiDQ/EAr-25_nSjQ.jpg?size=1080x985&quality=95&sign=caf0dd2266fe1be4e5dd2108524b13ac&type=album',
            'https://sun9-47.userapi.com/impg/hIBcFOVo9VE3G6B7E9ejCKe7Z-vkuk4DbcJlZg/ogK0ZuFlRlU.jpg?size=320x301&quality=95&sign=28727c76de614737510b1651fa18d137&type=album',
            'https://sun9-83.userapi.com/impg/gKyeVmpCJE20EAwNCXBzksu2_TgkeWBekoSLCA/BVt-Wr1ww6Q.jpg?size=168x300&quality=95&sign=9f308a16fb8ae8b3cbe9332380bd6d81&type=album',
            'https://sun9-36.userapi.com/impg/sDkzuw4JmzeZSY9HYRnPAfysTWNHRVPG2MesKg/C9gwgkGxQGk.jpg?size=861x994&quality=95&sign=e08fef770d4589e20ee054dadb36a35d&type=album',
            'https://sun9-44.userapi.com/impg/wsUYlMATv1nLxYVrwj5kBvr1H7gQaxiQlrRd9A/ZtkVQ01jlaA.jpg?size=548x772&quality=95&sign=43acc28dfc1ff3e4299bb387e87ea750&type=album',
            'https://sun9-20.userapi.com/impg/HRBSKQib8fzjqhOWcAzeCvrZuNaclXFm8HdYBA/nACw5fQOQaw.jpg?size=1080x1030&quality=95&sign=8b73694a8798e574f526d11673ed6f0c&type=album',
            'https://sun9-10.userapi.com/impg/TCuD0MeQjYUo978bOMyfz6-QtB7GSJroI1s8jA/rCt0vFae53c.jpg?size=1080x1013&quality=95&sign=b43d1528deb1156b645f685aa0f37c25&type=album',
            'https://sun9-73.userapi.com/impg/Is7CBoNssIKpAB-RSyEJ747xS-xKlB0wJSfTvA/p1dkg5tm_wg.jpg?size=512x377&quality=95&sign=e4c59ddbabad923ace01baa4e6f7da9f&type=album',
            'https://sun9-32.userapi.com/impg/AOriz3Ohy2DDe6AfuzHd7m7Owb2EXVkVMOaEQQ/ol3aGQnR6Ho.jpg?size=992x992&quality=95&sign=ecf69e46833efd0d5b0afeddd7360c67&type=album',
            'https://sun9-58.userapi.com/impg/Ao5Xsc67Dc41vvqYYL6w_j2kHpeloZI5rU70lQ/frVxbgfWGXE.jpg?size=1080x763&quality=95&sign=19895fbc827f1239e096baae707908f1&type=album',
            'https://sun9-31.userapi.com/impg/9Kw98esVP1uqE-o6SaDZ2b2Rzm1QMJrtOqsDgQ/kFrYp5IcG1Y.jpg?size=1080x1061&quality=95&sign=c55f11c74c2fe59a088ef38c9f4c402b&type=album',
            'https://sun9-27.userapi.com/impg/J2-Fldk2p7R-qSna4vaTPY_-LvBYoO3q8IUO3Q/WPTaB_nEK80.jpg?size=499x349&quality=95&sign=72b83ef72492c19a972c063d7edb7a12&type=album',
            'https://sun9-39.userapi.com/impg/W2l4LcsJlWqhbEqBT5kj2IKnlZfY9LpUpTgJ6Q/FNlfbv5NPTU.jpg?size=604x566&quality=95&sign=472b8ca8803bbc9e50862a6d9380b447&type=album',
            'https://sun9-12.userapi.com/impg/E438uudr4lLlm9XoEr0w-OPXVXZmTymCz5VefA/EIC39yzsBIc.jpg?size=1080x487&quality=95&sign=3a6dc16d672d018d62a2346bf6a11f4a&type=album',
            'https://sun9-2.userapi.com/impg/7nP1cBOX67d1pswes30VBrcgaeZ0wOTRxArcqw/fGLlm2403fQ.jpg?size=1080x606&quality=95&sign=7b1f16114736b58d474d485815acfc56&type=album',
            'https://sun9-32.userapi.com/impg/4A4YOKbvO5fjchoyWGvDJgUiAhcJttg8z7l8DA/m9PkEV64SeQ.jpg?size=1080x1296&quality=95&sign=f04361e7348f8030c5135054b65e1d0c&type=album',
            'https://sun9-10.userapi.com/impg/ClgSZFyE3mPrqmaWGtEdLVFY8TxTZcUkfEE-ZA/VEYyD7Zm5Uw.jpg?size=883x864&quality=95&sign=5b4dc3cbd8223c2fcf5adc7c8019c6de&type=album',
            'https://sun9-46.userapi.com/impg/UPtC5jMcfGbq3KJ-3MxcSSDWPdImbdc0gKVKlw/5UDada-58Bg.jpg?size=200x161&quality=95&sign=d0b44ce2a431fc80a34394e7e8aa836b&type=album',
            'https://sun9-40.userapi.com/impg/45v2o8mDazPUnb1K3FfLN0RSECfxipiaxEQtAg/PcZct5KFxHk.jpg?size=875x800&quality=95&sign=67d387cff8bf6b593ee5c96500ffa392&type=album',
            'https://sun9-85.userapi.com/impg/sVves-AI_WWywnSLfLaW_R-QauNzGZyEt0lyhg/iaVv6Dtf4JA.jpg?size=600x717&quality=95&sign=92ad1ec7cd72e7a63bb4e6f4d5ce7f71&type=album',
            'https://sun9-43.userapi.com/impg/uCAkr2JtN9z3RY9_utLeNufM64yXhjQnDMO40w/vKhm7KD65l8.jpg?size=1024x888&quality=95&sign=f42ec3250c076229f651475e3f63e04d&type=album',
            'https://sun9-9.userapi.com/impg/isTOXIjEa6B74k3YmXiRtw2ZypWGITB3XmENXg/BxFQE6YcZBs.jpg?size=714x710&quality=95&sign=3c64201a71a20976d260d9cbc33e76ae&type=album',
            'https://sun9-86.userapi.com/impg/iJT431mNS_xQE-a6HuBC6imX2hEEhkdAEXYgbA/cgQv1wAYaVs.jpg?size=720x860&quality=95&sign=af1c41abaf3d0f72563a899bad884ae5&type=album',
            'https://sun9-22.userapi.com/impg/EF92cXapU_Shr0Y_DpjQbHZk5fJD-aETJyXP_w/Gs0oN9ALPVA.jpg?size=1200x1132&quality=95&sign=7f630910e46f50d0a06192b6e0eec157&type=album',
            'https://sun9-42.userapi.com/impg/Vadi4GIpREGw3Wjq_R9pPdntOJtiCGHogu9vLw/pnGOzzoL_p8.jpg?size=962x1024&quality=95&sign=c25adb78f6a0726b384d826bb5fc0d64&type=album',
            'https://sun9-62.userapi.com/impg/4xzIec7m_uzPWGzupZvmpIJD4zIHUc5iMu33kw/84K3HzEvuhg.jpg?size=1280x720&quality=95&sign=478365126948b1103882b101ee2e9110&type=album',
            'https://sun9-25.userapi.com/impg/AVtFmxGEwt4zUiFlCvGLe2RXgojHThXhOoRx1w/A4ZiAWnu9zQ.jpg?size=1837x1188&quality=95&sign=3e2c89a93ddf24187de2c31939fd4c1b&type=album',
            'https://sun9-63.userapi.com/impg/2D5hmXFQHoDtKq7bDOwa3xsG1YjYOKlm3KY9jQ/1FnK1tIsOek.jpg?size=1080x1059&quality=95&sign=846c40dfd7eea389c5b1e9cacaed7a9a&type=album',
            'https://sun9-32.userapi.com/impg/uWt7pCr03tnu4AxCgJxPe4z6AOYHjwC3ID7s7g/gZcZgTodoyU.jpg?size=1079x1075&quality=95&sign=74aef2f94991ff9be55519fbbf1cbf2b&type=album',
            'https://sun9-69.userapi.com/impg/2hcqsOh85YtUyVZo5vtn-tD3-cyXGV9yaFjWjA/HlBXKezU20A.jpg?size=976x1200&quality=95&sign=f8c8f97de62700943fe178d650ad90ef&type=album',
            'https://sun9-20.userapi.com/impg/mkbc3yDJA5TqNj0SprTM_TXSYjTwgdpcs14jTw/-FkkI9J8h_0.jpg?size=895x657&quality=95&sign=d225ce87fdb7ee19d0376c993777292f&type=album',
            'https://sun9-60.userapi.com/impg/ctOBVaLR93dQY5xTj0APHtiXRHcdwLAlfcSrTg/vCb_fFgeV6c.jpg?size=585x604&quality=95&sign=c12452383db1cb6499d183704e251850&type=album',
            'https://sun9-16.userapi.com/impg/wT5FZEdPG9tCbW2f6x7x7Tm3kBusVE04XLgOQw/x0iE6TXxTQg.jpg?size=827x827&quality=95&sign=ef60d3f0b9dcca485a084dfa718a7632&type=album',
            'https://sun9-19.userapi.com/impg/xGlGKJ8s7xTOQ55qHkvZ4e3HY7qxuiMgkugZPg/wXlfmk0IRGU.jpg?size=995x521&quality=95&sign=d89e654fbb8b73cc63628c16609d4943&type=album',
            'https://sun9-74.userapi.com/impg/gTgM3sExvrd5X08FEg853xcrD-jUWS3wepoTvQ/kCVeSQ7M-fM.jpg?size=544x604&quality=95&sign=331b9587fe935f9ed5a01d7c87aff032&type=album',
            'https://sun9-12.userapi.com/impg/zEVH-bMlaHMad_ajrNJbR14PzaJFWqfLqqTxBQ/1Z_YhTocaCk.jpg?size=1080x810&quality=95&sign=b85d79fc27dc62558bc20d68890201de&type=album',
            'https://sun9-29.userapi.com/impg/VV_befcVDArOJG26PmA7Mwc73mxDggMfKRIZQw/R6ueuebc7MQ.jpg?size=827x893&quality=95&sign=05fc4a0515f7402a039804496a292517&type=album',
            'https://sun9-12.userapi.com/impg/xaC5ueiPKrrwAeJ9_tE_IoKCoYrrSWVdFTAA_A/xoJRQxIwPJo.jpg?size=699x517&quality=95&sign=7e750d35d959b1e5d381b866385859ce&type=album',
            'https://sun9-40.userapi.com/impg/40-S1H7o2Gnm8lYcY6fCJ11UwxHP3b3xSMfKUw/JlQXSHlusPY.jpg?size=811x811&quality=95&sign=d88a3d9ef2209d1766c38d4329c13a2b&type=album',
            'https://sun9-68.userapi.com/impg/SCJYranqdRDmfrNqyANWjRvWWsYMvgXxRU1boQ/YlM2_Y8v9w4.jpg?size=604x604&quality=95&sign=c0bc9635c3f0221329dc29439903c346&type=album',
            'https://sun9-44.userapi.com/impg/oVI2I1s0bRV7e8-2P_k3fXU5Vsb68v3VvsuuOQ/HjPHdozHQL0.jpg?size=1080x1060&quality=95&sign=cf63f3b126c4bafa23762fa48d0994bf&type=album',
            'https://sun9-78.userapi.com/impg/ZYip-iKrt3JSqALHn6Y_ItGiv--H90jnaYwgjA/jg4SySgO3s0.jpg?size=811x1015&quality=95&sign=c3893e7169ad07a73d9bac290a4abf54&type=album',
            'https://sun9-30.userapi.com/impg/reAMbimSawWOeooOtcvPtR4608IhNk2luE7vtw/pCXGwQsUXs0.jpg?size=592x604&quality=95&sign=c4b87e08f5184538b7c5198166174b46&type=album',
            'https://sun9-20.userapi.com/impg/YR4Y93cF9OkHhKEiNx1FQF2HDvY6JJCI2lbLXA/PgbIvoDlmBs.jpg?size=1200x675&quality=95&sign=b405e07cdbedaa5375b9345cdc45e0b4&type=album',
            'https://sun9-31.userapi.com/impg/SrQbfiwKw144tIruJ2VNfX_b5_U1h1jkUeR1eg/Z7nJPtVP3Yo.jpg?size=759x711&quality=95&sign=1e9da9d738cf5e8f5ce8b565f45e3b3a&type=album',
            'https://sun9-6.userapi.com/impg/NgvFHXAmyxrhzpqm3Qr6ue2XefWdgwQGrOQERg/qWiDA6rzGxY.jpg?size=1046x1200&quality=95&sign=fa3d3793c5607d14fed43691a12961b1&type=album',
            'https://sun9-79.userapi.com/impg/2ehabb4kSTr0mgeNKTKhWR7_nQ9BPO7cl6odCQ/QvZf_IhrJes.jpg?size=604x585&quality=95&sign=d4c8093e436db8bb6b215ff721281a12&type=album',
            'https://sun9-37.userapi.com/impg/S8PbjwLhrHVaypB6a4wPbBNWxZrzf2Tf2_gX_w/apIg89oxkac.jpg?size=800x450&quality=95&sign=c41d6a034b4e9eb29f542d7db5750d02&type=album',
            'https://sun9-86.userapi.com/impg/ZrCX9mngFCpOpdP5IlTx2idquTjRM6rUJgJm7g/1ukkHLqjLU8.jpg?size=780x780&quality=95&sign=7b4fde8e76089d7c4df9a1f2b7fad78e&type=album',
            'https://sun9-57.userapi.com/impg/7Jsdo98NFuKoD746xX4K4tbIAxxOZ370blV0qw/nh1HfPUUfnk.jpg?size=1080x1079&quality=95&sign=14720d1db9f57858fa08a92818bfeab3&type=album',
            'https://sun9-2.userapi.com/impg/AoMNSx9xgDYHtsoFaLlv2gabJLFWqbOJbZeNjg/o6uUsna8AGQ.jpg?size=1080x1135&quality=95&sign=28648a9d2212c04a960bb73be00e6941&type=album',
            'https://sun9-4.userapi.com/impg/XBW2yoyBTIS5iS5yoFeGPsIZDnw6qJcjcTi1qg/N-6asyn7ARw.jpg?size=1080x1350&quality=95&sign=a6451e55d747064dc04002046ba99bc8&type=album',
            'https://sun9-61.userapi.com/impg/ygODGmHY4X7pwMkSWpg6-EW_cckur6sD3WqkIA/ZXE3u5tYZgE.jpg?size=1080x753&quality=95&sign=ff44dca6bd5f675b0a1a01d0efc6de69&type=album',
            'https://sun9-29.userapi.com/impg/LTWZgoH0LriyMuq-WaMKGx726OMvXlJwAVpiPg/znFsWU-VYWo.jpg?size=1024x683&quality=95&sign=c6894421025ccb2cee6618873985913f&type=album',
            'https://sun9-80.userapi.com/impg/QOhONM8oZPEGZeTd3lEWbbgicB35dkGfiez-Dg/Oa9YCwyKNwo.jpg?size=1280x720&quality=95&sign=bc473352eadebb1ccc11cb6855b75a1f&type=album',
            'https://sun9-62.userapi.com/impg/IjRhHSoxyTOQHave0APf1Ot_aZKOHalvB5XTZg/DS6Gww4KKeQ.jpg?size=1280x720&quality=95&sign=f99adf629df9b70a0a49b9271d729c0a&type=album',
            'https://sun9-53.userapi.com/impg/CInclCObZgrSD35o-okP2qJ7IPLRUygwEqRBfg/sfoeCU6Ve4U.jpg?size=1280x720&quality=95&sign=3759f650bb4467da2c0faa6afe095419&type=album',
            'https://sun9-65.userapi.com/impg/eTZcgXPlVAv5bOQ0wyLxvbu_Y1q42Scq3Qc9zg/jf1AjQR6M30.jpg?size=1280x720&quality=95&sign=0ccc5571ad62129daf7a62e049cd5ee0&type=album',
            'https://sun9-69.userapi.com/impg/jnCJlrL_oI6wdygekKscmTc_MNt-CrzsakAxtA/Uc62C2EgpoQ.jpg?size=1280x720&quality=95&sign=4afa43b97486bdf97677c14c5428c138&type=album',
            'https://sun9-15.userapi.com/impg/i3xG0Peh5MO2j_VlFV7AkVVWQrkBaQ1VXFMkcQ/wstNjEw7WQk.jpg?size=1280x720&quality=95&sign=c9d3e8d05b9f230f99cd8e45af49f1d7&type=album',
            'https://sun9-58.userapi.com/impg/xZLJm3cdvfSw8c99LdVVEZVROx-8QsAl_SQLBw/IggldVCn0FE.jpg?size=1280x720&quality=95&sign=60c7f17ade310ecd579619c57e2dee6c&type=album',
            'https://sun9-31.userapi.com/impg/FyhXDAGPrNpmoFuApAhb_wyZh_Fx_j_loShBQw/BwnpzUplJmo.jpg?size=1280x720&quality=95&sign=56cf978bd8438b1be331adbdd1fc5769&type=album',
            'https://sun9-14.userapi.com/impg/Izy1q9NbKCM0HXx22AVTasf7DeF3BVnuNiWrGw/MC9TPL2NsoI.jpg?size=1280x720&quality=95&sign=8adf7a17950518a48ccaed7d71b35ba2&type=album',
            'https://sun9-73.userapi.com/impg/yqvNG9fp-i6g_uXVyd-K55tcR66uDhaqic08gA/Y5GRaT_GzKU.jpg?size=1280x720&quality=95&sign=5e89689bce22ead9f4a93c6228697585&type=album',
            'https://sun9-82.userapi.com/impg/0I2139ismi_WOcJi0dIP1WPY7KiIKp7fBxrQfQ/00TOZNp0Tcw.jpg?size=1280x720&quality=95&sign=832d261692aeb88b9a510a831783b35f&type=album',
            'https://sun9-40.userapi.com/impg/GkOghSE6-_WGqwRcfu_EQOWDwqRYtyRUP0A39A/GPqbk3HC29I.jpg?size=1280x720&quality=95&sign=90a99ba20989b5c6e467d42411ddbbb7&type=album',
            'https://sun9-86.userapi.com/impg/b-UZS0yCfu1xBkDWLYCfejOpkplBmySyVyuaLA/PKD1vJDoIgA.jpg?size=1920x1440&quality=95&sign=13f5560f44a9696e5c543b95b2a47da4&type=album',
            'https://sun9-53.userapi.com/impg/in3xq524jNrwmP7JwNXQ0I0hbt0qH0YlHG7Ttw/oRSE570mUY0.jpg?size=900x900&quality=95&sign=e0d661313240fe08773730eb4a9f3b75&type=album',
            'https://sun9-13.userapi.com/impg/vDQNNrpLAkDwAT9oZgQ3WBvV2NV8pjfxOIGJzw/6r6kfsmaR-I.jpg?size=900x900&quality=95&sign=c4c64873148c700a584747926fa31a2e&type=album',
            'https://sun9-18.userapi.com/impg/GoeDahirBwbVaK83uE1JV4Weir9omVdiMV_SDQ/GgDBx-tjr6I.jpg?size=604x604&quality=95&sign=2e9d60027c4261fcfec08db666b01924&type=album',
            'https://sun9-54.userapi.com/impg/3Iy31W9UnbkDtRSxD6j_tYp_ZtBUY5C6wZ-MRg/N9ZCnzgzTO0.jpg?size=759x544&quality=95&sign=3c25e6ca5e5251909c060417aab936d1&type=album',
            'https://sun9-88.userapi.com/impg/wF0wbFavyOQPnhdwZsuwB7QEd3vsOtSBNcLcRQ/KSNAc0jgKxo.jpg?size=698x800&quality=95&sign=b4b7ac34b19ebdb711440f8589230961&type=album',
            'https://sun9-36.userapi.com/impg/6r3RSVYt8n1LefMn1irFO4rJesGvuKudTUmKWA/0DyQ4tKc-5s.jpg?size=657x800&quality=95&sign=c7c3b96c21b2648c3c96f0768f5653d7&type=album',
            'https://sun9-59.userapi.com/impg/H-oqpBvOReHvVxj3vA_HhVkdtQFiJEosSznNog/FvlmEOe_l3Y.jpg?size=666x627&quality=95&sign=ae554a4d79b39b181d9fbd75de3fdee5&type=album',
            'https://sun9-20.userapi.com/impg/BnkGAOVRc9DQ_wXZQDT4SLDsvP_g0NdWNuQjmA/ty3ndzXCSHU.jpg?size=650x759&quality=95&sign=67da885a97e4b5a6d9e5f9706da890a5&type=album',
            'https://sun9-45.userapi.com/impg/Anfgti59rwIjcfh_76GthHYZDh8Td7y-X1bgkw/u9hsWIYnoVs.jpg?size=712x647&quality=95&sign=3046e5c9f110d52932afd5724e9b9e53&type=album',
            'https://sun9-52.userapi.com/impg/4EcaG0UPLjEUiRN4ddIlGIpWRW3MMvliWh908w/p8wvVFi52A8.jpg?size=480x256&quality=95&sign=a2c8352be29f5ce68fefe0011c4e3ea5&type=album'
        ]  # links to all pictures
        channel = client.get_channel(786670178805088259)  # here the id of all channels ds (using []) (this is the crutch)
        await channel.send(random.choice(imgs))  # displays a random one picture

    gachi = message.content.lower()  # converts the user's message to lowercase
    find_gachi_words = False  # this is what searched for phrases (words with a space)
    for item in gachi_words:
        if gachi.find(item) >= 0:
            find_gachi_words = True
    if (find_gachi_words):
        img1 = [
            'https://sun9-41.userapi.com/impg/zw1y8dgW3twimJxYM9tCBOoz7lA64ItFPCNt1A/M6hr42iEHe4.jpg?size=768x759&quality=95&sign=4d2cdfc4818cc42f5065601e0ba9f192&type=album',
            'https://sun9-43.userapi.com/impg/uyAHgkbxVEqHcfEjY7Re1cLCTC1pK5wg_qnlFg/gWc1tF_tCxs.jpg?size=738x713&quality=95&sign=922d6466d404f5bd5cdf8e8456571926&type=album',
            'https://sun9-15.userapi.com/impg/mpYcV9YnfIhYsR5CeI2yGZxuZXlDiWcQoaJStA/xIJtDetwrL0.jpg?size=1080x1470&quality=95&sign=77bccf24bd7b12b1d80b64c863622e33&type=album',
            'https://sun9-80.userapi.com/impg/DLk1otbWpVmXpnYrWHXNLgPSB-xwz4Rx7EErag/esWmb0IzGe0.jpg?size=1080x738&quality=95&sign=328707e660156146f2693b7f76b52a2e&type=album',
            'https://sun9-65.userapi.com/impg/jrghkAIXlxDeIweJcZemq0ZUUEwkl_uLTb23Jw/TVytUlmJ38s.jpg?size=320x180&quality=95&sign=8d53e2383daa31b8c901bb772b1d4353&type=album',
            'https://sun9-17.userapi.com/impg/Y9I7YxF_mSoJwDAlDfcV0Y69aJyLMHwNrNBNsg/kFiY2WpSQrQ.jpg?size=604x456&quality=95&sign=dfb666e8ce45b181f184f8d243bb9580&type=album',
            'https://sun9-83.userapi.com/impg/qhEeaRuyenpBZ1_o4ghZRgJ-xuy8GO6Aqb0kOg/VdDmbFgVSQI.jpg?size=1000x562&quality=95&sign=17d718daa1651b5818f6f9c6fe1b5cf7&type=album',
            'https://sun9-84.userapi.com/impg/tS1qqdhawrN8IBq_tbrlSaZprgoB4CStobulxw/_MnS-gY2Ipk.jpg?size=1920x1080&quality=95&sign=cf0a84ecd9a12d9178374955d411a011&type=album',
            'https://sun9-57.userapi.com/impg/99BDUvxwQrH0E-zUS7mjIP8E6HmDJPGYpwKllw/gRL5LFmplVE.jpg?size=1000x562&quality=95&sign=d9140d19d8abcefe86ec3bd0d3a3e2d0&type=album',
            'https://sun9-69.userapi.com/impg/CeF4niHmcYXWXlG1W_Qaq5HJaMGyaBbYDacwtA/kom36JTE8_0.jpg?size=600x785&quality=95&sign=2ec6266c4096be65a7eca00b0f515cad&type=album',
            'https://sun9-46.userapi.com/impg/Dgnm3LNOioQDeTkMu_IqfIIaUOpLiiufkEvduw/5bLBJDQgXNs.jpg?size=1000x579&quality=95&sign=1092031de09b96b7ba71abb081df97ed&type=album',
            'https://sun9-31.userapi.com/impg/eCPMOww7pq6asa7tkF1v2bQYZkbSjj7kS1KZwQ/vAvqJcizUoY.jpg?size=858x653&quality=95&sign=52da161c78f2a807e0822ba1ef86388c&type=album',
            'https://sun9-88.userapi.com/impg/pGQVhRXnrchGfh9hmbGnAylbdIngtTeOgSM0eQ/T7Ar8qSxv3U.jpg?size=968x686&quality=95&sign=305118ab3e4606f52f61323f07adbed4&type=album',
            'https://sun9-40.userapi.com/impg/owtAVD63x7frrVLz8u-hBuf8MtL_Lk6zblVrOw/qK6Zs1jsYhw.jpg?size=1920x1080&quality=95&sign=5e8c52bd7f5ced292ed164098a162bc9&type=album',
            'https://sun9-12.userapi.com/impg/aj8K7Qczz0U4i3-ciTEfgd38mwsMtxHjfkeFNA/zgZsZU7lm7w.jpg?size=960x627&quality=95&sign=c7f61e4b8df809bfe780c53b5311cf96&type=album',
            'https://sun9-10.userapi.com/impg/DzwM-GXAX1XmClVwHcmqVEEFwQxAaU79l7x00w/63ScFSL1ddw.jpg?size=800x451&quality=95&sign=102b77afbc4aecadbc31874f631d3a9c&type=album',
            'https://sun9-11.userapi.com/impg/B0OETNmne6xSo4A-jMLIcKdQAUdg48ACcV9Rjw/l_SMtiMb3dU.jpg?size=1280x720&quality=95&sign=2871befcb00cefe3195520e5df1b3bd2&type=album',
            'https://sun9-88.userapi.com/impg/R7cqHfIgk2jEOXN5fven_wCX_vFVQw7jkZJ35w/KAa5QoSLEeQ.jpg?size=1280x720&quality=95&sign=c3de7dcc244dbff5c5bdd25f5f99a3cc&type=album',
            'https://sun9-73.userapi.com/impg/clQ7FQDYOQ2GbhztlzTcqmkcbeuGG0iqEwlJ_w/B4znajuyE6Q.jpg?size=1280x720&quality=95&sign=573bbfe3545c347ce046f17a868bd181&type=album',
            'https://sun9-25.userapi.com/impg/FgPY6TBzlmEkXS8UjoL0agkgJ_DkFuWSwZc98Q/r6uufy8Jdt8.jpg?size=1920x1080&quality=95&sign=a2e56f06e6d89c0a92bf5e6ff54691cb&type=album',
            'https://sun9-21.userapi.com/impg/Xswe-EI6TOKsWNzYiJynq_xFVf6rgeW5FiE9pA/TOfhP34MXOw.jpg?size=1920x1080&quality=95&sign=5da791ad83b1c11c3f8359468ff1c9eb&type=album',
            'https://sun9-6.userapi.com/impg/-Jwl-F5XRmQ7GPYiAT63dirN3BFGCEDpe_9ZzA/zjKvTBaA5Uo.jpg?size=1920x1080&quality=95&sign=aa4a40880a60204f1e1982f1a7a6ced8&type=album',
            'https://sun9-79.userapi.com/impg/e0ZzcfMyEll2cACUpnX5nNcwNz5hw4uotllPXg/6hxNFH_dtlM.jpg?size=1920x1080&quality=95&sign=4fcfed18e91784a92c44e6fe50f9a168&type=album',
            'https://sun9-29.userapi.com/impg/0efgKyxQkDTudzv8r4bpfNoXeiUhaZ0aoI7WjA/Wn1zuTbtt5Q.jpg?size=1920x1080&quality=95&sign=4e30964a67ae5cacc0b719524220f56a&type=album',
            'https://sun9-81.userapi.com/impg/oVM31zgyIEQE9wYO9nLoUvRobORbfD3sYOILMw/EbvJoxjmYjg.jpg?size=1920x1080&quality=95&sign=4899a925e719fb24ff7617318c4849f3&type=album',
            'https://sun9-73.userapi.com/impg/MkwYrZRWDCMmhC_H0vFenAjxPnfkAD1OJxlXoA/4zDAeDfrlTE.jpg?size=1024x895&quality=95&sign=34467bf9006610b28b294e305a5867d9&type=album',
            'https://sun9-22.userapi.com/impg/NrkwHqkCeC6bMqqTsuIHZRktt5wIW7Lmenqi7A/16VECQI-7hI.jpg?size=1280x720&quality=95&sign=d2e993cc3a5c14097ea932266354fcd3&type=album',
            'https://sun9-50.userapi.com/impg/6l-r6JqKeKtDTpvNSxGZOJXEdMpTW676xBW_HQ/fFpoAJGn5-w.jpg?size=1920x1080&quality=95&sign=699f8c9714f5f1889d675f6d3b7f9b26&type=album',
            'https://sun9-18.userapi.com/impg/-nM60PlL9Ata3rkdnWm6dkt0HTPIiWUSppxx5w/sg1jATRBoKc.jpg?size=929x702&quality=95&sign=55b7ca5404274fe5a6b3c25571536696&type=album',
            'https://sun9-55.userapi.com/impg/c49IKi17LHwaYaq5hPkVUG6kn57ZBZvfee1kXg/ZqW3KNQXXh0.jpg?size=864x884&quality=95&sign=bae1004da66b65c335d6188f9ff5036e&type=album',
            'https://sun9-8.userapi.com/impg/HJeA_qIL5GSyXVtNlThnM52z7KKgB2Rh0xi7KA/YJ_rS5-kc3c.jpg?size=1240x1754&quality=95&sign=c249680eec84213d06344d96cc88b263&type=album',
            'https://sun9-5.userapi.com/impg/gLr4ZtP9jUZESiXffDAiCy7QbZdAVaNNsKtiQQ/B02hOf9x2_M.jpg?size=604x604&quality=95&sign=5a842b2b032fcdf98343b313decd08ef&type=album',
            'https://sun9-88.userapi.com/impg/43sXABo72I6dgZ3lZX4VK9C_qgN-HndPbZuGKQ/9-9aiUiz3lc.jpg?size=720x404&quality=95&sign=5dbc2c509f21b30660b08034e1f596b5&type=album',
            'https://sun9-31.userapi.com/impg/vrnyezSinO16fEI1Twfuy5G3yOL9T95O5gO5mg/ozPPsPyTcTE.jpg?size=1200x630&quality=95&sign=f2953255dfa3308aba23ed52f4599934&type=album',
            'https://sun9-21.userapi.com/impg/zDDWCireEh2H_iON5aFmPO0nIN-xDuE99zMaSg/PA0pTEHH2ts.jpg?size=1200x935&quality=95&sign=04d13cf0b6f7c983dab4328c8f4db6aa&type=album',
            'https://sun9-32.userapi.com/impg/Rm1h2knsxATzbdztwebMtcGRnLm9VQC1WQRSrw/WCbvY3gQ0U0.jpg?size=870x1200&quality=95&sign=650a201d0b355a7f8f88a24961a78860&type=album',
            'https://sun9-9.userapi.com/impg/SGNGXxhFo-WAd952CYNMG43PaOCbiMZO-RnMCg/p41FE8d4RiY.jpg?size=700x700&quality=95&sign=e8068c7a7d1df98d90b04109007b2360&type=album',
            'https://sun9-36.userapi.com/impg/LMZ7CmCAMJWSV20XDuzh03BtHkg61OtguYUGJA/cDbsvbeERAw.jpg?size=1200x801&quality=95&sign=50e296d9a8b3223bd53f8b846357e5e0&type=album',
            'https://sun9-68.userapi.com/impg/3oS55sCciugAubxekNZILphgEbRWuVnxIO-t1Q/yZ-lzy_DVeM.jpg?size=1200x900&quality=95&sign=8c1ac6858ba04037f649abae3cc39c19&type=album',
            'https://sun9-55.userapi.com/impg/Plk9tMEoUgmSZjicKF9pXLbv8wzG3i4_MnLb_w/gLnemOt701g.jpg?size=1000x582&quality=95&sign=791950c1420004e86583f8b0cc13756e&type=album',
            'https://sun9-55.userapi.com/impg/wfuK_57cBm4ghTTw9ZFS6rjj2gQB6lAtb0aDmg/GVaWAINoOXw.jpg?size=1280x720&quality=95&sign=983388720f43d65f6dac1f97f7bd7ea4&type=album',
            'https://sun9-5.userapi.com/impg/x4g7HRqDWu_qBcqEdm88VtoBtu1HXiAYFHuXDQ/J1Gr7SWhW5o.jpg?size=640x640&quality=95&sign=5c685ee5daebd0667e325e5851f0b151&type=album',
            'https://sun9-4.userapi.com/impg/Zpe_IGFZ11G1ix7o3ryNhnI7MyxbIr72ZQeJSA/DTPXOd1m4do.jpg?size=1280x720&quality=95&sign=76c7ab74c3247f71fc66393ab318d754&type=album',
            'https://sun9-51.userapi.com/impg/8c3BtPkVoDOT8_Xr_ll8EXz1xQ1-lnIF2oOJ-w/yTW67KVr-JQ.jpg?size=1280x720&quality=95&sign=a91afe881e4286d0d51db7565266e57d&type=album',
            'https://sun9-28.userapi.com/impg/4Y3zELzmFch2ZJztqsCiRA9bADWKXhLPPgeyZA/tBaPxlwk2L4.jpg?size=1280x720&quality=95&sign=7decbe628f332459da195844f02285d1&type=album',
            'https://sun9-77.userapi.com/impg/8LNiuHC1elwOhnHECbY3IeMf4Qh32mZ7L4J4-g/ZdVr6NLRJSM.jpg?size=1280x720&quality=95&sign=0ca4a956c73a3751c88fbb37affaabbb&type=album',
            'https://sun9-12.userapi.com/impg/ugbsx7ehzKB87DTSUGNj7ZRe6WWF47yWB-U4dQ/ilVtf6NdIgQ.jpg?size=1280x720&quality=95&sign=a3ecf69c4c78e78dcad74ffdfe6f237d&type=album',
            'https://sun9-59.userapi.com/impg/hZ_efHYPPn3Hei48CRADM-kYrzi--U2AA4GBEA/mumTQI_7GgM.jpg?size=1280x720&quality=95&sign=19ce094fb8bfa38be432d0a5fcb99416&type=album',
            'https://sun9-12.userapi.com/impg/IctZwslJW2ugdoqFinJQ7Cz6taush9IlHqHnAw/15PXhZf39Eg.jpg?size=1280x720&quality=95&sign=3452473c86d9459ef68206de0c993c08&type=album',
            'https://sun9-54.userapi.com/impg/SwM7Vq8Xa57SzjMImcgXScleewuhj8FzvOQQLA/hwikiGGgeOc.jpg?size=1280x720&quality=95&sign=9e0e44518802d5364802ed1f398a7324&type=album',
            'https://sun9-17.userapi.com/impg/G_73iye7jXmt63VnRrcW0r1jmzwMnLY9ul9npw/hr2HTs1ga1M.jpg?size=1280x720&quality=95&sign=30645ad90ffa6b8d60d600a8b6e9f286&type=album',
            'https://sun9-56.userapi.com/impg/nVEgOVP-vxB2pM0VMlHFbOo6B4fh58uKNimwwg/zUvyO5UqGJA.jpg?size=1280x720&quality=95&sign=129433ddbe23d4c6ec4b335d33e71c02&type=album',
            'https://sun9-48.userapi.com/impg/RDG7VsARE70gLUMfGTfNkKycRlNzZGk4n7PJeg/ix_COUb4RvU.jpg?size=1280x720&quality=95&sign=ddcf855aef919bea575f8029d15db370&type=album',
            'https://sun9-39.userapi.com/impg/7BCc2OUURHOzSYFohyQNoYw8uFCNCR-tVu5VmA/mv9R4qvX97s.jpg?size=1280x720&quality=95&sign=787c0414297ec39c055d173c34b8f330&type=album',
            'https://sun9-88.userapi.com/impg/huoSvsWXDq_D2YH1h6XZFflUGWyCHJsM8O8RAA/K7ZH4T8Znlk.jpg?size=1280x720&quality=95&sign=48e22dd5776e581cbaf44386ef520f27&type=album',
            'https://sun9-24.userapi.com/impg/YPFudadLAm-pZNPJMtcI6hRKNhezxfaqz26sGg/rNvbZ40Xrdc.jpg?size=1280x720&quality=95&sign=9ae85ef4602efa5405aae0e9c0dd9162&type=album',
            'https://sun9-12.userapi.com/impg/I-Q4MQQGkgfeuQbsRX5b7A0QAo9uobvJZs3clg/vMOW7xp1HrY.jpg?size=1280x720&quality=95&sign=1de18746188286421504fc92bdf62218&type=album',
            'https://sun9-84.userapi.com/impg/1pV_ocebjEBaSNtpu3qZfyxarVryC7ymeHSRrg/K7YLUa-ftGw.jpg?size=1280x720&quality=95&sign=e06b10b97e92a362429896bae1c73d47&type=album',
            'https://sun9-3.userapi.com/impg/_n1xHAQyOkCiLwRjnan1bTZUi9VJmMkKapzZ3w/OyJ7lnvqWNE.jpg?size=1280x720&quality=95&sign=82ecc898e57b5d0044714fd4202a49c1&type=album',
            'https://sun9-24.userapi.com/impg/3uA99ptDThC1ix8IQtb9eSHGzwzPuKOMm7zEMQ/d69XMvDc3tg.jpg?size=1280x720&quality=95&sign=6dbf8a668b6a2d55e562933193438fa3&type=album',
            'https://sun9-44.userapi.com/impg/Oa3Ur4SFvUFRrS1u8NWp2Skas1zntGnO1h9P3Q/k-IfpwM1xRI.jpg?size=1280x720&quality=95&sign=da2c6bb11f177ab1056c4e5a3edc5b3b&type=album',
            'https://sun9-48.userapi.com/impg/_tlT_yjcpaMveRRs2d7nfhjiY0EoHs2AtRIsOA/HFIl6MxPZHg.jpg?size=1280x720&quality=95&sign=79535c45ddd02fac07fdae4dc1958fa1&type=album',
            'https://sun9-80.userapi.com/impg/kblU7IyfGbJnm4u7DQe_LhqCeosIDVVnMjHw2w/0SrL10ftdRU.jpg?size=1280x720&quality=95&sign=dc197001721bdb68a10abf404b3abe6d&type=album',
            'https://sun9-87.userapi.com/impg/q7lm60xtwAX5lwhWXImRK9hgb9ew7aCxLGzC9w/alqhF2Q6pKs.jpg?size=1280x720&quality=95&sign=5698f09860b494ea5dcb3bb7e1b38926&type=album',
            'https://sun9-48.userapi.com/impg/NNz6dmjRXuSizioIKMoxil9F2-dycyx-KP9ssg/peaktCB1dIM.jpg?size=1280x720&quality=95&sign=ef2c80186e5af4fa897ffc50c8ef0605&type=album',
            'https://sun9-43.userapi.com/impg/Ay2DzyvzZrbibMf01cEl5u0oxQKulTWyDVhxSQ/lg_Yyhe1fVY.jpg?size=1280x720&quality=95&sign=d5086d9015e0a0b7d55dce8bb86e820d&type=album',
            'https://sun9-83.userapi.com/impg/r6SDGgmc4qgCCaxm4yADW2XhpOMV1Q9UMEpE6Q/kHYLyF8NzSk.jpg?size=1280x720&quality=95&sign=7abddb668f73df8740f5122af855fd17&type=album',
            'https://sun9-33.userapi.com/impg/qS1A8Yuv7ATmH1C8FohVy33usCOnMC_DPbas1w/QgwtwftxIkQ.jpg?size=1280x720&quality=95&sign=bf167f6dcf61a40e783417d71995abf8&type=album',
            'https://sun9-8.userapi.com/impg/YSOnf35KbcOvnvxxxqIKMIK-FRUgsOVkURpPIw/nPPTBFFS9iE.jpg?size=1280x720&quality=95&sign=e4efabbd4490de542916ce84c29706e1&type=album',
            'https://sun9-9.userapi.com/impg/YvyI82Ol-k2dTEigmxYPlgaSmvNFYcppaqlWCA/ZS7PifBXt7o.jpg?size=959x719&quality=95&sign=0ee252870b1b638b526b30c0c7d94712&type=album',
            'https://sun9-7.userapi.com/impg/zaOs8E6kJ3gXfqbDD6sN4nPaOHtV5SOWmlTTRw/WZ-krUWilBA.jpg?size=600x350&quality=95&sign=28540ef0829d1002cad94918e3667664&type=album',
            'https://sun9-41.userapi.com/impg/3iHHaqh9RZknoYK66HZaZ3DiHwZZ9RMq6aqtJA/TWXBOywMz2w.jpg?size=1200x628&quality=95&sign=e9c5d417356ab05e732457ce627791b6&type=album',
            'https://sun9-23.userapi.com/impg/1Ha9FdLp32_xPFCGilnFnZ_lunC5tSGUnnHUUg/h_wpufd3c0E.jpg?size=1100x1080&quality=95&sign=bc9e8f631d99af5fc174c76fa238d1e0&type=album',
            'https://sun9-42.userapi.com/impg/QdzgzhtpYCRBUGF_NpA3FaJeui3CKHw0WAJF5w/ltip6b2QNgo.jpg?size=907x985&quality=95&sign=7cf2f660c2af5dd19d759cf2d058755d&type=album',
            'https://sun9-27.userapi.com/impg/KLjmFLg6r3TgLqsTB2QphV5E1xsku4DlkjCb9A/1MAbxkpD3OE.jpg?size=559x800&quality=95&sign=5fd28f6b37315be5e4e5be52ff40ddcc&type=album',
            'https://sun9-6.userapi.com/impg/fbPCexNvF5bhDnLVfkUFTk_TqztB1kVm2Nos7g/SCsKMPNuHag.jpg?size=900x900&quality=95&sign=dded23c788147dcc2aab7bc68dbe3a53&type=album',
            'https://sun9-88.userapi.com/impg/bquqF5EwuX4lvu3yZmji-aI-QXOvhdIoPQB5Pw/M_Zpc7usxkE.jpg?size=1270x856&quality=95&sign=e94510fd981e8816dcd8b60d9de74e71&type=album',
            'https://sun9-14.userapi.com/impg/oVq73nnMoD0J28osptkRMvw2VbAaFVO3MtJ8nQ/SAlL-Lkyt9Q.jpg?size=1200x904&quality=95&sign=ad4b513f7fa107440002a207b9f19add&type=album',
            'https://sun9-80.userapi.com/impg/nhmgMhX7R2OPrdkIywoKU12mf0Va-njbTbtEqQ/YDElDrdUdhs.jpg?size=1920x1094&quality=95&sign=d6d5b9c3ef9bd72418c045a7b35dd452&type=album',
            'https://sun9-35.userapi.com/impg/ylKom2w145p03EfhcMFjjRULkO6Md1y3hX1RFQ/09Bc73-9eBA.jpg?size=1200x1200&quality=95&sign=b4c714d095e6912ba85ea35ef891f665&type=album'
        ]
        channel = client.get_channel(786670178805088259)  # here the id of all channels ds (using []) (this is the crutch)
        await channel.send(random.choice(img1))  # displays a random one picture

    await client.process_commands(message)

@client.event
async def on_member_update(before, after):  # function that does not change nickname
    n = after.display_name
    k = before.display_name
    if n:
        if n == "Вова Вист":
            last = "Вова Fist"
            if last:
                await asyncio.sleep(300)
                await after.edit(nick=last)
            else:
                await after.edit(nick="NO STOP THAT")
    elif k == "Вова Вист":
        g = "Вова Fist"
        await asyncio.sleep(300)
        await after.edit(nick=g)

client.run('Bots token')
