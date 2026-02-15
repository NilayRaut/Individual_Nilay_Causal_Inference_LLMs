# Comprehensive Causal Inference: From LLM Prompting to Policy Evaluation

**Author:** NILAY RAUT  
**Email:** raut.ni@northeastern.edu  
**Course:** INFO 7390 - Advances in Data Science and Architecture  
**Institution:** Northeastern University  
**Semester:** Spring 2026

**Links:**
- GitHub Repository: [https://github.com/NilayRaut/Individual_Nilay_Causal_Inference_LLMs](https://github.com/NilayRaut/Individual_Nilay_Causal_Inference_LLMs)
- Video Presentation: [YouTube Link](https://youtu.be/Kawh2ElTSMc)

---

## Project Overview

This project demonstrates:
- **Comprehensive causal inference**: Propensity Score Matching (PSM) methodology with rigorous validation
- **Two complete examples**:
  - Example 1: Few-shot vs direct prompting effects in LLMs (null result demonstrates methodology)
  - Example 2: Job training program evaluation using LaLonde dataset (validates PSM against RCT)
- **Multi-method validation**: DoWhy and CausalML frameworks for robustness
- **Experimental benchmark**: RCT gold standard for validating observational methods
- **Sensitivity analysis**: Multiple specifications, calipers, and balance diagnostics

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
│   ├── gptneo_completions_real.pkl           # GPT-Neo completions
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

For best results with GPT-Neo and GPT-3.5:

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

### Part 3: Example 1 - LLM Prompt Engineering Analysis (Sections 3.1-3.9)
**Research Question**: Does few-shot prompting causally improve task completion quality?

**Treatment**: Format C (few-shot with examples) vs Format A (direct zero-shot instructions)

**Methods**:
- Generate both instruction formats for 50 tasks with confounded assignment
- Multi-model completion (GPT-2, GPT-Neo, GPT-3.5)
- Quality evaluation: perplexity, length appropriateness, coherence metrics
- Propensity score estimation and nearest-neighbor matching with caliper=0.1
- Balance checking with Standardized Mean Differences (SMD)
- ATE estimation with 1000-iteration bootstrap confidence intervals
- **DoWhy validation** with refutation tests
- **Sensitivity analysis** across multiple specifications

**Key Findings**:
- **Primary result**: ATE = -0.041, 95% CI [-0.098, 0.017]
- **Interpretation**: No statistically significant causal effect detected (null result)
- Task difficulty was the primary confounder (successfully controlled)
- Balance improved: 74% to 81% confounding reduction with tighter caliper
- **Conclusion**: Demonstrates PSM methodology even when treatment effect is null

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

### Multi-Framework Validation
- **Manual PSM implementation**: Complete from scratch for educational transparency
- **DoWhy framework**: Microsoft's causal inference library with refutation tests
- **CausalML**: Uber's library for heterogeneous treatment effects
- **Multiple estimation methods**: PSM, IPW, OLS regression for robustness
- **Automatic caching**: Completions saved to avoid redundant API calls

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

## Key Results Summary

### Example 1: LLM Prompt Engineering
| Metric | Value | Interpretation |
|--------|-------|----------------|
| ATE | -0.041 | Near-zero effect |
| 95% CI | [-0.098, 0.017] | Includes zero (not significant) |
| Matched Pairs | 31 | With caliper=0.1 |
| Balance | 3/6 covariates SMD < 0.1 | Improved from 0/6 before matching |
| Confounding Reduction | 81.1% | From 0.681 to 0.129 difference |

### Example 2: Job Training Evaluation
| Metric | Value | Interpretation |
|--------|-------|----------------|
| RCT Benchmark | $1,794 | Gold standard experimental result |
| PSM Estimate | $1,730 | Within $64 (3.6%) of RCT |
| Balance | All SMD < 0.1 | Excellent covariate balance |
| Validation | Converges across methods | DoWhy, IPW, OLS all agree |

## Running the Analysis

### Recommended Approach

1. **Start with cached results**: The notebook includes pre-generated completions to run immediately
2. **Examine methodology**: Focus on PSM implementation, balance checking, and validation
3. **Explore both examples**: Example 1 demonstrates methodology; Example 2 validates against RCT

### Configuration Options

Control which models to use in the notebook:
```python
USE_GPT2 = True      # Local model, always available
USE_GPTNEO = True    # HuggingFace API (requires HF_TOKEN)
USE_GPT35 = True     # OpenAI API (requires OPENAI_API_KEY)
```

**Note**: All examples use GPT-2 completions by default. Multi-model comparison is available but optional for understanding the core causal methodology.

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
- `huggingface_hub` - GPT-Neo API

## Video Presentation

A 3-5 minute presentation explaining the notebook structure, key findings, and causal reasoning.

Link: See `Video_Link.txt` or [YouTube - To be added](https://youtube.com/placeholder)

## Quiz Questions

15 multiple-choice questions covering:
- Causal inference fundamentals
- Propensity score matching
- DAGs and confounding
- RCTs vs observational studies
- LaLonde dataset and experimental validation

See `QuizQuestions.md`

## Key References

**Foundational Papers:**
- Rubin (1974): Estimating Causal Effects (Potential Outcomes Framework)
- Rosenbaum & Rubin (1983): The Central Role of the Propensity Score
- Pearl (2009): Causality: Models, Reasoning, and Inference
- LaLonde (1986): Evaluating Training Programs with Experimental Data
- Dehejia & Wahba (1999): Causal Effects in Nonexperimental Studies

**Software & Implementation:**
- Sharma & Kiciman (2020): DoWhy - End-to-End Library for Causal Inference
- Chen et al. (2020): CausalML - Python Package for Causal Machine Learning
- Imbens & Rubin (2015): Causal Inference for Statistics, Social, and Biomedical Sciences

**Recent Advances (2023-2025):**
- Chernozhukov et al. (2024): Flexible ML Methods for Causal Inference
- Künzel & Sekhon (2024): Causal Forests - Recent Developments
- Shi et al. (2023): Adapting Neural Networks for Causal Inference

See notebook for complete bibliography with 24+ references.

## License

MIT License - See `LICENSE` file

## Contact

**NILAY RAUT**  
Email: raut.ni@northeastern.edu  
Course: INFO 7390 - Advances in Data Science and Architecture  
Institution: Northeastern University

---

**Note**: This project demonstrates causal inference methods for educational purposes. Real-world applications should consider additional confounders, larger samples, and domain-specific validation.