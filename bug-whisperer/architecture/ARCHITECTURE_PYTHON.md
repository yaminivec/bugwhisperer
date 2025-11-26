Architecture Document: Bug Whisperer AI Agents

1. High-Level Overview

The Bug Whisperer project follows a Modular Agent Design. The core principle is the separation of concerns, ensuring that the utility logic (API handling, common configuration) is separate from the domain logic (the specific agent personas and system prompts).

2. Component Breakdown

A. src/utils.py

This module is designed for shared functionality.

System Prompt Generation: Provides a base function to construct the final system instruction based on the agent's role and user context.

API Configuration: Holds standard parameters for the Gemini API call (model, temperature, etc.).

Error Handling: Implements exponential backoff and retry logic for API calls (represented conceptually, as the actual API calls are made in the JavaScript frontend).

B. src/bug_whisperer.py (QA Engineer)

Persona: Defines the QAAgent class.

System Instruction: Contains a specialized, detailed system prompt that establishes the agent as an experienced QA professional focused on defensive coding, edge cases, and test strategy.

C. src/learning_navigator.py (Learning Navigator)

Persona: Defines the LearningNavigator class.

System Instruction: Contains a system prompt that guides the model to act as a structured curriculum planner, demanding output in a specific, step-by-step format suitable for educational purposes.

D. main.py (Entry Point)

Provides the mechanism to instantiate the different agents and run a demonstration of their capabilities. It acts as the orchestrator, taking user input and directing it to the selected agent logic.

3. Data Flow (Conceptual)

User Input: The user provides a query and selects an agent mode (QA or Learning) via the CLI or HTML frontend.

Agent Selection: main.py (or the frontend JS) selects the appropriate agent class (QAAgent or LearningNavigator).

Prompt Construction: The agent uses its specialized system prompt.

API Call: The system prompt and user query are sent to the gemini-2.5-flash-preview-09-2025 model.

Response: The model returns the generated text and grounding metadata (citations).

Output: The result is displayed to the user.