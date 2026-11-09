import sys
import tkinter as tk
from tkinter import messagebox, ttk

# System Sound fallback for cross-platform audio effects
try:
    import winsound
    def play_sound(freq=1000, dur=100):
        winsound.Beep(freq, dur)
except ImportError:
    def play_sound(freq=1000, dur=100):
        print("\a")  # Console bell sound fallback

# Global state to prevent main application exit during gameplay
is_game_running = False

class MainDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Visual Programming Multi-Game Hub - Lab Mid")
        self.geometry("600x450")
        self.configure(bg="#1e1e2e")
        
        # Prevent window closing when game is running
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.create_widgets()

    def create_widgets(self):
        # Header & Credits (As instructed by Sir Muhammad Abdullah)
        title_label = tk.Label(
            self, 
            text="🎮 MULTI-GAME PLATFORM", 
            font=("Helvetica", 20, "bold"), 
            fg="#cdd6f4", 
            bg="#1e1e2e"
        )
        title_label.pack(pady=15)
        
        # Project Credits Card
        credits_frame = tk.Frame(self, bg="#313244", bd=2, relief="groove")
        credits_frame.pack(fill="x", padx=30, pady=5)
        
        dev_label = tk.Label(
            credits_frame, 
            text="Developed by: Student Developer & Sir Muhammad Abdullah", 
            font=("Helvetica", 11, "bold"), 
            fg="#a6e3a1", 
            bg="#313244"
        )
        dev_label.pack(pady=8)
        
        guide_label = tk.Label(
            credits_frame, 
            text="Supervised by: Sir Muhammad Abdullah | Lab Mid Project (50 Marks)", 
            font=("Helvetica", 9, "italic"), 
            fg="#bac2de", 
            bg="#313244"
        )
        guide_label.pack(pady=(0, 8))

        # Game Launch Controls
        btn_frame = tk.Frame(self, bg="#1e1e2e")
        btn_frame.pack(pady=30)
        
        ludo_btn = tk.Button(
            btn_frame, 
            text="🎲 Launch Ludo (4-Player)", 
            font=("Helvetica", 12, "bold"),
            bg="#89b4fa", 
            fg="#11111b", 
            padx=20, 
            pady=10,
            command=self.launch_ludo
        )
        ludo_btn.pack(fill="x", pady=10)

        chess_btn = tk.Button(
            btn_frame, 
            text="♟️ Launch Chess (3D UI & Chat)", 
            font=("Helvetica", 12, "bold"),
            bg="#f9e2af", 
            fg="#11111b", 
            padx=20, 
            pady=10,
            command=self.launch_chess
        )
        chess_btn.pack(fill="x", pady=10)

    def launch_ludo(self):
        global is_game_running
        is_game_running = True
        play_sound(800, 150)
        LudoGameWindow(self)

    def launch_chess(self):
        global is_game_running
        is_game_running = True
        play_sound(1200, 150)
        ChessGameWindow(self)

    def on_close(self):
        global is_game_running
        if is_game_running:
            messagebox.showwarning(
                "Warning", 
                "You cannot close the application while a game is running."
            )
        else:
            self.destroy()

# ---------------------------------------------------------
# LUDO GAME WINDOW (4-PLAYER & SOUNDS)
# ---------------------------------------------------------
class LudoGameWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Ludo - 4 Player Edition")
        self.geometry("600x650")
        self.configure(bg="#181825")
        
        self.protocol("WM_DELETE_WINDOW", self.on_game_close)
        
        self.players = ["Red", "Green", "Yellow", "Blue"]
        self.current_turn = 0
        
        self.setup_ui()

    def setup_ui(self):
        # Credits Bar
        credits_bar = tk.Label(
            self, 
            text="Ludo Engine | Credits: Sir Muhammad Abdullah & Developer", 
            bg="#313244", 
            fg="#cdd6f4", 
            font=("Helvetica", 9)
        )
        credits_bar.pack(fill="x")

        # 4-Player Status Dashboard
        self.status_label = tk.Label(
            self, 
            text=f"Current Turn: {self.players[self.current_turn]} Player", 
            font=("Helvetica", 14, "bold"), 
            fg="#f38ba8", 
            bg="#181825"
        )
        self.status_label.pack(pady=10)

        # Ludo Board Visualization Canvas
        self.canvas = tk.Canvas(self, width=400, height=400, bg="#cdd6f4")
        self.canvas.pack(pady=10)
        self.draw_ludo_board()

        # Controls & Sound Action
        ctrl_frame = tk.Frame(self, bg="#181825")
        ctrl_frame.pack(pady=10)
        
        self.dice_label = tk.Label(
            ctrl_frame, 
            text="🎲 Dice: -", 
            font=("Helvetica", 14, "bold"), 
            fg="#cdd6f4", 
            bg="#181825"
        )
        self.dice_label.grid(row=0, column=0, padx=15)

        roll_btn = tk.Button(
            ctrl_frame, 
            text="Roll Dice", 
            font=("Helvetica", 11, "bold"), 
            bg="#a6e3a1",
            command=self.roll_dice
        )
        roll_btn.grid(row=0, column=1, padx=15)

    def draw_ludo_board(self):
        # 4 Player Quadrants
        self.canvas.create_rectangle(0, 0, 160, 160, fill="#f38ba8", outline="black") # Red
        self.canvas.create_rectangle(240, 0, 400, 160, fill="#a6e3a1", outline="black") # Green
        self.canvas.create_rectangle(240, 240, 400, 400, fill="#f9e2af", outline="black") # Yellow
        self.canvas.create_rectangle(0, 240, 160, 400, fill="#89b4fa", outline="black") # Blue
        self.canvas.create_rectangle(160, 160, 240, 240, fill="#cba6f7", outline="black") # Home Center

    def roll_dice(self):
        import random
        play_sound(600, 80) # Dice Roll Sound Effect
        val = random.randint(1, 6)
        self.dice_label.config(text=f"🎲 Dice: {val}")
        
        # Move Turn to Next Player
        self.current_turn = (self.current_turn + 1) % 4
        colors = ["#f38ba8", "#a6e3a1", "#f9e2af", "#89b4fa"]
        self.status_label.config(
            text=f"Current Turn: {self.players[self.current_turn]} Player",
            fg=colors[self.current_turn]
        )
        play_sound(1000, 50) # Token Move Sound Effect

    def on_game_close(self):
        global is_game_running
        is_game_running = False
        self.destroy()

