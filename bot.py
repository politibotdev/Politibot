import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import requests
import json

load_dotenv()

print("Lancement de Politibot...")
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Politibot est en ligne ! Connecté en tant que {bot.user}')
    print('---')
    try:
        synced = await bot.tree.sync()
        print(f"Commandes Synchronisées: {len(synced)}")
    except Exception as e:
        print(e)

@bot.tree.command(name="cgu", description="afficher les CGU")
async def cgu(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Voici les CGU: https://docs.google.com/document/d/1C9z97KnXOKczYeQu6pQnIWLGUS1o-9BUorh5vUiGUjU/edit?usp=sharing"
    )

@bot.tree.command(name="pdc", description="afficher la politique de confidentialité")
async def pdc(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Voici la politique de confidentialité: https://docs.google.com/document/d/1JAO541YtrDSuQAWueNtiq6I9ohfpHj0GLrEIG3Xs9UM/edit?usp=sharing"
    )

@bot.tree.command(name="apropos", description="afficher l'a propos")
async def apropos(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Voici l'a propos du bot: https://docs.google.com/document/d/1C9z97KnXOKczYeQu6pQnIWLGUS1o-9BUorh5vUiGUjU/edit?usp=sharing"
    )

bot.run(os.getenv('DISCORD_TOKEN'))