import os
import random
from pyswip import Prolog
import sys
import asyncio
import telepot
from telepot.aio.loop import MessageLoop
from telepot.aio.delegate import pave_event_space, per_chat_id, create_open
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


class PrologReplier(telepot.aio.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(PrologReplier, self).__init__(*args, **kwargs)
        self.prolog = Prolog()
        self.prolog.consult('Askid.pl')
        self.activities = {'eat': 'Did you eat anything at school today?',
                           'play': 'Did you play anything at school today?',
                           'learn': 'Did you learn anything at school today?',
                           'rest': 'Did you have a good rest at school today?',
                           'sports': 'Did you do any sports at your school today?'}
        self.unused_activities = list(self.activities.keys())
        self.activity = ''
        self.question = ''

    async def on_chat_message(self, msg):
        _, _, id = telepot.glance(msg)
        if (msg['text'] == '/start'):
            self.prolog = Prolog()
            self.prolog.consult('Askid.pl')
            self.question = random.choice(list(self.activities.keys()))
            self.activity = self.question
            self.prolog.assertz('curr({})'.format(self.question))
            self.prolog.query("assert(asked('{}'))".format(
                self.activities[self.question]))
            # await self.sender.sendMessage(self.activities[self.question])
            kb = ReplyKeyboardMarkup(keyboard=[['YES', 'NO']])
            await bot.sendMessage(id, self.activities[self.question], reply_markup=kb)
        elif (msg['text'] == 'YES'):
            if self.question in self.activities:
                self.question = list(self.prolog.query(
                    'random_question(X)'))[0]['X']
                kb = ReplyKeyboardMarkup(keyboard=[['YES', 'NO']])

                # await self.sender.sendMessage(self.question, reply_markup = kb)
                await bot.sendMessage(id, self.question, reply_markup=kb)
            else:
                # For some strange bugs, multiple print() functions must be inserted for the query to run successfully.
                print(list(self.prolog.query("play(X)")))
                self.prolog.query("assert(yes('{}'))".format(self.question))
                print(list(self.prolog.query(
                    "assert(yes('{}'))".format(self.question))))
                questions = list(self.prolog.query(
                    "ask('{}', X)".format(self.question)))
                print(questions)
                self.question = random.choice(questions)['X']
                self.prolog.query("assert(asked('{}'))".format(self.question))
                kb = ReplyKeyboardMarkup(keyboard=[['YES', 'NO']])
                # await self.sender.sendMessage(self.question, reply_markup = kb)
                await bot.sendMessage(id, self.question, reply_markup=kb)
        elif (msg['text'] == 'NO'):
            self.unused_activities.remove(self.activity)
            self.prolog.retract("curr({})".format(self.activity))
            if (len(self.unused_activities) == 0):
                self.prolog = Prolog()
                self.prolog.consult('Askid.pl')
                self.unused_activities = list(self.activities.keys())
                self.question = random.choice(list(self.activities.keys()))
                self.activity = self.question
                self.prolog.assertz('curr({})'.format(self.question))
            else:
                self.question = random.choice(self.unused_activities)
                self.activity = self.question
                self.prolog.assertz('curr({})'.format(self.question))
            self.prolog.query("assert(asked('{}'))".format(
                self.activities[self.question]))
            kb = ReplyKeyboardMarkup(keyboard=[['YES', 'NO']])
            # await self.sender.sendMessage(self.activities[self.question], reply_markup = kb)
            await bot.sendMessage(id, self.activities[self.question], reply_markup=kb)


# get token from command-line
TOKEN = <YOUR TOKEN>

bot = telepot.aio.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, PrologReplier, timeout=500),
])

loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot).run_forever())
print('Listening ...')

loop.run_forever()
