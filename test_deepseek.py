import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_deepseek_translation():
    """Test DeepSeek API translation"""
    try:
        # Get API key and endpoint from environment variables
        api_key = os.getenv("DEEPSEEK_API_KEY")
        endpoint = os.getenv("DEEPSEEK_ENDPOINT", "https://api.deepseek.com/chat/completions")
        model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
        
        # Check if API key is set
        if not api_key or api_key == "your_deepseek_api_key_here":
            print("Please set your DeepSeek API key in the .env file")
            return
        
        # Test prompt
        prompt = """You are a professional translator who specializes in translating Chinese to natural, authentic American English.
        
        Requirements:
        1. Provide 3-5 different translation options
        2. Translations must be natural and authentic, but not overly casual or artificial
        3. If applicable, include commonly used slang with a note
        4. If there are differences in usage context (formal/informal) or audience, please indicate
        5. Format: Each translation on a new line, followed by context notes in parentheses if needed
        6. Do not include explanations or numbering, only the translations and optional notes
        
        Chinese: 你好
        English:"""
        
        # Prepare request payload
        payload = {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 300,
            "temperature": 0.7
        }
        
        # Set headers
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Make API request
        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()
        
        # Parse response
        result = response.json()
        content = result["choices"][0]["message"]["content"]
        
        print("DeepSeek API Response:")
        print(content)
        
    except Exception as e:
        print(f"Error in DeepSeek translation: {e}")

if __name__ == "__main__":
    test_deepseek_translation()