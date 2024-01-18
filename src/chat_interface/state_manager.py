import csv
import logging
import os
import uuid


class StateManager:
    def __init__(self) -> None:
        self.desktop_path = os.path.join(
            os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.file_path = os.path.join(
            self.desktop_path, 'chat-ai', 'resources', 'conversation_state.csv')
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def generate_conversation_id(self) -> str:
        return str(uuid.uuid4())

    def save_state(self, conversation_id: str, state: dict) -> None:
        try:
            existing_states = []
            if os.path.isfile(self.file_path):
                with open(self.file_path, mode='r') as file:
                    reader = csv.reader(file)
                    existing_states = [row for row in reader]

            updated = False
            for i, row in enumerate(existing_states):
                if row[0] == conversation_id:
                    existing_states[i] = [conversation_id,
                                          state['summary'], state['details']]
                    updated = True
                    break

            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                if updated:
                    writer.writerows(existing_states)
                else:
                    writer.writerow(
                        [conversation_id, state['summary'], state['details']])

        except IOError as e:
            logging.error(f"File I/O error: {e}")

    def load_state(self) -> list:
        states = []
        try:
            with open(self.file_path, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    states.append(
                        {'timestamp': row[0], 'summary': row[1], 'details': row[2]})
            return states
        except FileNotFoundError:
            logging.warning("State file not found, returning empty state list")
            return []
        except IOError as e:
            logging.error(f"File IO error in StateManager: {e}")
            return []
