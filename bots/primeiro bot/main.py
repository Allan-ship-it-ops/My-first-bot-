import discord
from discord.ext import commands, tasks
import random
import asyncio


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

@tasks.loop(minutes=30)
async def x9_aleatorio():
    await bot.wait_until_ready()
    canal = bot.get_channel(1495965550617296916)
    if not canal:
        return


    membros = [m for m in canal.guild.members if not m.bot]
    if not membros:
        return
        
    alvo = random.choice(membros)
    
    fofocas = [
        f"🕵️‍♂️ Análise de campo: {alvo.mention} parece estar tramando algo nas calls de madrugada...",
        f"📸 O espião avistou {alvo.mention} editando mensagens suspeitas hoje. O que você está escondendo?",
        f"🚩 ALERTA: {alvo.mention} é o membro com maior probabilidade de ser um agente infiltrado.",
        f"⚖️ O Tribunal de Guerra está de olho em você, {alvo.mention}. Comporte-se.",
        f"👀 Alguém avise o {alvo.mention} que apagar mensagem não apaga o meu registro no auditoria!"
    ]
    
    await canal.send(random.choice(fofocas))


@x9_aleatorio.before_loop
async def before_x9():
    await bot.wait_until_ready()

@bot.event
async def on_ready():
    print(f" FINALMENTE! O bot {bot.user} ligou!")


    await bot.change_presence(activity=discord.Game(name="Vigiando o tribunal de guerra ⚖️"))

    if not x9_aleatorio.is_running():
        x9_aleatorio.start()

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

    @bot.command()
    async def zoar(ctx):
        await ctx.send("Allan e muito ruim!")

import asyncio

@bot.command()
async def vrau(ctx, usuario: discord.Member):
    msg = await ctx.send(f"{usuario.mention} voce e um feio e ninguem te avisou!")
    await asyncio.sleep(2)
    await ctx.message.delete()
    await msg.delete()

    import random

    @bot.command()
    async def opa(ctx, usuario: discord.Member):
        frases = [
            f"Ih {usuario.mention}, sua mae sabe que voce ta na internet?",
            f"O {usuario.mention} joga pior que bot de tutorial.",
            f"Alguem muta o {usuario.mention}, por favor?",
            f"O {usuario.mention} e o tipo de cara que usa mouse pra clicar nas habilidades."
        ]
        
@bot.event
async def on_message(message):

    await bot.process_commands(message)

    if message.author == bot.user:
        return
    
    if "Allan" in message.author.name:
        await message.add_reaction("😍")

    if random.random() < 0.2:
        reacoes = ["🤡", "🤣", "🤨", "🔥", "👀", "👻", "⚡"]
        await message.add_reaction(random.choice(reacoes))


@bot.command()
async def regras(ctx):
    embed = discord.Embed(
        title="⚠️ DIRETRIZES DA COMUNIDADE - CORAÇÃO DE FERRO",
        description="Para manter a convivência em harmonia, todos os membros devem seguir as normas abaixo.",
        color=0x2f3136
    )

    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)

    
    embed.add_field(
        name="⚖️ 1. CONDUTA E RESPEITO", 
        value="> Seja cordial. Ataques pessoais, preconceito, discurso de ódio ou assédio resultarão em banimento imediato.", 
        inline=False
    )
    
    embed.add_field(
        name="🚫 2. DIVULGAÇÃO E SPAM", 
        value="> Proibido o envio de links externos, convites de outros servidores ou flood sem autorização prévia.", 
        inline=False
    )

    embed.add_field(
        name="🔞 3. CONTEÚDO IMPRÓPRIO", 
        value="> Mantenha o chat limpo. Conteúdos sexualmente explícitos ou gore são estritamente proibidos.", 
        inline=False
    )

    embed.add_field(
        name="🔊 4. CANAIS DE VOZ", 
        value="> Não utilize soundboards irritantes ou grite nos canais de voz. Respeite o espaço de conversa alheio.", 
        inline=False
    )

    embed.add_field(
        name="📢 5. CANAIS ESPECÍFICOS", 
        value="> Use cada canal para sua devida função. Evite poluir canais de arte com memes, por exemplo.", 
        inline=False
    )

    embed.set_footer(text="A administração se reserva o direito de punir qualquer conduta tóxica.")
    
    
    embed.set_image(url="https://cdn.discordapp.com/attachments/1496333308316094636/1496599602697212036/a561542be31e597e90d3fac62b8fa1d1.jpg?ex=69ea787e&is=69e926fe&hm=da63afb123e90753a5a6a12c4c4325ccbfe6301127a246838231269466313f63")

    await ctx.message.delete()
    
    
    await ctx.send(content="||@everyone|| ||@here||", embed=embed)


