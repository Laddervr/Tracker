# Gorilla Tag Player Tracker with Discord Webhook

A BepInEx mod for **Gorilla Tag** that tracks player join/leave events and the room codes they enter, sending the information directly to a Discord webhook. The mod is always enabled and continuously monitors player activities during gameplay.

## Features

- Tracks when players join and leave the game.
- Logs the room (code) the player enters or exits.
- Automatically sends the information to a configured Discord webhook.
- The mod is always active and does not require manual enabling/disabling.

## Prerequisites

- **Gorilla Tag** installed on your system.
- **BepInEx** framework installed to manage mods.
- A **Discord webhook** URL to receive the logs.

## Installation

1. **Download and Install BepInEx**:
   - Download BepInEx from [here](https://github.com/BepInEx/BepInEx/releases).
   - Extract the files to your *Gorilla Tag* game folder.
   - Ensure that `BepInEx` is properly set up by running the game once, which will generate necessary folders like `BepInEx/plugins`.

2. **Download/Clone this repository**:
   - Download the latest release or clone this repository to your local system:
     ```bash
     git clone https://github.com/yourusername/gorillatag-player-tracker.git
     ```

3. **Place the DLL in BepInEx Plugins Folder**:
   - Once you compile the mod (or download the compiled `.dll` from releases), place the `PlayerTracker.dll` into the `BepInEx/plugins/` folder inside your *Gorilla Tag* directory.

4. **Configure Your Discord Webhook**:
   - Open the `PlayerTracker.cs` file in your favorite code editor.
   - Replace the line containing:
     ```csharp
     private const string WebhookUrl = "YOUR_DISCORD_WEBHOOK_URL";
     ```
     with your actual Discord webhook URL. You can create a new webhook in your Discord server settings.
   
5. **Run Gorilla Tag**:
   - Start *Gorilla Tag* as usual. The mod will track player join/leave events and room codes, and the information will be sent to your configured Discord channel.

## Usage

Once installed and running, the mod will automatically log:

- **Player joins**: Logs when a player joins the game and which room they join.
- **Player leaves**: Logs when a player leaves the game and which room they left.
- **Room changes**: Logs whenever a new room (code) is joined.

Example logs sent to your Discord:

```plaintext
Player Bob joined the game in room XYZ123 at 2024-09-17 15:30:00
Player Alice left the game from room ABC789 at 2024-09-17 15:45:00
Room code ABC789 was joined at 2024-09-17 15:20:00
