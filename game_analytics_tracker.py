
import random
import json
import matplotlib.pyplot as plt
import time

# Written by Idlan bin Hafiz

# Simulated player data (mock for now)
player_data = {
    "time_played": [],  # Minutes played each session
    "win_loss_ratio": []  # Win/Loss ratio for each session
}

# Generate random player data for 10 sessions
for session in range(10):
    time_played = random.randint(30, 120)  # Random time played between 30 and 120 minutes
    wins = random.randint(0, 10)
    losses = random.randint(0, 10)
    win_loss_ratio = wins / (losses + 1)  # Avoid division by zero

    player_data["time_played"].append(time_played)
    player_data["win_loss_ratio"].append(win_loss_ratio)

# Save the generated data to a JSON file
with open("player_data.json", "w") as f:
    json.dump(player_data, f)

# Plot the player data using Matplotlib
def visualize_player_data(player_data):
    sessions = list(range(1, len(player_data["time_played"]) + 1))
    
    # Plot time played per session
    plt.figure(figsize=(10, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(sessions, player_data["time_played"], marker='o', color='b', label='Time Played (minutes)')
    plt.title('Player Statistics')
    plt.xlabel('Session')
    plt.ylabel('Time Played (minutes)')
    plt.grid(True)
    plt.legend()

    # Plot win/loss ratio per session
    plt.subplot(2, 1, 2)
    plt.plot(sessions, player_data["win_loss_ratio"], marker='x', color='r', label='Win/Loss Ratio')
    plt.xlabel('Session')
    plt.ylabel('Win/Loss Ratio')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Load and visualize player data
with open("player_data.json", "r") as f:
    loaded_player_data = json.load(f)

visualize_player_data(loaded_player_data)
