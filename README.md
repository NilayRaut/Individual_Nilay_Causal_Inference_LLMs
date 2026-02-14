# Multi-Model Causal Inference in Large Language Models

A comprehensive implementation demonstrating causal inference methods across multiple LLM scales (GPT-2, GPT-J, GPT-3.5), with full validation using DoWhy and CausalML libraries.

## Project Overview

This project demonstrates:
- **Multi-model analysis**: GPT-2 (124M), GPT-J (6B), GPT-3.5 (175B+) comparison
- **Propensity Score Matching**: Two complete implementations
  - Example 1: Few-shot prompting effects in LLMs
  - Example 2: Job training program evaluation (LaLonde dataset)
- **Experimental validation**: RCT benchmark for validating PSM
- **Library validation**: DoWhy and CausalML implementations
- **Sensitivity analysis**: Robustness across specifications
- **Emergent properties**: Scale-dependent treatment effects

## Project Structure

```
Individual_Nilay_Causal_Inference_LLMs/
├── .env                                      # YOUR API KEYS (never commit!)
├── .env.example                              # Template for API keys (safe to commit)
├── .gitignore                                # Git ignore rules
├── notebooks/
│   └── Causal_Inference_LLMs_Complete.ipynb  # Main analysis (all examples)
├── cache/                                    # Generated completions (not in git)
│   ├── gpt2_completions_real.pkl             # GPT-2 completions
│   ├── gptj_completions_real.pkl             # GPT-J completions
│   └── gpt35_completions_real.pkl            # GPT-3.5 completions
├── Example1_Dataset/
│   └── instruction_format_data.csv           # LLM prompt format data
├── Example2_Dataset/
│   ├── nswre74_treated.txt                   # LaLonde treated group (n=185)
│   └── nswre74_control.txt                   # LaLonde control group (n=260)
├── scripts/
│   └── generate_dataset.py                   # Dataset generation utility
├── QuizQuestions.md                          # 15 quiz questions
├── Video_Link.txt                            # Video presentation link
├── requirements.txt                          # Dependencies
├── README.md                                 # This file
└── LICENSE                                   # MIT License
```

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure API keys
cp .env.example .env
# Edit .env and add your API keys

# 3. Start Jupyter
jupyter notebook

# 4. Open and run the notebook
# notebooks/Causal_Inference_LLMs_Complete.ipynb
```
Note: All required dependencies are in requirements.txt

## Installation

### 1. Clone repository

```bash
git clone <repository-url>
cd Individual_Nilay_Causal_Inference_LLMs
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up API keys (optional but recommended)

For best results with GPT-J and GPT-3.5:

```bash
# Copy the example file
cp .env.example .env

# Edit .env file and add your actual API keys
# Get Hugging Face token from: https://huggingface.co/settings/tokens
# Get OpenAI API key from: https://platform.openai.com/api-keys

# Your .env file should look like:
# HF_TOKEN=hf_your_actual_token_here
# OPENAI_API_KEY=sk-your_actual_key_here
```

