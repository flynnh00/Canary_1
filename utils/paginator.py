#!/usr/bin/python3

import discord
from discord.ext import commands
import asyncio

import math

class Pages():
    def __init__(self, ctx, currentPage=1, msg=None, itemList=[], title='Paginator'):
        self.bot = ctx.bot
        self.guild = ctx.guild
        self.channel = ctx.channel
        self.user = ctx.author
        self.message = msg
        self.itemList = itemList
        self.title = title
        length = 0
        pageCounter = 0
        cache = 0
        self.pagesToSend = ['empty page']
        for i in range(len(self.itemList)):
            length += len(self.itemList[i])
            if length > 1994 or i == len(self.itemList)-1:
                self.pagesToSend.append('```' + '\n'.join(self.itemList[cache:i]).replace('```', '') + '```')
                cache = i
                length = len(self.itemList[i])
                pageCounter += 1
        self.lastPage = pageCounter
        self.actions = [('⏪', self.__firstPage),
                        ('◀', self.__prevPage),
                        ('▶', self.__nextPage),
                        ('⏩', self.__lastPage),
                        ('⏹', self.__halt),
                        ('🚮', self.__del)]
        self.currentPage = currentPage
        self.delete = False


    async def __showPage(self, page):
        self.currentPage = max(0, min(page, self.lastPage))
        if self.message:
            if self.currentPage == 0:
                try:
                    await self.message.delete()
                    self.message = None
                    return
                except:
                    pass
            else:
                await self.message.edit(content=self.pagesToSend[self.currentPage])
                return
        else:
            self.message = await self.channel.send(content=self.pagesToSend[self.currentPage], delete_after=300)
            for (emoji, _) in self.actions:
                await self.message.add_reaction(emoji)
            return


    async def __firstPage(self):
        await self.__showPage(1)


    async def __prevPage(self):
        await self.__showPage(max(1, self.currentPage - 1))


    async def __nextPage(self):
        await self.__showPage(min(self.lastPage, self.currentPage + 1))


    async def __lastPage(self):
        await self.__showPage(self.lastPage)


    async def __halt(self):
        await self.__showPage(0)


    async def __del(self):
        self.delete = True
        await self.__showPage(1)


    def __reactCheck(self, reaction, user):
        if user == self.bot.user:
            return False
        if reaction.message.id != self.message.id:
            return False
        for (emoji, action) in self.actions:
            if reaction.emoji == emoji:
                self.user = user
                self.__turnPage = action
                return True
        return False


    async def paginate(self):
        self.delete = False
        await self.__showPage(self.currentPage)
        while not self.delete and self.message:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=self.__reactCheck)
            except:
                try:
                    self.message.delete()
                except:
                    pass
                finally:
                    break
            await self.__turnPage()
            try:
                await self.message.remove_reaction(reaction, user)
            except:
                pass
