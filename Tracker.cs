using UnityEngine;
using BepInEx;
using UnityEngine.Networking;
using System.Text;
using System.Collections;

[BepInPlugin("com.yourname.gorillatag.playertracker", "Always Enabled Player Tracker with Webhook", "1.0.0")]
public class PlayerTracker : BaseUnityPlugin
{
    private const string WebhookUrl = "YOUR_DISCORD_WEBHOOK_URL";  // <-- Replace with your Discord webhook URL

    // This method runs when the mod is loaded and keeps the hooks always active
    void Start()
    {
        // Always keep hooks enabled for player join, leave, and room join events
        PlayerManager.OnPlayerJoin += LogPlayerJoin;
        PlayerManager.OnPlayerLeave += LogPlayerLeave;
        RoomManager.OnRoomJoin += LogRoomJoin;
    }

    // Log when a player joins the game
    void LogPlayerJoin(Player player)
    {
        string currentRoom = RoomManager.GetCurrentRoom(); // Assuming RoomManager has this method
        string logMessage = $"Player {player.Name} joined the game in room {currentRoom} at {System.DateTime.Now}\n";
        StartCoroutine(SendToDiscord(logMessage));
    }

    // Log when a player leaves the game
    void LogPlayerLeave(Player player)
    {
        string currentRoom = RoomManager.GetCurrentRoom(); // Assuming RoomManager has this method
        string logMessage = $"Player {player.Name} left the game from room {currentRoom} at {System.DateTime.Now}\n";
        StartCoroutine(SendToDiscord(logMessage));
    }

    // Log when the player changes rooms or enters a new room
    void LogRoomJoin(string roomCode)
    {
        string logMessage = $"Room code {roomCode} was joined at {System.DateTime.Now}\n";
        StartCoroutine(SendToDiscord(logMessage));
    }

    // Send log message to Discord via Webhook
    IEnumerator SendToDiscord(string message)
    {
        // Format the message as JSON payload
        string jsonPayload = "{\"content\": \"" + message.Replace("\"", "\\\"") + "\"}";

        using (UnityWebRequest request = new UnityWebRequest(WebhookUrl, "POST"))
        {
            byte[] bodyRaw = Encoding.UTF8.GetBytes(jsonPayload);
            request.uploadHandler = new UploadHandlerRaw(bodyRaw);
            request.downloadHandler = new DownloadHandlerBuffer();
            request.SetRequestHeader("Content-Type", "application/json");

            // Send the request and wait for a response
            yield return request.SendWebRequest();

            if (request.result != UnityWebRequest.Result.Success)
            {
                Debug.LogError($"Error sending to Discord: {request.error}");
            }
            else
            {
                Debug.Log("Successfully sent log to Discord.");
            }
        }
    }
}
