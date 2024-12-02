import json
import os

class MAFALDADataset:
    def __init__(self, dataset_path='data/mafalda_dataset.json'):
        """
        Initialize MAFALDA Dataset handler
        
        Args:
            dataset_path (str): Path to MAFALDA dataset JSON
        """
        self.dataset_path = dataset_path
        self.dataset = self._load_dataset()

    def _load_dataset(self):
        """
        Load MAFALDA dataset from JSON file
        
        Returns:
            dict: Parsed dataset
        """
        try:
            with open(self.dataset_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Dataset not found at {self.dataset_path}. Using minimal dataset.")
            return self._create_minimal_dataset()

    def _create_minimal_dataset(self):
        """
        Create a minimal fallacy dataset for demonstration
        
        Returns:
            dict: Minimal fallacy dataset
        """
        return {
            'slippery_slope': [
                "If we allow X, then Y will inevitably happen, leading to catastrophic Z."
            ],
            'false_causality': [
                "After I started wearing lucky socks, my team started winning. Therefore, my socks cause our victories."
            ],
            # Add more fallacy examples
        }

    def get_example(self, fallacy_type):
        """
        Retrieve an example for a specific fallacy type
        
        Args:
            fallacy_type (str): Type of fallacy
        
        Returns:
            str: Example text for the fallacy
        """
        # Normalize fallacy type for dataset lookup
        normalized_type = fallacy_type.lower().replace(' ', '_')
        
        examples = self.dataset.get(normalized_type, [])
        
        # Return first example if available, else a generic message
        return examples[0] if examples else "No example available for this fallacy."

    def add_example(self, fallacy_type, example):
        """
        Add a new example to the dataset
        
        Args:
            fallacy_type (str): Type of fallacy
            example (str): Example text
        """
        normalized_type = fallacy_type.lower().replace(' ', '_')
        
        if normalized_type not in self.dataset:
            self.dataset[normalized_type] = []
        
        self.dataset[normalized_type].append(example)
        
        # Optional: Save updated dataset
        self._save_dataset()

    def _save_dataset(self):
        """
        Save updated dataset back to JSON file
        """
        os.makedirs(os.path.dirname(self.dataset_path), exist_ok=True)
        with open(self.dataset_path, 'w') as f:
            json.dump(self.dataset, f, indent=2)