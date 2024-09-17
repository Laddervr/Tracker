import requests
import random

# List of possible codes
codes = [
    "JMAN", "ZERDY", "DAPPER", "SNAIL", "ELLIOT", "K9", "TURBO", "VMT", "MOSA", "RAKZZ",
    "MAXO", "AUSSIE", "DAPPERSLUG", "TYLERVR", "STYLEDSNAIL", "CODY", "QUINN", "LEOVR", "LEO", 
    "PARTYMONKEY", "BOETHIA", "CHIVI", "HEADCHEF", "HEADCHEFVR", "KNINLY", "JAWCLAMPS", "MAJORA", 
    "KISHARK", "WIDDOM", "TIKTOK", "TTT", "DAISY", "J3VU", "RUN", "SREN17", "YOUTUBER", "GTC", 
    "MODS", "GTC1", "GTC2", "GTC3", "GTC4", "GTC5", "GTC6", "GTC7", "GTC8", "GTC9", "GTC10", "O", 
    "PIG", "TTTPIG", "LEMMING", "AA", "JUAN", "THUMBZ", "VMT", "TYLERVR", "A", "JMAN1", "ELLIOT", 
    "K8", "TIMMY", "JMAN2", "JMAN3", "GT", "CGT", "GTC", "GHOST", "DAISY09", "RUN", "RUN1", "666", 
    "DAISY099", "ENDISHERE", "ECHO", "CHIPPD", "BANJO", "CHIPPDBANJO", "GH0ST", "END", "DEATH", 
    "FNAF", "GTAG", "ECH0", "BANANA", "SMILER", "UNKNOWN", "BOTS", "DEAD", "HUNT", "J3VU", "MORSE", 
    "PBBV", "SPIDER", "SREN17", "SREN18", "MONK", "STATUE", "GORILLA", "LEMMING", "STICK", "MODDER", 
    "MODDERS", "MODERATOR", "TTTPIG", "ANTOCA", "BODA", "JOLYENE", "ELECTRONIC", "OWNER", "DEV", 
    "CREATOR", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "CREEP", "CREEPY", "SCARY", 
    "SPOOKY", "SPOOK", "MINIGAMES", "GAMES", "PLAY", "FINGERPAINTER", "CONTENTCREATOR", "CONTENT", 
    "MIRRORMAN", "HELPME", "BEES", "NAMO", "WARNING", "BANSHEE", "JUAN", "THUMBZ", "VMT", "TYLERVR", 
    "PARTYMONKEY", "HIDE", "MONKEY", "WOW", "THUMBZ", "MITTENS", "RAY2", "RAY1", "GRAPES", "MICROPHONE", 
    "BARK", "DURF", "JULIAN", "HAVEN", "PIG", "TTTPIG", "VR", "WEAREVR", "GTAG", "GORILLA", "GT", 
    "MOD", "MODS", "FINGER", "PAINTER", "STICK", "ADMIN", "STAFF", "STYLED", "SNAIL", "JUAN", "CRASH", 
    "AUSSIE", "YOUTUBE", "TIKTOK", "MODDER", "MODDING", "GTC", "K9", "JMAN", "3", "4", "5", "6", "7", 
    "8", "9", "10", "O", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "ALEC", "ALECVR"
]

# Function to send the message to Discord Webhook
def send_to_discord(message, webhook_url):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

# Choose a random code
random_code = random.choice(codes)

# Discord webhook URL
webhook_url = "YOUR_DISCORD_WEBHOOK_URL"  # Replace with your actual Discord Webhook URL

# Send the random code to Discord
send_to_discord(f"Player joined random room code: {random_code}", webhook_url)
