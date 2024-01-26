import discord
import random
import time
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def yas(ctx):
    await ctx.send("Merhaba,Kaç yaşındasın?")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    try:
        message = await bot.wait_for("message",check=check)    
        yas = int(message.content)

        if yas<18:
            await ctx.send("bilgi almak için cevrekucuk yazınız")
        else:
            await ctx.send("bilgi almak için cevrebuyuk yazınız")
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben çevre dostu bir botum!')
    time.sleep(1)
    await ctx.send(f'Haydi biraz konuşalım!')
@bot.command()
async def sohbet(ctx):
    await ctx.send(f'Merhaba! Ne hakkında konuşalım?')

#KUCUKLER İÇİn

@bot.command()
async def cevrekucuk(ctx):
     await ctx.send(f'Çevre ve kirlilik hakkında bir şey yapmak istiyorsanız oneriev1 / oneridısarı1 komutunu kullanın!')
@bot.command()
async def oneriev1(ctx):
    await ctx.send(f'Geri dönüşüm ve hangi malzemelerin geri dönüştürülebileceği hakkında bilgi edinin ve günlük yaşamınızda geri dönüştürülebilir malzemeleri kullanın')
    time.sleep(1)
    await ctx.send(f"gereksiz ısıkları acık bırakmayın")
    time.sleep(1)
    await ctx.send(f"evinizde ısı yalıtımına sahip olun ")

@bot.command()
async def oneridısarı1(ctx):
    await ctx.send(f"toplu tasıma kullanalım")
    time.sleep(1)
    await ctx.send(f"yerlere çöp atmayalım")
    time.sleep(1)
    await ctx.send(f"atık pilleri çöpe değil atık pil kutusuna atalım")
    time.sleep(1)
    await ctx.send(f"tek kullanımlık tabak bardak çatal yerine seramik veya metal olarak kullanalım")
    time.sleep(1)
    await ctx.send(f"naylon poşet kullanımını azaltın")


#BUYUKLER ICIN


@bot.command()
async def cevrebuyuk(ctx):
    await ctx.send(f'Çevre ve kirlilik hakkında bir şey yapmak istiyorsanız oneriev / oneridısarı / oneritoplum  komutunu kullanın!')
@bot.command()
async def oneriev(ctx):
    await ctx.send(f'Geri dönüşüm ve hangi malzemelerin geri dönüştürülebileceği hakkında bilgi edinin ve günlük yaşamınızda geri dönüştürülebilir malzemeleri kullanın')
    time.sleep(1)
    await ctx.send(f"kullanılmış yağları lavaboya dökmeyin")
    time.sleep(1)
    await ctx.send(f"gereksiz ısıkları acık bırakmayın")
    time.sleep(1)
    await ctx.send(f"evinizde ısı yalıtımına sahip olun ")

@bot.command()
async def oneridısarı(ctx):
    await ctx.send(f"toplu tasıma kullanalım")
    time.sleep(1)
    await ctx.send(f"yerlere çöp atmayalım")
    time.sleep(1)
    await ctx.send(f"atık pilleri çöpe değil atık pil kutusuna atalım")
    time.sleep(1)
    await ctx.send(f"tek kullanımlık tabak bardak çatal yerine seramik veya metal olarak kullanalım")
    time.sleep(1)
    await ctx.send(f"naylon poşet kullanımını azaltın")
    
@bot.command()
async def resim(ctx):
    with open(r'C:\Users\Lenovo\OneDrive\Masaüstü\Yeni klasör (2)\bot\resim\aad.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    time.sleep(1)
    await ctx.send(f'Hep birlikte tercih ve alışkanlıklarımızı değiştirerek çevre kirliliği sorununu çözmeye çalışalım ve dünyamızı temiz tutalım.')
bot.run("TOKEN")
