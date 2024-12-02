import json
from prompts import FALLACY_PROMPTS
from data_processing import MAFALDADataset

class FallacyDetector:
    def __init__(self, llm_interaction):
        """
        Initialize Fallacy Detector with LLM interaction
        
        Args:
            llm_interaction: LLM interaction handler
        """
        self.llm_interaction = llm_interaction
        self.mafalda_dataset = MAFALDADataset()

    def analyze_argument(self, argument):
        """
        Comprehensive analysis of an argument for logical fallacies
        
        Args:
            argument (str): Argument to analyze
        
        Returns:
            list: Detected fallacies with details
        """
        # Initial fallacy identification
        fallacy_identification = self._identify_fallacies(argument)
        
        # Detailed fallacy analysis
        detailed_fallacies = self._analyze_fallacies(argument, fallacy_identification)
        
        return detailed_fallacies

    def _identify_fallacies(self, argument):
        """
        Identify potential fallacies in the argument
        
        Args:
            argument (str): Argument to analyze
        
        Returns:
            list: Initial fallacy identifications
        """
        fallacy_prompt = FALLACY_PROMPTS['identification'].format(argument=argument)
        
        raw_response = self.llm_interaction.send_prompt(fallacy_prompt)
        
        try:
            fallacies = json.loads(raw_response)
            return fallacies
        except json.JSONDecodeError:
            return []

    def _analyze_fallacies(self, argument, fallacy_list):
        """
        Provide detailed analysis for each detected fallacy
        
        Args:
            argument (str): Original argument
            fallacy_list (list): List of initially detected fallacies
        
        Returns:
            list: Detailed fallacy information
        """
        detailed_fallacies = []
        
        for fallacy in fallacy_list:
            explanation_prompt = FALLACY_PROMPTS['explanation'].format(
                argument=argument,
                fallacy_type=fallacy['type']
            )
            
            explanation = self.llm_interaction.send_prompt(explanation_prompt)
            
            detailed_fallacies.append({
                'type': fallacy['type'],
                'description': explanation,
                'example': self._get_example_from_mafalda(fallacy['type'])
            })
        
        return detailed_fallacies

    def _get_example_from_mafalda(self, fallacy_type):
        """
        Retrieve an example for a fallacy from MAFALDA dataset
        
        Args:
            fallacy_type (str): Type of fallacy
        
        Returns:
            str: Example text for the fallacy
        """
        return self.mafalda_dataset.get_example(fallacy_type)