# ---------------------------------------------------------
# CHESS GAME WINDOW (REALISTIC UI & CHAT SYSTEM)
# ---------------------------------------------------------
class ChessGameWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Chess Pro - 3D Interface & Live Chat")
        self.geometry("750x550")
        self.configure(bg="#181825")
        
        self.protocol("WM_DELETE_WINDOW", self.on_game_close)
        self.setup_ui()

    def setup_ui(self):
        # Main Layout Split (Board Left, Chat Right)
        left_frame = tk.Frame(self, bg="#181825")
        left_frame.pack(side="left", padx=15, pady=15)

        right_frame = tk.Frame(self, bg="#313244", bd=2, relief="ridge")
        right_frame.pack(side="right", fill="both", expand=True, padx=15, pady=15)

        # Chessboard Rendering (Realistic Wooden Theme & 3D Pieces Symbols)
        board_title = tk.Label(
            left_frame, 
            text="Realistic 3D Chess Board", 
            font=("Helvetica", 12, "bold"), 
            fg="#cdd6f4", 
            bg="#181825"
        )
        board_title.pack(pady=5)

        self.chess_canvas = tk.Canvas(left_frame, width=400, height=400)
        self.chess_canvas.pack()
        self.draw_realistic_chess_board()

        # Chat Interface (Requirement 5)
        chat_title = tk.Label(
            right_frame, 
            text="💬 In-Game Player Chat", 
            font=("Helvetica", 11, "bold"), 
            fg="#cdd6f4", 
            bg="#313244"
        )
        chat_title.pack(pady=5)

        self.chat_history = tk.Text(
            right_frame, 
            width=30, 
            height=18, 
            bg="#1e1e2e", 
            fg="#cdd6f4", 
            font=("Helvetica", 9),
            state="disabled"
        )
        self.chat_history.pack(padx=10, pady=5, fill="both", expand=True)

        entry_frame = tk.Frame(right_frame, bg="#313244")
        entry_frame.pack(fill="x", padx=10, pady=10)

        self.msg_entry = tk.Entry(entry_frame, font=("Helvetica", 10))
        self.msg_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.msg_entry.bind("<Return>", lambda e: self.send_chat())

        send_btn = tk.Button(
            entry_frame, 
            text="Send", 
            bg="#89b4fa", 
            fg="#11111b", 
            font=("Helvetica", 9, "bold"),
            command=self.send_chat
        )
        send_btn.pack(side="right")

    def draw_realistic_chess_board(self):
        # High quality realistic wooden palette colors
        colors = ["#eeeed2", "#769656"]
        pieces_white = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
        pieces_black = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
        
        sq = 50
        for r in range(8):
            for c in range(8):
                color = colors[(r + c) % 2]
                self.chess_canvas.create_rectangle(
                    c*sq, r*sq, (c+1)*sq, (r+1)*sq, fill=color, outline=""
                )
                
                # Render Unicode symbols representing 3D styled chess pieces
                if r == 0:
                    self.chess_canvas.create_text(
                        c*sq+25, r*sq+25, text=pieces_black[c], 
                        font=("Helvetica", 24, "bold"), fill="#11111b"
                    )
                elif r == 1:
                    self.chess_canvas.create_text(
                        c*sq+25, r*sq+25, text="♟", 
                        font=("Helvetica", 24, "bold"), fill="#11111b"
                    )
                elif r == 6:
                    self.chess_canvas.create_text(
                        c*sq+25, r*sq+25, text="♙", 
                        font=("Helvetica", 24, "bold"), fill="#ffffff"
                    )
                elif r == 7:
                    self.chess_canvas.create_text(
                        c*sq+25, r*sq+25, text=pieces_white[c], 
                        font=("Helvetica", 24, "bold"), fill="#ffffff"
                    )

    def send_chat(self):
        msg = self.msg_entry.get().strip()
        if msg:
            play_sound(1500, 40)
            self.chat_history.config(state="normal")
            self.chat_history.insert("end", f"Player: {msg}\n")
            self.chat_history.config(state="disabled")
            self.chat_history.see("end")
            self.msg_entry.delete(0, "end")

    def on_game_close(self):
        global is_game_running
        is_game_running = False
        self.destroy()

if __name__ == "__main__":
    app = MainDashboard()
    app.mainloop()
