import asyncio
import time
from poke_env.player import Player
from poke_env import AccountConfiguration, ServerConfiguration
from start_bot_server import BotServer


num_battles = 5
max_concurrent_battles = 10

# --- Bot 1: The "Max Damage" Bot ---
# Looks at all available moves and picks the one with highest Base Power.
class MaxDamagePlayer(Player):
    def choose_move(self, battle):
        # 1. Pick the strongest move
        if battle.available_moves:
            # Sort moves by base power (highest first)
            best_move = max(battle.available_moves, key=lambda m: m.base_power)
            return self.create_order(best_move)
        
        # 2. Switch if cannot attack.
        return self.choose_random_move(battle)

# --- Bot 2: The "Random Move" Bot ---
# Simply picks a random move each turn.
class TypeRandoPlayer(Player):
    def choose_move(self, battle):
        return self.choose_random_move(battle)

# --- Main Execution ---
async def main():
    # Initialize Pokemon Showdown server
    server = BotServer()
    
    try:
        print("[Test] Setting up Pokemon Showdown server...")
        server.setup()
        print("[Test] Starting Pokemon Showdown server...")
        server.start()
        
        # Configuration for Localhost
        # Parameter 1: WebSocket URL, Parameter 2: HTTP action URL
        local_server = ServerConfiguration("ws://localhost:8000/showdown/websocket", "http://localhost:8000/action.php?")
        
        # Give the server time to be ready to connect
        await asyncio.sleep(3)
        
        # save_replays=True will save HTML replay files you can open in a browser to view battles
        # Use timestamp for unique usernames
        unique_id = str(int(time.time()))[-6:] 
        
        bot_dumb = MaxDamagePlayer(
            account_configuration=AccountConfiguration(f"DumbBot{unique_id}", ""),
            server_configuration=local_server,
            max_concurrent_battles=max_concurrent_battles,
            save_replays=True  
        )
        
        bot_smart = TypeRandoPlayer(
            account_configuration=AccountConfiguration(f"RandoBot{unique_id}", ""),
            server_configuration=local_server,
            max_concurrent_battles=max_concurrent_battles,
            save_replays=True  
        )

        print(f"Starting battle: {bot_dumb.username} vs {bot_smart.username}")
        print("\nTo view battles:")
        print("  1. Open http://localhost:8000 in your browser (while server is running)")
        print("  2. Replay HTML files will be saved in the current directory after battles complete")
        print()
        
        await bot_smart.battle_against(bot_dumb, n_battles=num_battles)

        print(f"\nFinal Score ({bot_smart.n_finished_battles} games):")
        print(f"Smart Bot Won: {bot_smart.n_won_battles}")
        print(f"Dumb Bot Won:  {bot_dumb.n_won_battles}")
    
    finally:
        # Delay to view the battles
        time.sleep(1000)

        # Ensure server is stopped when done
        print("[Test] Stopping Pokemon Showdown server...")
        server.stop()

if __name__ == "__main__":
    asyncio.run(main())