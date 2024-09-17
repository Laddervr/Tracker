import requests
import time
from datetime import datetime

# Your Discord Webhook URL
WEBHOOK_URL = 'YOUR_DISCORD_WEBHOOK_URL'

# Simulated player and room tracking
players_in_game = {}  # Dictionary to track players in the game and their room codes


def send_to_discord(message):
    """Send a log message to a Discord webhook."""
    data = {"content": message}
    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print("Message sent to Discord.")
    else:
        print(f"Failed to send message to Discord: {response.status_code} {response.text}")


def player_join(player_name, room_code):
    """Log when a player joins a room."""
    global players_in_game

    if player_name not in players_in_game:
        players_in_game[player_name] = room_code
        message = f"Player {player_name} joined the game in room {room_code} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        send_to_discord(message)
    else:
        print(f"Player {player_name} is already in the game.")


def player_leave(player_name):
    """Log when a player leaves the game."""
    global players_in_game

    if player_name in players_in_game:
        room_code = players_in_game[player_name]
        message = f"Player {player_name} left the game from room {room_code} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        send_to_discord(message)
        del players_in_game[player_name]
    else:
        print(f"Player {player_name} is not currently in the game.")


def room_change(player_name, new_room_code):
    """Log when a player changes rooms."""
    global players_in_game

    if player_name in players_in_game:
        old_room_code = players_in_game[player_name]
        if old_room_code != new_room_code:
            players_in_game[player_name] = new_room_code
            message = f"Player {player_name} moved from room {old_room_code} to {new_room_code} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            send_to_discord(message)
        else:
            print(f"Player {player_name} is already in room {new_room_code}.")
    else:
        print(f"Player {player_name} is not currently in the game.")


# Simulate player actions (you would replace this part with actual data from a game or server)
def simulate_game():
    """Simulate player actions to test the script."""
    time.sleep(2)
    player_join("Player1", "RoomA")
    time.sleep(2)
    player_join("Player2", "RoomB")
    time.sleep(3)
    room_change("Player1", "RoomC")
    time.sleep(2)
    player_leave("Player2")
    time.sleep(3)
    player_leave("Player1")


if __name__ == "__main__":
    simulate_game()
