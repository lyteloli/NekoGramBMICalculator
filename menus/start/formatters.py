from NekoGram import NekoRouter, Neko, Menu
from aiogram import types
from html import escape

ROUTER = NekoRouter()


@ROUTER.formatter()
async def start(data: Menu, user: types.User, _: Neko):
    await data.build(text_format={'name': escape(user.full_name)})
