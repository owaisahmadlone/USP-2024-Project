FALLACY_PROMPTS = {
    'identification': """
    Analyze the following argument for logical fallacies:
    "{argument}"

    Identify potential logical fallacies using the MAFALDA taxonomy:
    1. Detect the presence of fallacies
    2. Categorize fallacies (Pathos/Ethos/Logos)
    3. Specify the exact fallacy type

    Respond in a structured JSON format with the following keys:
    - type: Specific fallacy name
    - category: Pathos/Ethos/Logos
    - reasoning: Brief explanation of why it's a fallacy

    Example response format:
    [
        {
            "type": "Slippery Slope",
            "category": "Logos",
            "reasoning": "Argument suggests an extreme outcome from a small initial action"
        }
    ]
    """,
    
    'explanation': """
    Provide a detailed breakdown of the '{fallacy_type}' fallacy in the context of this argument:
    "{argument}"

    Include:
    1. Precise definition of the fallacy
    2. Specific points in the argument that demonstrate the fallacy
    3. How the fallacy undermines the argument's credibility
    4. A concise example illustrating this type of fallacious reasoning
    """,
    
    'multi_fallacy_detection': """
    Comprehensively analyze the argument for multiple potential logical fallacies:
    "{argument}"

    Guidelines:
    1. Identify all present fallacies
    2. Categorize each fallacy
    3. Explain how each fallacy impacts the overall argument
    4. Prioritize fallacies by their severity and impact on reasoning
    """
}