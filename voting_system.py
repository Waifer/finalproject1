import csv
import os

class VotingSystem:
    """Class to manage voting operations."""

    def __init__(self, data_file: str = 'votes.csv'):
        self.data_file = data_file
        self.candidates = {1: 'John', 2: 'Jane'}
        self.votes = {'John': 0, 'Jane': 0}
        self._load_votes()

    def _load_votes(self) -> None:
        """Load votes from the CSV file if it exists."""
        if os.path.exists(self.data_file):
            with open(self.data_file, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] in self.votes:
                        self.votes[row[0]] += int(row[1])

    def vote_for_candidate(self, candidate_number: int) -> str:
        """Register a vote for a candidate."""
        candidate_name = self.candidates.get(candidate_number)
        if candidate_name:
            self.votes[candidate_name] += 1
            self._save_votes()
            return f'Voted for {candidate_name}'
        return 'Invalid candidate'

    def _save_votes(self) -> None:
        """Save the current votes to the CSV file."""
        with open(self.data_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for candidate, count in self.votes.items():
                writer.writerow([candidate, count])

    def get_results(self) -> str:
        """Return a formatted string of the voting results."""
        total_votes = sum(self.votes.values())
        results = f"John - {self.votes['John']}, Jane - {self.votes['Jane']}, Total - {total_votes}"
        return results
