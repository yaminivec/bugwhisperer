Bug Whisperer AI Agent Project

The Bug Whisperer is a multi-mode AI agent designed to assist with both software quality assurance (QA) engineering and technical skill acquisition.

Project Structure

The project is structured around modularity:

main.py: The command-line interface (CLI) entry point for demonstrating the agents.

src/: Contains the core logic for the agents and utilities.

bug_whisperer.py: Implements the QA Engineer agent persona and logic.

learning_navigator.py: Implements the Learning Navigator agent persona and logic.

utils.py: Provides shared utility functions, such as API request templates and exponential backoff logic (though API calls are handled by the separate HTML frontend).

architecture/: Stores documentation, including the architectural overview.

Agent Modes

QA Engineer (Bug Whisperer): Focused on analyzing code snippets, identifying potential bugs, suggesting test cases, and improving overall code quality from a testing perspective.

Learning Navigator: Focused on taking a complex topic (like a new programming concept or algorithm) and breaking it down into a structured, digestible learning path with prerequisites and resources.

Frontend Interaction

This project is paired with a single-file HTML/JavaScript frontend (index.html) that provides a user-friendly interface to select an agent mode and interact with the Gemini API in real-time.
