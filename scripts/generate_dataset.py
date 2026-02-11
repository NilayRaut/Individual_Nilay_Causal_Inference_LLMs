"""
Generate a coherent dataset for causal inference analysis.
Ensures task_type matches instruction and uses realistic text samples.
"""

import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Sample texts for different task types
CLASSIFICATION_TEXTS = [
    "This movie was absolutely fantastic! I loved every minute of it.",
    "The service was terrible and the food was cold.",
    "I'm not sure how I feel about this product. It's okay I guess.",
    "Best purchase ever! Highly recommend to everyone.",
    "Waste of money. Very disappointed with the quality.",
    "The book was engaging and well-written throughout.",
    "This restaurant exceeded all my expectations.",
    "The product broke after just one week of use.",
    "An incredible experience from start to finish.",
    "Not worth the price. There are better alternatives.",
]

SUMMARIZATION_TEXTS = [
    "Artificial intelligence has made significant progress in recent years. Machine learning algorithms can now perform tasks that were once thought to require human intelligence. Deep learning, a subset of machine learning, has been particularly successful in areas like image recognition and natural language processing.",
    "Climate change is one of the most pressing issues of our time. Rising global temperatures are causing ice caps to melt, sea levels to rise, and weather patterns to become more extreme. Scientists agree that human activities, particularly the burning of fossil fuels, are the primary cause.",
    "The human brain is an incredibly complex organ. It contains approximately 86 billion neurons that communicate through trillions of connections. Despite decades of research, scientists are still working to understand how consciousness emerges from neural activity.",
    "The internet has revolutionized how we communicate and access information. What started as a military research project has become an essential part of modern life. Today, billions of people use the internet daily for work, education, and entertainment.",
    "Quantum computing represents a paradigm shift in computational power. Unlike classical computers that use bits, quantum computers use qubits that can exist in multiple states simultaneously. This allows them to solve certain problems exponentially faster than traditional computers.",
]

QA_CONTEXTS = [
    ("What is the capital of France?", "France is a country in Western Europe. Its capital and largest city is Paris, known for the Eiffel Tower and rich cultural heritage."),
    ("Who wrote Romeo and Juliet?", "William Shakespeare was an English playwright and poet. He wrote many famous plays including Romeo and Juliet, Hamlet, and Macbeth."),
    ("What is photosynthesis?", "Photosynthesis is the process by which plants convert light energy into chemical energy. Plants use sunlight, water, and carbon dioxide to produce glucose and oxygen."),
    ("When did World War II end?", "World War II was a global conflict that lasted from 1939 to 1945. It ended in 1945 with the surrender of Germany in May and Japan in September."),
    ("What is the speed of light?", "The speed of light in a vacuum is approximately 299,792,458 meters per second. This is considered the universal speed limit according to Einstein's theory of relativity."),
]

TRANSLATION_TEXTS = [
    "Hello, how are you today?",
    "The weather is beautiful this morning.",
    "I would like to order a coffee please.",
    "Where is the nearest train station?",
    "Thank you very much for your help.",
    "Good morning, have a great day!",
    "I love learning new languages.",
    "This is a wonderful opportunity.",
    "Can you help me find my way?",
    "The book is on the table.",
]

REASONING_TEXTS = [
    "If all cats are mammals, and all mammals are animals, then all cats are animals.",
    "The sky appears blue because of Rayleigh scattering.",
    "Water boils at 100 degrees Celsius at sea level because that's when vapor pressure equals atmospheric pressure.",
    "Plants grow toward light because of phototropism.",
    "Ice floats on water because it is less dense than liquid water.",
    "The Earth orbits the Sun due to gravitational attraction.",
    "Vaccines work by training the immune system to recognize pathogens.",
    "Metals conduct electricity because they have free electrons.",
    "The moon causes tides through gravitational pull on Earth's oceans.",
    "Sound travels faster in water than in air due to density differences.",
]

def generate_task_data(n_tasks=1000):
    """Generate coherent task data."""
    
    task_types = ['classification', 'summarization', 'qa', 'translation', 'reasoning']
    difficulties = ['easy', 'medium', 'hard']
    
    data = []
    
    for i in range(n_tasks):
        task_type = random.choice(task_types)
        difficulty = random.choice(difficulties)
        
        # Generate appropriate instruction and input based on task type
        if task_type == 'classification':
            input_text = random.choice(CLASSIFICATION_TEXTS)
            instruction = f"Classify the sentiment of this text as positive, negative, or neutral: {input_text}"
        
        elif task_type == 'summarization':
            input_text = random.choice(SUMMARIZATION_TEXTS)
            instruction = f"Summarize the following text in one sentence: {input_text}"
        
        elif task_type == 'qa':
            question, context = random.choice(QA_CONTEXTS)
            input_text = f"Question: {question} Context: {context}"
            instruction = f"Answer the question based on the context: {input_text}"
        
        elif task_type == 'translation':
            input_text = random.choice(TRANSLATION_TEXTS)
            instruction = f"Translate this English text to French: {input_text}"
        
        elif task_type == 'reasoning':
            input_text = random.choice(REASONING_TEXTS)
            instruction = f"Explain the reasoning behind this statement: {input_text}"
        
        data.append({
            'task_id': i,
            'task_type': task_type,
            'difficulty': difficulty,
            'instruction': instruction,
            'input': input_text
        })
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    # Generate dataset
    df = generate_task_data(n_tasks=1000)
    
    # Save to CSV
    output_path = '../Example1_Dataset/instruction_format_data.csv'
    df.to_csv(output_path, index=False)
    
    print(f"Generated {len(df)} tasks")
    print(f"\nTask type distribution:")
    print(df['task_type'].value_counts())
    print(f"\nDifficulty distribution:")
    print(df['difficulty'].value_counts())
    print(f"\nSaved to: {output_path}")
    print(f"\nSample rows:")
    print(df.head(3))
