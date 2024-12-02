import os
from dotenv import load_dotenv
from fallacy_detector import FallacyDetector
from llm_interaction import GroqLLMInteraction

# Load environment variables
load_dotenv()

class FallacyIdentificationApp:
    def __init__(self):
        # Initialize Groq API interaction
        api_key = os.getenv('GROQ_API_KEY')
        if not api_key:
            raise ValueError("Groq API Key not found. Please set GROQ_API_KEY in .env file")
        
        self.llm_interaction = GroqLLMInteraction(api_key)
        self.fallacy_detector = FallacyDetector(self.llm_interaction)

    def run_interactive_session(self):
        """
        Run an interactive fallacy identification session
        """
        print("Welcome to MAFALDA: Logical Fallacy Detection System")
        
        while True:
            # Get argument from user
            argument = input("\nEnter an argument to analyze (or 'quit' to exit): ")
            
            if argument.lower() == 'quit':
                break
            
            try:
                # Analyze argument for fallacies
                results = self.fallacy_detector.analyze_argument(argument)
                
                # Display results
                self.display_results(results)
            
            except Exception as e:
                print(f"Error analyzing argument: {e}")

    def display_results(self, results):
        """
        Display fallacy detection results
        """
        print("\n--- Fallacy Analysis Results ---")
        
        if not results:
            print("No fallacies detected in the argument.")
            return
        
        for fallacy in results:
            print(f"Detected Fallacy: {fallacy['type']}")
            print(f"Description: {fallacy['description']}")
            print(f"Example: {fallacy['example']}")
            print("---")

def main():
    app = FallacyIdentificationApp()
    app.run_interactive_session()

if __name__ == "__main__":
    main()