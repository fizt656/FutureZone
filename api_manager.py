# api_manager.py
import aiohttp
import json
from config import OPENROUTER_URL, ANTHROPIC_URL, OPENROUTER_HEADERS, ANTHROPIC_HEADERS, OPENROUTER_MODELS, CLAUDE_MODELS, DEFAULT_CLAUDE_MODEL, ANTHROPIC_MAX_TOKENS

class APIManager:
    def __init__(self):
        self.current_llm = "anthropic"
        self.current_claude_model = DEFAULT_CLAUDE_MODEL
        self.current_openrouter_model = list(OPENROUTER_MODELS.keys())[0]

    async def generate_response(self, message, conversation_manager):
        if self.current_llm == "anthropic":
            response_text = await self.generate_anthropic_response(message, conversation_manager)
        elif self.current_llm == "openrouter":
            response_text = await self.generate_openrouter_response(message, conversation_manager)
        else:
            response_text = "Invalid LLM selected."
        return response_text

    async def generate_anthropic_response(self, message, conversation_manager):
        # Remove any system messages from the conversation
        filtered_conversation = [msg for msg in conversation_manager.get_conversation() if msg['role'] != 'system']
        
        data = {
            "model": self.current_claude_model,
            "system": conversation_manager.system_prompt,
            "messages": filtered_conversation + [{"role": "user", "content": message}],
            "max_tokens": ANTHROPIC_MAX_TOKENS,
            "temperature": 0.7
        }

        print(f"Sending request to Anthropic API with data: {json.dumps(data, indent=2)}")
        print(f"Headers: {json.dumps(ANTHROPIC_HEADERS, indent=2)}")

        async with aiohttp.ClientSession() as session:
            async with session.post(ANTHROPIC_URL, json=data, headers=ANTHROPIC_HEADERS) as response:
                try:
                    response_text = await response.text()
                    print(f"Raw response from Anthropic API: {response_text}")
                    
                    response_json = json.loads(response_text)
                    if response.status == 200:
                        if 'content' in response_json:
                            content = response_json['content']
                            response_text = ""
                            for item in content:
                                if item['type'] == 'text':
                                    response_text += item['text']
                            return response_text.strip()
                        else:
                            print(f"Error: 'content' key not found in the Anthropic API response. Full response: {response_json}")
                    else:
                        print(f"Error: Anthropic API returned status code {response.status}")
                        print(f"Error details: {response_json}")
                except Exception as e:
                    print(f"Error: {str(e)}")
                    print(f"Raw response: {response_text}")
                
                return "I apologize, but I encountered an error while processing your request."

    async def generate_openrouter_response(self, message, conversation_manager):
        full_conversation = [{"role": "system", "content": conversation_manager.system_prompt}] + conversation_manager.get_conversation() + [{"role": "user", "content": message}]

        async with aiohttp.ClientSession() as session:
            async with session.post(OPENROUTER_URL, json={
                "model": self.current_openrouter_model,
                "messages": full_conversation
            }, headers=OPENROUTER_HEADERS) as response:
                response_json = await response.json()
                if 'choices' in response_json and len(response_json['choices']) > 0:
                    response_text = response_json['choices'][0]['message']['content']
                    return response_text
                else:
                    return "No response generated."

    def switch_llm(self):
        self.current_llm = "openrouter" if self.current_llm == "anthropic" else "anthropic"

    def get_current_llm(self):
        return self.current_llm

    def switch_claude_model(self, model_code):
        for full_name, short_code in CLAUDE_MODELS.items():
            if model_code.lower() == short_code.lower():
                self.current_claude_model = full_name
                self.current_llm = "anthropic"
                return True
        return False

    def switch_openrouter_model(self, model_code):
        for full_name, short_code in OPENROUTER_MODELS.items():
            if model_code.lower() == short_code.lower():
                self.current_openrouter_model = full_name
                self.current_llm = "openrouter"
                return True
        return False

    def get_current_model(self):
        if self.current_llm == "anthropic":
            return self.current_claude_model
        else:
            return self.current_openrouter_model