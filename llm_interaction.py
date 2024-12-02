import requests

class GroqLLMInteraction:
    def __init__(self, api_key):
        """
        Initialize Groq LLM interaction with API key
        """
        self.api_key = api_key
        self.base_url = "https://api.groq.cloud/v1/llama_70b"

    def send_prompt(self, prompt_text, max_tokens=200):
        """
        Send prompt to Groq LLama 70b API
        
        Args:
            prompt_text (str): Prompt to send to LLM
            max_tokens (int): Maximum tokens to generate
        
        Returns:
            str: LLM response
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "prompt": prompt_text,
                "max_tokens": max_tokens
            }
            
            response = requests.post(self.base_url, headers=headers, json=data)
            response.raise_for_status()
            
            return response.json().get("choices", [{}])[0].get("text", "")
        
        except requests.RequestException as e:
            print(f"Error interacting with Groq API: {e}")
            return ""

    def generate_fallacy_explanation(self, fallacy_type):
        """
        Generate an explanation for a specific fallacy type
        
        Args:
            fallacy_type (str): Type of fallacy to explain
        
        Returns:
            str: Explanation of the fallacy
        """
        prompt = f"""
        Provide a concise explanation of the '{fallacy_type}' logical fallacy. 
        Include:
        1. A brief definition
        2. Why it weakens an argument
        3. A clear example demonstrating the fallacy
        """
        
        return self.send_prompt(prompt)

    def identify_fallacies(self, argument):
        """
        Identify potential fallacies in an argument
        
        Args:
            argument (str): Argument to analyze
        
        Returns:
            list: Detected fallacies with details
        """
        prompt = f"""
        Analyze the following argument for logical fallacies:
        "{argument}"

        Identify fallacies across these levels:
        - Level 0: Presence of fallacy (Yes/No)
        - Level 1: Fallacy Category (Pathos, Ethos, Logos)
        - Level 2: Specific Fallacy Type

        For each detected fallacy, provide:
        1. Fallacy Type
        2. Reasoning for identification
        3. How it undermines the argument
        """
        
        return self.send_prompt(prompt)