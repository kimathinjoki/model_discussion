# AI Model Discussion System

This project implements a system that facilitates discussion and comparison between three major AI models: OpenAI's GPT, Anthropic's Claude, and Google's Gemini. The system allows models to evaluate each other's responses and collaboratively improve the final output.

## Features

- Simultaneous querying of multiple AI models
- Blind evaluation system through randomized response labeling
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

## How It Works

### 1. Initial Response Collection
- The system takes a user prompt and sends it to all three AI models
- Responses are collected asynchronously
- Each response is randomly assigned a label (R1, R2, R3) to ensure unbiased evaluation

### 2. Discussion Phase
- Models are presented with all responses (labeled R1, R2, R3)
- Each model evaluates the responses and provides:
  - A preferred response selection
  - Reasoning for their choice
  - Suggested improvements

### 3. Analysis
- The system analyzes the discussion to determine:
  - Most preferred response
  - Consolidated improvement suggestions

### 4. Final Response
- The chosen model provides a refined response
- Incorporates suggested improvements
- Delivers final output to user

## Usage

The system can be used either as a Python script or in a Jupyter notebook. The system will return a dictionary containing:
- Initial responses from each model
- The chosen response label
- Refinement suggestions
- The final refined response

## Key Components

### ModelDiscussionSystem
The main class that orchestrates the entire process:
- Manages model interactions
- Handles response collection
- Facilitates discussions
- Processes refinements

### Blind Evaluation System
- Responses are randomly labeled (R1, R2, R3)
- Models evaluate responses without knowing their source
- Prevents potential biases in the evaluation process

### Asynchronous Operation
- Utilizes Python's asyncio for concurrent operations
- Improves performance by running model queries in parallel
- Handles API communications efficiently

## Customization

### Modifying Model Selection
You can modify the model_map in the ModelDiscussionSystem class to use different models, with labels R1, R2, R3 mapping to your chosen models.

### Adjusting Response Format
The discussion prompt format can be customized in the _create_discussion_prompt method.

## Error Handling

The system includes robust error handling for:
- API communication issues
- Response parsing
- Discussion analysis
- Refinement extraction

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Acknowledgments

- OpenAI for GPT API
- Anthropic for Claude API
- Google for Gemini API