# Multi-Level Causal Inference in Large Language Models

A comprehensive guide to applying causal inference methods to Large Language Models (LLMs), demonstrating both external causality (prompt-level interventions) and internal causality (attention mechanisms as mediators).

## Project Overview

This project bridges traditional causal analysis with modern deep learning by:
- Applying **Propensity Score Matching** to study instruction format effects on task completion
- Using **Causal Mediation Analysis** to understand attention mechanisms in reasoning
- Providing a complete theoretical foundation and practical implementation

## Project Structure

```
Individual_Nilay_Causal_Inference_LLMs/
├── notebooks/
│   ├── 00_setup_and_theory.ipynb      # Theory, DAGs, dataset prep, GPT-2 testing
│   ├── 01_example1_psm.ipynb         # Example 1: Propensity Score Matching
│   └── 02_example2_mediation.ipynb   # Example 2: Mediation Analysis
├── Example1_Dataset/
│   └── instruction_format_data.csv    # Processed instruction format dataset
├── Example2_Dataset/
│   └── attention_reasoning_data.csv  # Processed GSM8K dataset
├── QuizQuestions.md                  # 15 quiz questions with explanations
├── Video_Link.txt                    # Link to video presentation
├── requirements.txt                  # Python dependencies
├── LICENSE                           # MIT License
└── README.md                         # This file
```

## Installation

### 1. Clone or download this repository

### 2. Create a Python virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Navigate to the `notebooks/` directory and open the notebooks in order.

## Notebook Contents

### Notebook 0: Setup and Theory (`00_setup_and_theory.ipynb`)

**Duration**: 4-6 hours

**Content**:
- Comprehensive theory section covering:
  - Causality fundamentals (correlation vs causation, potential outcomes framework)
  - Causal graphs (DAGs) with LLM examples
  - Propensity score matching methodology
  - Causal mediation analysis
  - Data preparation for causal inference
  - LLM-specific considerations
- Two DAG visualizations illustrating:
  - Confounding in instruction format experiments
  - Mediation in attention mechanisms
- Dataset downloads and exploratory analysis:
  - SuperNaturalInstructions (1000 samples) for Example 1
  - GSM8K (500 samples) for Example 2
- GPT-2 model testing and verification

**Key Deliverables**:
- Title & Abstract (150-200 words)
- Complete theory section (~2500 words)
- Working datasets saved to disk
- GPT-2 model confirmed functional

### Notebook 1: Example 1 - Propensity Score Matching (`01_example1_psm.ipynb`)

**Duration**: 6-8 hours

**Research Question**: Does instruction format causally affect task completion quality?

**Content**:
- Generate three instruction formats for each task:
  - Format A: Direct command
  - Format B: Polite request
  - Format C: Few-shot examples
- Measure task completion quality with GPT-2
- Identify confounders (task difficulty, prompt length, task category)
- Estimate propensity scores using logistic regression
- Perform nearest neighbor matching with caliper
- Check balance before/after matching
- Estimate treatment effects (ATE, ATT)
- Conduct sensitivity analyses

**Key Deliverables**:
- Complete causal analysis with proper causal reasoning
- Balance visualizations
- Treatment effect estimates with confidence intervals
- Sensitivity analysis results

### Notebook 2: Example 2 - Mediation Analysis (`02_example2_mediation.ipynb`)

**Duration**: 8-10 hours (spread over 2 days)

**Research Question**: Does chain-of-thought prompting improve reasoning through changes in attention patterns?

**Content**:
- Generate reasoning tasks with and without CoT prompting
- Extract attention patterns from GPT-2 at different layers/heads
- Perform causal mediation analysis using DoWhy
- Decompose total effect into direct and indirect effects
- Visualize attention patterns and mediation paths
- Conduct intervention experiments on attention heads
- Sensitivity analysis for sequential ignorability

**Key Deliverables**:
- Complete mediation analysis
- Attention pattern visualizations
- Effect decomposition (direct vs indirect)
- Intervention experiments results

## Datasets

### Example 1: Instruction Format Dataset
- **Source**: SuperNaturalInstructions or synthetic instruction-following tasks
- **Size**: 1000 samples
- **Variables**: Task type, difficulty, instruction format, input, expected output
- **Use Case**: Studying causal effects of prompt engineering

### Example 2: Attention and Reasoning Dataset
- **Source**: GSM8K (Grade School Math)
- **Size**: 500 math problems
- **Variables**: Question, step-by-step solution, extracted attention weights
- **Use Case**: Studying causal mediation in attention mechanisms

## Key Concepts

### Causal Inference Methods
- **Propensity Score Matching**: Balancing treatment and control groups
- **Causal Mediation Analysis**: Decomposing direct and indirect effects
- **Potential Outcomes Framework**: Counterfactual reasoning

### LLM-Specific Applications
- Prompts as interventions/treatments
- Model outputs as outcomes
- Attention mechanisms as causal mediators
- Confounding in LLM experiments

### Data Preparation for Causality
- Feature selection (confounders vs colliders vs mediators)
- Handling missing data in causal contexts
- Encoding categorical variables
- Common support and overlap requirements

## Dependencies

- **Core ML/DL**: `torch>=2.0.0`, `transformers>=4.30.0`, `datasets>=2.14.0`
- **Causal Inference**: `dowhy>=0.11.0`, `causalml>=0.13.0`, `econml>=0.14.0`
- **Data Processing**: `pandas>=2.0.0`, `numpy>=1.24.0`, `scikit-learn>=1.3.0`
- **Visualization**: `matplotlib>=3.7.0`, `seaborn>=0.12.0`, `plotly>=5.14.0`, `networkx>=3.1.0`

See `requirements.txt` for complete list.

## Model Used

- **GPT-2**: Fully reproducible, no API costs, publicly available
- **Why GPT-2**: Small enough for local execution, large enough for meaningful analysis

## References

### Causal Inference Foundations
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*
- Rubin, D. B. (1974). Estimating causal effects of treatments
- Imbens, G. W., & Rubin, D. B. (2015). *Causal Inference for Statistics, Social, and Biomedical Sciences*

### Propensity Score Matching
- Rosenbaum, P. R., & Rubin, D. B. (1983). The central role of the propensity score
- Stuart, E. A. (2010). Matching methods for causal inference

### Mediation Analysis
- Imai, K., Keele, L., & Tingley, D. (2010). A general approach to causal mediation analysis

### LLM and Attention
- Vaswani, A., et al. (2017). Attention is all you need
- Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Nilay**  
INFO 7390: Crash Course in Causality  
Northeastern University  
Spring 2026

## Acknowledgments

This project demonstrates the integration of causal inference methods with modern deep learning, showing how traditional causal frameworks can be applied to understand and improve Large Language Models.

---

**Note**: All code is designed to be fully reproducible. Set random seeds and document environment details for complete reproducibility.