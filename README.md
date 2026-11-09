
# 🎮 AN Games Arena (Visual Programming Project)

Developed by **Uneba Rana & Sir Muhammad Abdullah**

**Technology:** C# Windows Forms  
**Framework:** .NET 8  
**Project Type:** Multiplayer LAN Gaming Application

---

## 🎯 Project Overview

AN Games Arena is a multiplayer gaming application developed using C# Windows Forms. It allows players to enjoy different games over LAN or the same Wi-Fi network.

### 🎲 Available Games

- **Ludo:** 2–4 Players with Sound Effects.
- **Chess:** Realistic Chess Board with 3D-Style Pieces and Chat.
- **Tic-Tac-Toe:** Multiplayer Tic-Tac-Toe Game.

---

## 🚀 How to Run the Project

### Requirements

1. Install .NET 8 SDK.
2. Install Visual Studio 2022.
3. Select ".NET Desktop Development" workload.
4. Open `LanGames.csproj`.
5. Press **F5** to run the application.

Alternatively, run the following command:

```bash
dotnet run
```

Allow the application through Windows Firewall on the Private Network when prompted.

---

## 🎮 How to Play

1. Enter your player name.
2. Select your favorite game.
3. Click **Host Game** to create a new game.
4. For Ludo, select 2, 3, or 4 players.
5. Other players can click **Join Game**.
6. Select the host from the available list or enter the host IP address.
7. Start playing with your friends!

### Local Testing

To test the application on one computer:

- Run the application 2–4 times.
- Join using IP address `127.0.0.1`.

---

## ✅ Project Requirements (Sir's Checklist)

| # | Requirement | Implementation |
|---|---|---|
| 1 | Main window cannot close during an active game | `Form1.OnFormClosing`, `GameForm.ActiveGames` |
| 2 | Developer credits | `AppInfo` in `UI.cs` |
| 3 | Ludo sound effects and 4-player support | `Sfx.cs`, `LudoForm.cs`, `NetworkPeer.cs` |
| 4 | Realistic Chess UI with 3D-style pieces | `ChessBoard` in `ChessForm.cs` |
| 5 | Chess chat system | Right-side panel in `ChessForm.cs` |
| 6 | Public GitHub Repository | GitHub |

---

## 🛠️ Technologies Used

- C#
- Windows Forms
- .NET 8
- TCP/IP Networking
- LAN / Wi-Fi Multiplayer
- Visual Studio 2022
- Git & GitHub

---

## 📸 Screenshots

Add your project screenshots here.

### Main Screen
![Main Screen](Screenshots/main-screen.png)

### Ludo Game
![Ludo Game](Screenshots/ludo.png)

### Chess Game
![Chess Game](Screenshots/chess.png)

### Tic-Tac-Toe
![Tic Tac Toe](Screenshots/tic-tac-toe.png)

---

## 👩‍💻 Developers

- **Uneba Rana**
- **Sir Muhammad Abdullah**
- **Team Members:** Add team members' names here.

---

## 📂 Project Structure

```text
AN-Games-Arena/
│
├── LanGames.csproj
├── Program.cs
├── Form1.cs
├── UI.cs
├── Sfx.cs
├── NetworkPeer.cs
├── LudoForm.cs
├── ChessForm.cs
├── GameForm.cs
├── README.md
└── Screenshots/
```

---

## 🌐 GitHub Repository Setup

Run these commands in your project terminal:

```bash
git init
git add .
git commit -m "AN Games Arena - Final Version"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

To make your repository public:

1. Open your GitHub repository.
2. Go to **Settings**.
3. Select **General**.
4. Scroll down to **Danger Zone**.
5. Click **Change visibility**.
6. Select **Public**.

---

## ⭐ Project Features

- Multiplayer Gaming
- LAN / Wi-Fi Connectivity
- Real-Time Communication
- Ludo Sound Effects
- Chess Chat System
- 2–4 Player Ludo Support
- User-Friendly Interface

---

**AN Games Arena – Play Together, Enjoy Together! 🎮**

