#導入Discord.py
import discord
import time
client = discord.Client()
bot_name='喵喵'

u=[]
b=[]
def setting(s):
    t=s.split('/')
    return t
    
@client.event
async def on_ready():
    print('目前登入身份：',client.user)
    game = discord.Game('喵')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.idle, activity=game)
    
@client.event
async def on_message(message):
    msg=message.content
    if message.author == client.user:
        return 
    if msg[0:7]==(bot_name+' add '):
        msg=msg[7:]
        if len(msg.split('/'))==2:
            t=setting(msg)
            u.append(t[0])
            b.append(t[1])
            print(u)
            print(b)            
            await message.channel.send('成功設定對話')            
    elif msg[0:7]==(bot_name+' del '):
        msg=msg[7:]
        b.pop(u.index(msg))
        u.remove(msg)
        await message.channel.send('成功刪除對話')
    elif msg[0:3]==(bot_name+' '):
        msg=msg[3:]
        if msg in u:            
            await message.channel.send(b[u.index(msg)])
        else:
            await message.channel.send('喵?')


client.run('ODUwMzI3OTQxOTU5NTE2MTYx.YLoHmw._mLpMoM5wOMAda6ScXOawpsfRr0')