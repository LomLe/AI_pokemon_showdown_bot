import asyncio
import time
import random
import os
from dotenv import load_dotenv
from poke_env.player import SimpleHeuristicsPlayer
from poke_env import AccountConfiguration, ShowdownServerConfiguration

# Load .env file
load_dotenv()

class HumanLikeBot(SimpleHeuristicsPlayer):
    def choose_move(self, battle):
        delay = random.uniform(1, 3)
        time.sleep(delay)
        print(f"[Bot] Thinking for {delay:.2f} seconds before moving...")
        print(f"[Bot] Move: {super().choose_move(battle)}")
        return super().choose_move(battle)

# --- Configuration ---
bot_username = os.getenv("BOT_USERNAME")
bot_password = os.getenv("BOT_PASSWORD")

if not bot_username or not bot_password:
    raise ValueError(
        "BOT_USERNAME and BOT_PASSWORD environment variables must be set. "
        "Create a .env file or export them before running."
    )

async def main():
    my_account_config = AccountConfiguration(bot_username, bot_password)

    # 2. Use our new 'HumanLikeBot' instead of 'RandomPlayer'
    player = HumanLikeBot(
        account_configuration=my_account_config,
        server_configuration=ShowdownServerConfiguration,
        battle_format="gen9randombattle",
        max_concurrent_battles=1,
        save_replays=False
    )

    print(f"Logged in as {bot_username}. Searching for a game...")

    await player.ladder(n_games=1)

    print("Battle finished. Script ending.")

if __name__ == "__main__":
    asyncio.run(main())