from os import environ as env, listdir
from resources.constants import SERVER_HOST, SERVER_PORT, MODULES
from resources.secrets import DISCORD_PUBLIC_KEY, DISCORD_APPLICATION_ID, DISCORD_TOKEN
from resources.bloxlink import Bloxlink
import asyncio

loop = asyncio.get_event_loop()

if __name__ == "__main__":
    bot = Bloxlink(
        env.get("DISCORD_PUBLIC_KEY", DISCORD_PUBLIC_KEY),
        env.get("DISCORD_APPLICATION_ID", DISCORD_APPLICATION_ID),
        token=env.get("DISCORD_TOKEN", DISCORD_TOKEN),
        sync_commands=True,
        auto_defer=True
    )

    for directory in MODULES:
        files = [name for name in listdir('src/'+directory.replace('.', '/')) if name[:1] != "." and name[:2] != "__" and name != "_DS_Store"]

        for filename in [f.replace(".py", "") for f in files]:
            if filename in ('bot', '__init__'):
                continue
            bot.load_module(f"{directory.replace('/','.')}.{filename}")

    bot.run(env.get("HOST", SERVER_HOST), env.get("PORT", SERVER_PORT), debug=True)
