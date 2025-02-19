# AI Model Discussion System

This project implements a sophisticated system that facilitates discussion and comparison between three major AI models: OpenAI's GPT, Anthropic's Claude, and Google's Gemini. The system offers two distinct approaches to model evaluation and response refinement.

## Features

- Simultaneous querying of multiple AI models
- Two distinct evaluation methodologies
- Blind evaluation through randomized response labeling
- Inter-model discussion and analysis
- Refinement of chosen responses
- Asynchronous operation for improved performance

## Prerequisites

- Python 3.8 or higher
- API keys for:
  - OpenAI
  - Anthropic
  - Google (Gemini)

## Installation

1. Clone the repository and navigate to project directory
2. Create and activate a virtual environment 
3. Install required packages:
   - openai
   - anthropic 
   - google-generativeai
   - python-dotenv
4. Create a `.env` file in the project root with your API keys:
   - SELF_RAG_OPENAI_API_KEY
   - NEZ_CLAUDE_API_KEY  
   - GEMINI_API

## Evaluation Approaches

The system implements two distinct methods for evaluating and selecting the best response:

### 1. Plain Model Ranking
- Models evaluate responses blindly (labeled as R1, R2, R3)
- Discussion-based selection process
- Qualitative evaluation of responses
- Focus on reasoning and improvement suggestions
- Simple majority-based selection
- Outputs:
  - Chosen response
  - Improvement suggestions
  - Final refined response

### 2. Merit Score Ranking
- Comprehensive scoring system across multiple criteria
- Weighted evaluation metrics:
  - Factual Accuracy (35%)
  - Explanation Quality (25%)
  - Practical Examples (20%)
  - Technical Depth (20%)
  - Additional considerations for Clarity and Completeness
- Numerical scoring (0-100) for each category
- Confidence levels based on score differences:
  - Very High: >15 points difference
  - High: 10-15 points difference
  - Medium: 5-10 points difference
  - Low: <5 points difference
- Statistical analysis of scores including outlier removal
- Detailed performance metrics

## Process Flow

### Initial Phase (Common to Both Approaches)
1. User provides a prompt
2. System queries all three models simultaneously
3. Responses are collected asynchronously
4. Random labeling (R1, R2, R3) ensures unbiased evaluation

### Evaluation Phase

#### Plain Model Ranking:
1. Models discuss and evaluate responses
2. Each model provides reasoning for their choice
3. System identifies the most preferred response
4. Collects improvement suggestions
5. Final response incorporates refinements

#### Merit Score Ranking:
1. Detailed scoring across all categories
2. Statistical analysis of scores
3. Weighted calculation of final scores
4. Confidence level determination
5. Comprehensive feedback collection
6. Refined response with specific improvements

## Output Format

Both approaches return structured results including:
- Initial responses from all models
- Evaluation results (discussion-based or scored)
- Selected response details
- Refinement suggestions
- Final refined response

## Key Components

### ModelDiscussionSystem
- Manages model interactions
- Handles response collection
- Facilitates evaluation process
- Processes refinements

### Evaluation System
- Plain Ranking: Discussion-based evaluation
- Merit Scoring: Comprehensive numerical evaluation
- Both systems maintain blind evaluation principles

### Asynchronous Operation
- Concurrent model queries
- Efficient API communication
- Improved response times

## Customization

- Adjustable scoring weights (Merit System)
- Modifiable evaluation criteria
- Customizable confidence thresholds
- Flexible prompt formats

## Error Handling

Robust error handling for:
- API communication issues
- Response parsing
- Score calculation (Merit System)
- Discussion analysis (Plain System)
- Refinement extraction

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Acknowledgments

- OpenAI for GPT API
- Anthropic for Claude API
- Google for Gemini API