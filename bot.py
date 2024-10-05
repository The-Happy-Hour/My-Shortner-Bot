import re
import aiohttp

from os import environ
from pyrogram import Client, filters
from pyrogram.types import *

API_ID = environ.get('API_ID', "1802906") #BSDK 5 Shortner Kam Nai Hota 📌 Agar 6th Shortner Add Karne Ka Try Bhi Kiya To Pel Duga...🤬
API_HASH = environ.get('API_HASH', "c7e95244251e33bb5cce566b29f7254")
BOT_TOKEN = environ.get('BOT_TOKEN', "758136993:AAHwuzKS6K5Px_szrGSbebvp31NtLujdCkA")

thehappyhour = Client('link shortener bot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=100)

print("Bot Is Started ✅")

@thehappyhour.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply("**Send me link and get short link.\n\nshortner 1 - tryshort.in\nshortner 2 - earnfly.net\nshortner 3 - sharedisklinks.com\nshortner 4 - thh.aslink.in\nshortner 5 - adrinolinks.in\n\nAdd Unlimited Shortner By Using Add Command.**")
        # f"**I'm Link Shortener bot. Just send me link and get short link, You can also send multiple links seperated by a space or enter.**")


@thehappyhour.on_message(filters.command('short1') & filters.private & filters.text & filters.incoming)
async def link_handler(bot, message):
    link_pattern = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', re.DOTALL)
    links = re.findall(link_pattern, message.text)
    if len(links) <1:
        await message.reply("No links Found in this text",quote=True)
        return
    for link in links:
        try:
            short_link = await get_shortlink_1(link)
            await message.reply(f"**Here is Your Shortened Link\n\nOriginal Link - {link}\n\nShorted Link - {short_link}\n\nTap 2 Copy - `{short_link}`**",quote=True,disable_web_page_preview=True)
        except Exception as e:
            await message.reply(f'Error: `{e}`', quote=True)

@thehappyhour.on_message(filters.command('short2') & filters.private & filters.text & filters.incoming)
async def link_handler(bot, message):
    link_pattern = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', re.DOTALL)
    links = re.findall(link_pattern, message.text)
    if len(links) <1:
        await message.reply("No links Found in this text",quote=True)
        return
    for link in links:
        try:
            short_link = await get_shortlink_2(link)
            await message.reply(f"**Here is Your Shortened Link\n\nOriginal Link - {link}\n\nShorted Link - {short_link}\n\nTap 2 Copy - `{short_link}`**",quote=True,disable_web_page_preview=True)
        except Exception as e:
            await message.reply(f'Error: `{e}`', quote=True)

@thehappyhour.on_message(filters.command('short3') & filters.private & filters.text & filters.incoming)
async def link_handler(bot, message):
    link_pattern = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', re.DOTALL)
    links = re.findall(link_pattern, message.text)
    if len(links) <1:
        await message.reply("No links Found in this text",quote=True)
        return
    for link in links:
        try:
            short_link = await get_shortlink_3(link)
            await message.reply(f"**Here is Your Shortened Link\n\nOriginal Link - {link}\n\nShorted Link - {short_link}\n\nTap 2 Copy - `{short_link}`**",quote=True,disable_web_page_preview=True)
        except Exception as e:
            await message.reply(f'Error: `{e}`', quote=True)

@thehappyhour.on_message(filters.command('short4') & filters.private & filters.text & filters.incoming)
async def link_handler(bot, message):
    link_pattern = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', re.DOTALL)
    links = re.findall(link_pattern, message.text)
    if len(links) <1:
        await message.reply("No links Found in this text",quote=True)
        return
    for link in links:
        try:
            short_link = await get_shortlink_4(link)
            await message.reply(f"**Here is Your Shortened Link\n\nOriginal Link - {link}\n\nShorted Link - {short_link}\n\nTap 2 Copy - `{short_link}`**",quote=True,disable_web_page_preview=True)
        except Exception as e:
            await message.reply(f'Error: `{e}`', quote=True)

@thehappyhour.on_message(filters.command('short5') & filters.private & filters.text & filters.incoming)
async def link_handler(bot, message):
    link_pattern = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', re.DOTALL)
    links = re.findall(link_pattern, message.text)
    if len(links) <1:
        await message.reply("No links Found in this text",quote=True)
        return
    for link in links:
        try:
            short_link = await get_shortlink_5(link)
            await message.reply(f"**Here is Your Shortened Link\n\nOriginal Link - {link}\n\nShorted Link - {short_link}\n\nTap 2 Copy - `{short_link}`**",quote=True,disable_web_page_preview=True)
        except Exception as e:
            await message.reply(f'Error: `{e}`', quote=True)

#Function
async def get_shortlink_1(link):
    url = "https://tryshort.in/api"
    key = "41d5dfab6c64a21e0e3e81b6eb3c947f28c7105c" 
    params = {'api': key, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]
        
async def get_shortlink_2(link):
    url = "https://earnfly.net/api"
    key = "daae6d5c8beace88e448b1059af2946df208b423" 
    params = {'api': key, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]

async def get_shortlink_3(link):
    url = "https://sharedisklinks.com/api"
    key = "fcd5336319ff60a848b4df69fd24664070d1691e" 
    params = {'api': key, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]
        
async def get_shortlink_4(link):
    url = "https://thh.aslink.in/api"
    key = "bd6f5d021a1c524512ebb40072962203a3abb7de" 
    params = {'api': key, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]
        
async def get_shortlink_5(link):
    url = "https://adrinolinks.in/api"
    key = "d255da53d874f9528bc98afd0fb13e9340fe0243" 
    params = {'api': key, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]
        
thehappyhour.run()
