'''
!λͺλ Ήμ΄
'''
import discord
import time
import json

token = 'ODc0NjAzOTYzNDk0ODQyNDI4.YRJYag.dnttO9TN5VVDuB8WcltlPxm88QQ'
admin = '! ππ π£π ππ π₯'

def times():
    return time.time()

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_connect():
    print("ONLINE")

@client.event
async def on_member_join(member):
    with open('./setting.json', 'r') as boo:
        data = json.load(boo)
    setting = data['days']
    setting = int(setting)

    created = times() - member.created_at.timestamp()
    created = int(created) / 86400
    created = round(created)

    if created < setting:
        embed = discord.Embed(title='β  κ³μ  μμ±μΌ λ―Έλ¬', description=f'κ³μ  μμ±μΌμ΄ {setting}μΌ λ―Έλ§μ΄λ―λ‘ **{member.guild}**μμ μΆλ°©λμμ΅λλ€')
        embed.set_footer(text=f'{admin}μΌλ‘ λ¬Έμμ£ΌμΈμ')
        await member.send(embed=embed)
        await member.kick(reason='κ³μ  μμ±μΌ λ―Έλ¬')

@client.event
async def on_message(message):
    if message.content == '!λͺλ Ήμ΄' and message.author.guild_permissions.manage_messages:
        await message.channel.send('**!μμ **: κΈ°μ€ μμ±μΌμ μμ ν©λλ€\n**!μ€μ κ°**: νμ¬ μ€μ λ κΈ°μ€ μμ±μΌμ λ³΄μ¬μ€λλ€')
    if message.content.startswith('!μμ '):
        if message.author.guild_permissions.manage_messages:
            j = message.content.split(" ")
            try:
                edit_amount = j[1]
            except:
                embed = discord.Embed(title='!μμ  [μ«μ]', description='')
                await message.channel.send(embed=embed)
                return

            if not edit_amount.isdecimal():
                embed = discord.Embed(title='!μμ  [μ«μ]', description='')
                await message.channel.send(embed=embed)
                return
            elif edit_amount.isdecimal():
                with open('./setting.json', 'r') as boo:
                    data = json.load(boo)
                data['days'] = edit_amount
                with open('./setting.json', 'w', encoding='utf-8') as making:
                    json.dump(data, making, indent="\t")
                d = data['days']
                await message.channel.send(f'`{d}`μΌμΌλ‘ μμ λ¨')

    if message.content == '!μ€μ κ°':
        if message.author.guild_permissions.manage_messages:
            with open('./setting.json', 'r') as boo:
                data = json.load(boo)
            d = data['days']
            embed = discord.Embed(description="")
            embed.set_author(name=f'{d}μΌμΌλ‘ μ€μ λμ΄μμ΅λλ€')
            await message.channel.send(embed=embed)

client.run(token)