@bot.event
async def on_message_delete(message):
    if message.author == bot.user:
        return

    
    canal_logs = bot.get_channel(1496618417162289194) 
    
    embed = discord.Embed(
        title="🗑️ MENSAGEM APAGADA",
        color=0xFF0000,
        timestamp=message.created_at
    )
    embed.add_field(name="Autor:", value=message.author.mention, inline=True)
    embed.add_field(name="Canal:", value=message.channel.mention, inline=True)
    embed.add_field(name="Conteúdo:", value=message.content or "*(Mensagem vazia ou imagem)*", inline=False)
    
    if canal_logs:
        await canal_logs.send(embed=embed)


@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user or before.content == after.content:
        return

    canal_logs = bot.get_channel(1496618417162289194) 
    
    embed = discord.Embed(
        title="✏️ MENSAGEM EDITADA",
        color=0xFFFF00,
        timestamp=after.edited_at or discord.utils.utcnow()
    )
    embed.add_field(name="Autor:", value=before.author.mention, inline=True)
    embed.add_field(name="Canal:", value=before.channel.mention, inline=True)
    embed.add_field(name="Antes:", value=before.content, inline=False)
    embed.add_field(name="Depois:", value=after.content, inline=False)

    if canal_logs:
        await canal_logs.send(embed=embed)

@bot.event
async def on_voice_state_update(member, before, after):
    
    canal_logs = bot.get_channel(1496618417162289194) 
    if not canal_logs:
        return

    
    if before.channel is None and after.channel is not None:
        embed = discord.Embed(
            title="🎤 ENTROU NA CALL",
            description=f"{member.mention} entrou no canal **{after.channel.name}**",
            color=0x00FF00 
        )
        await canal_logs.send(embed=embed)

    
    elif before.channel is not None and after.channel is None:
        embed = discord.Embed(
            title="🔇 SAIU DA CALL",
            description=f"{member.mention} saiu do canal **{before.channel.name}**",
            color=0xFF0000 
        )
        await canal_logs.send(embed=embed)

    
    elif before.channel is not None and after.channel is not None and before.channel != after.channel:
        embed = discord.Embed(
            title="🔄 MUDOU DE CALL",
            description=f"{member.mention} saiu de **{before.channel.name}** e foi para **{after.channel.name}**",
            color=0x808080 
        )
        await canal_logs.send(embed=embed)

import asyncio
from datetime import timedelta

@bot.command()
@commands.has_permissions(moderate_members=True) 
async def julgar(ctx, membro: discord.Member):
    embed = discord.Embed(
        title="⚖️ TRIBUNAL DE GUERRA",
        description=f"O réu {membro.mention} está sendo julgado pela comunidade!\n\n**Vote abaixo:**\n✅ - Inocente\n❌ - Culpado (5 min de silêncio)",
        color=0x808080 
    )
    embed.set_thumbnail(url=membro.display_avatar.url)
    embed.set_footer(text="O julgamento dura 30 segundos.")

    mensagem = await ctx.send(embed=embed)
    await mensagem.add_reaction("✅")
    await mensagem.add_reaction("❌")

    await asyncio.sleep(30) 

    
    mensagem = await ctx.channel.fetch_message(mensagem.id)
    
    votos_inocente = 0
    votos_culpado = 0

    for reaction in mensagem.reactions:
        if str(reaction.emoji) == "✅":
            votos_inocente = reaction.count -
        if str(reaction.emoji) == "❌":
            votos_culpado = reaction.count - 1

    if votos_culpado > votos_inocente:
        try:
            await membro.timeout(timedelta(minutes=5), reason="Condenado no Tribunal de Guerra")
            await ctx.send(f"🚨 **SENTENÇA:** Com {votos_culpado} votos contra, {membro.mention} foi enviado para a solitária por 5 minutos!")
        except:
            await ctx.send("❌ O réu é muito forte (tem cargo alto) e não pude silenciá-lo!")
    else:
        await ctx.send(f"🕊️ **ABSOLVIDO:** O tribunal decidiu que {membro.mention} é inocente... por enquanto.")



bot.run("")