import os
from typing import List, Dict, Tuple
import random
import asyncio
from openai import AsyncOpenAI
from anthropic import AsyncAnthropic
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Initialize API clients
openai_client = AsyncOpenAI(api_key=os.getenv("SELF_RAG_OPENAI_API_KEY"))
anthropic_client = AsyncAnthropic(api_key=os.getenv("NEZ_CLAUDE_API_KEY"))
genai.configure(api_key=os.getenv("GEMINI_API"))

class ModelDiscussionSystem:
    def __init__(self):
        self.model_map = {
            "R1": "OpenAI",
            "R2": "Claude",
            "R3": "Gemini"
        }
        # Reverse mapping for internal use
        self.reverse_map = {v: k for k, v in self.model_map.items()}
        
    async def get_initial_responses(self, prompt: str) -> Dict[str, str]:
        """Get initial responses from all three models."""
        tasks = [
            self._get_openai_response(prompt),
            self._get_claude_response(prompt),
            self._get_gemini_response(prompt)
        ]
        responses = await asyncio.gather(*tasks)
        
        # Randomly assign response labels
        labels = list(self.reverse_map.values())
        random.shuffle(labels)
        
        return {labels[i]: resp for i, resp in enumerate(responses)}

    async def facilitate_discussion(self, initial_responses: Dict[str, str]) -> Tuple[str, str]:
        """Facilitate discussion between models about the best response."""
        discussion_prompt = self._create_discussion_prompt(initial_responses)
        
        # Get discussion responses from each model
        tasks = [
            self._get_openai_response(discussion_prompt),
            self._get_claude_response(discussion_prompt),
            self._get_gemini_response(discussion_prompt)
        ]
        discussion_responses = await asyncio.gather(*tasks)
        
        # Analyze discussion to determine chosen response and refinements
        chosen_response_label, refinements = self._analyze_discussion(discussion_responses)
        return chosen_response_label, refinements

    async def get_final_response(self, prompt: str, chosen_label: str, refinements: str) -> str:
        """Get final refined response from the chosen model."""
        final_prompt = self._create_final_prompt(prompt, refinements)
        
        # Map the response label back to the actual model
        chosen_model = self.model_map[chosen_label]
        
        if chosen_model == "OpenAI":
            return await self._get_openai_response(final_prompt)
        elif chosen_model == "Claude":
            return await self._get_claude_response(final_prompt)
        else:  # Gemini
            return await self._get_gemini_response(final_prompt)

    async def _get_openai_response(self, prompt: str) -> str:
        """Get response from OpenAI's GPT model."""
        response = await openai_client.chat.completions.create(
            model="chatgpt-4o-latest",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    async def _get_claude_response(self, prompt: str) -> str:
        """Get response from Anthropic's Claude model."""
        response = await anthropic_client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text

    async def _get_gemini_response(self, prompt: str) -> str:
        """Get response from Google's Gemini model."""
        model = genai.GenerativeModel('gemini-2.0-pro-exp-02-05')
        response = await model.generate_content_async(prompt)
        return response.text

    def _create_discussion_prompt(self, responses: Dict[str, str]) -> str:
        """Create prompt for models to discuss the best response."""
        return f"""Analyze these three responses to the same prompt and discuss which one provides the best answer. 
        Don't reveal which model you are, and refer to responses by their labels.

        Responses:
        {responses}

        Based on these responses:
        1. Which response (R1, R2, or R3) do you think provides the best answer and why?
        2. What specific improvements or additions would make the chosen response even better?
        
        Provide your analysis in a clear, structured format."""

    def _create_final_prompt(self, original_prompt: str, refinements: str) -> str:
        """Create prompt for final refined response."""
        return f"""Original prompt: {original_prompt}

        Please provide a refined response incorporating these suggested improvements:
        {refinements}

        Give your best, most comprehensive answer incorporating these refinements."""

    def _analyze_discussion(self, discussion_responses: List[str]) -> Tuple[str, str]:
        """Analyze discussion responses to determine chosen response and refinements."""
        # This is a simplified analysis - you might want to make this more sophisticated
        chosen_labels = []
        all_refinements = []
        
        for response in discussion_responses:
            # Extract chosen label (R1, R2, or R3) from response
            for label in ["R1", "R2", "R3"]:
                if f"chose {label}" in response.lower() or f"prefer {label}" in response.lower():
                    chosen_labels.append(label)
            
            # Extract refinements (text after "improvements" or "refinements")
            if "improvements:" in response.lower():
                refinements = response.lower().split("improvements:")[1].strip()
                all_refinements.append(refinements)
            elif "refinements:" in response.lower():
                refinements = response.lower().split("refinements:")[1].strip()
                all_refinements.append(refinements)

        # Choose the most frequently mentioned label
        chosen_label = max(set(chosen_labels), key=chosen_labels.count)
        
        # Combine unique refinements
        unique_refinements = list(set(all_refinements))
        combined_refinements = "\n".join(unique_refinements)
        
        return chosen_label, combined_refinements

async def main():
    system = ModelDiscussionSystem()
    
    # Example usage
    prompt = "Explain the concept of quantum entanglement"
    
    # Get initial responses
    initial_responses = await system.get_initial_responses(prompt)
    print("Initial Responses:", initial_responses)
    
    # Facilitate discussion
    chosen_label, refinements = await system.facilitate_discussion(initial_responses)
    print(f"\nChosen Response: {chosen_label}")
    print(f"Suggested Refinements: {refinements}")
    
    # Get final response
    final_response = await system.get_final_response(prompt, chosen_label, refinements)
    print(f"\nFinal Response: {final_response}")

if __name__ == "__main__":
    asyncio.run(main())