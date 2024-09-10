# conversation_manager.py
import os
import re
from datetime import datetime
from characters import characters

class ConversationManager:
    def __init__(self, character_name):
        self.character_name = character_name
        self.system_prompt = characters[character_name]["system_prompt"]
        self.conversation = []
        self.log_file = ""
        self.subfolder_path = ""
        self.log_file_name_response = None

    def add_user_message(self, message):
        if message != self.log_file_name_response:
            self.conversation.append({"role": "user", "content": message})
            self.save_message_to_log("User", message)

    def add_assistant_response(self, response):
        self.conversation.append({"role": "assistant", "content": response})
        self.save_message_to_log("Bot", response)

    def delete_last_message(self):
        if len(self.conversation) > 1:
            return self.conversation.pop()
        return None

    def edit_last_message(self, new_content):
        if len(self.conversation) > 1:
            self.conversation[-1]["content"] = new_content
            return self.conversation[-1]
        return None

    def get_conversation(self):
        return self.conversation

    def get_last_message(self):
        if len(self.conversation) > 0:
            return self.conversation[-1]["content"]
        return None

    def split_response(self, response, chunk_size=2000):
        return [response[i:i+chunk_size] for i in range(0, len(response), chunk_size)]

    def set_log_file(self, log_file_name):
        if not log_file_name:
            log_file_name = "latest_session"
        
        subfolder_name = log_file_name
        self.subfolder_path = os.path.join(os.getcwd(), subfolder_name)
        counter = 1
        while os.path.exists(self.subfolder_path):
            subfolder_name = f"{log_file_name}_{counter}"
            self.subfolder_path = os.path.join(os.getcwd(), subfolder_name)
            counter += 1
        os.makedirs(self.subfolder_path)
        
        self.log_file = os.path.join(self.subfolder_path, f"{log_file_name}.txt")
        self.log_file_name_response = None

    def save_message_to_log(self, role, message):
        if self.log_file:
            with open(self.log_file, 'a', encoding='utf-8') as file:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"[{timestamp}] **{role}**: {message}\n")

    def resume_conversation(self, directory_path):
        if os.path.exists(directory_path):
            log_files = [f for f in os.listdir(directory_path) if f.endswith(".txt")]
            if log_files:
                log_file_path = os.path.join(directory_path, log_files[0])
                with open(log_file_path, 'r', encoding='utf-8') as file:
                    log_content = file.read()

                conversation_pattern = re.compile(r'\*\*User\*\*: (.*?)\n.*?\*\*Bot\*\*: (.*?)\n', re.DOTALL)
                matches = conversation_pattern.findall(log_content)

                self.conversation = []
                for user_msg, bot_msg in matches:
                    self.conversation.append({"role": "user", "content": user_msg})
                    self.conversation.append({"role": "assistant", "content": bot_msg})

                self.subfolder_path = directory_path
                self.log_file = log_file_path

                return True
        return False

    def clear_conversation(self):
        self.conversation = []
        self.save_message_to_log("System", "Conversation cleared")

    def save_conversation(self):
        if self.log_file:
            with open(self.log_file, 'w', encoding='utf-8') as file:
                for message in self.conversation:
                    role = message["role"].capitalize()
                    content = message["content"]
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    file.write(f"[{timestamp}] **{role}**: {content}\n")