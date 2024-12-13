import tkinter as tk
from tkinter import messagebox
from voting_system import VotingSystem

class VotingApp:
    """GUI for the Voting System."""

    def __init__(self, root: tk.Tk):
        self.voting_system = VotingSystem()
        self.root = root
        self.root.title('Voting App')

        # Create GUI elements
        self.label = tk.Label(root, text='Choose a Candidate:', font=('Arial', 14))
        self.label.pack(pady=10)

        self.vote_john_button = tk.Button(root, text='Vote for John', command=lambda: self.vote(1))
        self.vote_jane_button = tk.Button(root, text='Vote for Jane', command=lambda: self.vote(2))
        self.results_button = tk.Button(root, text='Show Results', command=self.show_results)
        self.exit_button = tk.Button(root, text='Exit', command=root.quit)

        # Pack buttons
        self.vote_john_button.pack(pady=5)
        self.vote_jane_button.pack(pady=5)
        self.results_button.pack(pady=5)
        self.exit_button.pack(pady=5)

    def vote(self, candidate_number: int) -> None:
        """Cast a vote for the selected candidate."""
        result = self.voting_system.vote_for_candidate(candidate_number)
        messagebox.showinfo('Vote', result)

    def show_results(self) -> None:
        """Display the voting results."""
        results = self.voting_system.get_results()
        messagebox.showinfo('Results', results)

if __name__ == '__main__':
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()
