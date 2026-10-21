# RateWillBot

A small Discord bot that rates my friend Will's memes. When Will posts an image in the server, the bot replies with a score from 1 to 9 and a comment to match.

I built it in 2020 to learn the basics of [discord.py](https://discordpy.readthedocs.io/).

## How it works

All of it is in `main.py`:

- **`on_message`** runs for every message. If it's from Will and has an attachment, the bot rates it.
- **The rating** is `random.randrange(1, 10)`, a number from 1 to 9. (Don't tell Will.)
- **The reply** depends on the score: 1–3, 4–6, or 7–9 each get their own comment.
- **`on_ready`** prints "I'm in" once the bot connects, so you know it's running.

## What I learned

- Reading the discord.py docs and finding what I needed in them
- Events: running code when something happens
- Conditionals and random numbers in Python

## Run it

1. Create a bot in the [Discord Developer Portal](https://discord.com/developers/applications) and copy its token.
2. Make a `.env` file next to `main.py` with your token. Never commit this file:
   ```
   DISCORD_TOKEN=your-token
   ```
3. Install the libraries and start the bot:
   ```
   pip install discord.py python-dotenv
   python main.py
   ```
4. To rate someone else, change the name in `main.py` (`message.author.name == 'Brother Man Will'`).

**Note:** this was written in 2020 for discord.py 1.x. discord.py 2.0 and later require "intents": create the client with `discord.Client(intents=intents)`, where `intents = discord.Intents.default()` and `intents.message_content = True`. Also turn on **Message Content Intent** for your bot in the Developer Portal.