**Important**: 
- Never commit your `.env` file to git (it's already in `.gitignore`)
- The `.env.example` file is a template - copy it to `.env` and add your real keys
- Restart Jupyter kernel after creating/updating `.env` file

**Alternative** (without .env file):
```bash
# Set as system environment variables
export HF_TOKEN='hf_xxxxx'
export OPENAI_API_KEY='sk-xxxxx'
```

### 5. Launch Jupyter

```bash
jupyter notebook
```

Navigate to `notebooks/Causal_Inference_LLMs_Complete.ipynb`

## Notebook Contents

### Part 1: Theory (Sections 1.1-1.6)
- Causality fundamentals (correlation vs causation, potential outcomes)
- Causal graphs (DAGs) with practical examples
- Propensity score matching methodology
- Confounding and selection bias
- Randomized controlled trials vs observational studies

### Part 2: Setup and DAG Visualization (Sections 2.1-2.2)
- Library imports including DoWhy and CausalML
- DAG visualizations for confounding and mediation

### Part 3: Example 1 - Propensity Score Matching (Sections 3.1-3.14)
**Research Question**: Does few-shot prompting causally improve task completion?

**Methods**:
- Generate Format A (zero-shot) vs Format C (few-shot) instructions
- Multi-model completion (GPT-2, GPT-J, GPT-3.5)
- Evaluate with perplexity, length, coherence metrics
- Propensity score estimation and nearest-neighbor matching
- Balance checking (SMD < 0.1)
- ATE estimation with bootstrap CI
- **DoWhy validation** (refutation tests)
- **CausalML** (heterogeneous effects)
- **Sensitivity analysis** (calipers, subgroups, IPW)
- **Model comparison** (scale-dependent effects)

**Key Findings**:
- GPT-2: Null effect (ATE approximately 0) - model too small
- GPT-J: Moderate effect (ATE approximately 0.08-0.12)
- GPT-3.5: Strong effect (ATE approximately 0.12-0.16)
- **Conclusion**: Few-shot learning is an emergent property

### Part 4: Example 2 - Job Training Evaluation (LaLonde Dataset) (Sections 4.1-4.9)
**Research Question**: Does job training causally increase earnings?

**Methods**:
- LaLonde NSW experimental data (RCT with 185 treated, 260 control)
- RCT analysis establishing gold standard benchmark
- Propensity score matching implementation
- DoWhy causal framework validation
- Sensitivity analysis (different calipers, IPW, OLS)
- Comprehensive visualizations (Love plots, propensity distributions)

**Key Findings**:
- RCT estimate: Job training increases earnings by ~$1,794
- PSM successfully recovers RCT effect (validates methodology)
- Results robust across multiple specifications
- Demonstrates why RCTs are the gold standard

**Why This Dataset**:
- Most cited causal inference dataset (10,000+ citations)
- LaLonde (1986), Dehejia & Wahba (1999)
- Allows validation of observational methods against experimental benchmark

### Part 5: Conclusion and References (Sections 5.1-5.2)
- Summary of findings
- Methodological contributions
- Literature references

## Key Features

### Multi-Model Architecture
- **Local model** (GPT-2): Fast, free, baseline
- **HF API** (GPT-J): Free, 50x larger, emergent few-shot
- **OpenAI API** (GPT-3.5): Best performance, low cost ($1-2)
- **Automatic caching**: Completions saved, regenerate only when needed

### Comprehensive Validation
- **DoWhy**: Formal causal graphs, multiple estimators, refutation tests
- **CausalML**: Heterogeneous effects, uplift modeling, meta-learners
- **Sensitivity Analysis**: Calipers, subgroups, alternative methods
- **Bootstrap**: 1000-iteration confidence intervals

### Production-Quality Code
- Clear documentation and cell organization
- Error handling and retry logic for APIs
- Progress bars (tqdm) for long operations
- Automatic cache management
- Flexible configuration (enable/disable models)

## Expected Results

| Model | Parameters | ATE (Few-Shot) | Significant? | Time | Cost |
|-------|-----------|---------------|--------------|------|------|
| GPT-2 | 124M | approximately 0.00 | No | 15 min | $0 |
| GPT-J | 6B | approximately 0.10 | Yes | 45 min | $0 |
| GPT-3.5 | 175B+ | approximately 0.14 | Yes | 15 min | $2 |

## Running the Analysis

### Option 1: Quick Run (GPT-2 only)
```python
USE_GPT2 = True
USE_GPTJ = False
USE_GPT35 = False
```
- Time: approximately 20 minutes
- Cost: $0
- Result: Null findings (pedagogical)

### Option 2: Recommended (GPT-J)
```python
USE_GPT2 = True
USE_GPTJ = True
USE_GPT35 = False
```
- Time: approximately 60 minutes
- Cost: $0
- Result: Significant findings

### Option 3: Full Analysis (All models)
```python
USE_GPT2 = True
USE_GPTJ = True
USE_GPT35 = True
```
- Time: approximately 60 minutes (parallel caching)
- Cost: approximately $2
- Result: Complete scale comparison

## Dependencies

Core libraries:
- `numpy`, `pandas`, `matplotlib`, `seaborn` - Data and visualization
- `scikit-learn` - Propensity scores, preprocessing
- `statsmodels` - Mediation analysis (OLS)
- `networkx` - DAG visualization
- `transformers`, `torch` - GPT-2 local generation

Causal libraries:
- `dowhy` - Causal inference framework
- `causalml` - Heterogeneous treatment effects

API libraries (optional):
- `openai` - GPT-3.5 API
- `huggingface_hub` - GPT-J API

## Video Presentation

Link: See `Video_Link.txt`

## Quiz Questions

15 multiple-choice questions covering:
- Causal inference fundamentals
- Propensity score matching
- DAGs and confounding
- RCTs vs observational studies
- LaLonde dataset and experimental validation

See `QuizQuestions.md`

## References

- Brown et al. (2020): Language Models are Few-Shot Learners
- Pearl (2009): Causality: Models, Reasoning, and Inference
- Rosenbaum and Rubin (1983): The Central Role of the Propensity Score
- Baron and Kenny (1986): The Moderator-Mediator Variable Distinction
- Sharma and Kiciman (2020): DoWhy: A Python Library for Causal Inference

## License

MIT License - See `LICENSE` file

## Author

Nilay - INFO 7390 Crash Course in Causality (Spring 2026)

---

**Note**: This project demonstrates causal inference methods for educational purposes. Real-world applications should consider additional confounders, larger samples, and domain-specific validation.