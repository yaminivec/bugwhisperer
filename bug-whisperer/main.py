import sys
from src.bug_whisperer import QAAgent
from src.learning_navigator import LearningNavigator
from src.refactoring_guru import RefactoringGuru
from src.documentation_writer import DocumentationWriter

def run_cli():
    """
    Command-Line Interface entry point for demonstrating the agents.
    """
    print("--- Bug Whisperer AI Agent CLI Demo ---")
    
    while True:
        mode = input(
            "Select Agent Mode (1: QA Engineer, 2: Learning Navigator, 3: Refactoring Guru, 4: Documentation Writer, q: Quit): "
        ).strip().lower()
        
        if mode == 'q':
            print("Exiting Bug Whisperer. Goodbye!")
            sys.exit(0)
        
        user_query = input("Enter your query: ").strip()
        
        if not user_query:
            print("Query cannot be empty. Please try again.")
            continue
            
        agent = None
        if mode == '1':
            agent = QAAgent()
        elif mode == '2':
            agent = LearningNavigator()
        elif mode == '3':
            agent = RefactoringGuru()
        elif mode == '4':
            agent = DocumentationWriter()
        else:
            print("Invalid mode selection. Please enter '1', '2', '3', '4', or 'q'.")
            continue
            
        # The actual API call is simulated here, but would be performed 
        # by the dedicated frontend for real interaction.
        response = agent.run_query(user_query)
        print("\n--- AGENT RESPONSE ---")
        print(response)
        print("----------------------\n")

if __name__ == "__main__":
    run_cli()