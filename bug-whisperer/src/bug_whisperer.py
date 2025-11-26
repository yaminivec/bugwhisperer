from src.utils import simulate_api_call, construct_gemini_payload

class QAAgent:
    """
    The Bug Whisperer Agent (QA Engineer Mode).
    Specializes in code review, bug identification, test case generation, 
    and quality assurance strategy.
    """
    
    SYSTEM_PROMPT = """
    You are the 'Bug Whisperer', a world-class Senior QA Engineer and software architect.
    Your primary goal is to analyze code snippets or technical scenarios provided by the user. 
    You must provide structured feedback in the following three parts:
    
    1.  **Vulnerability & Bug Analysis:** Identify any potential runtime errors, security vulnerabilities (e.g., injection, XSS), or logic bugs. Explain *why* it's a bug.
    2.  **Suggested Fixes & Improvements:** Provide the clean, fixed code or a clear description of the architectural change needed to resolve the issues and improve defensive programming.
    3.  **Comprehensive Test Cases:** Generate a set of comprehensive, high-priority test cases (inputs and expected outputs) to validate the fix and cover edge cases (e.g., zero, null, maximum limits, concurrency).
    
    Maintain a professional, analytical, and highly detailed tone. Your response must be actionable.
    """
    
    def run_query(self, user_query: str) -> str:
        """
        Runs a query through the QA Agent logic.
        
        Args:
            user_query: The code snippet or scenario to analyze.
        
        Returns:
            The simulated agent response string.
        """
        print(f"\n[AGENT MODE: QA Engineer Initialized]")
        payload = construct_gemini_payload(
            user_query=user_query,
            system_instruction=self.SYSTEM_PROMPT,
            use_grounding=False # QA often doesn't need external grounding
        )
        return simulate_api_call(payload)