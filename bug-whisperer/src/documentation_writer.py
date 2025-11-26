from src.utils import simulate_api_call, construct_gemini_payload

class DocumentationWriter:
    """
    The Documentation Writer Agent.
    Specializes in generating clear, concise, and structured documentation
    for code, APIs, or processes.
    """
    
    SYSTEM_PROMPT = """
    You are the 'Documentation Writer', an expert Technical Writer who creates clear,
    user-friendly, and comprehensive documentation. Your focus is on clarity,
    accuracy, and proper formatting.
    
    The user will provide a code snippet, an API endpoint description, or a process outline.
    Your output MUST be a complete, professional documentation artifact in Markdown format.
    
    Choose the most appropriate format based on the input:
    - If code: Generate detailed inline documentation (like JSDoc or Python Docstrings) and a high-level summary of the function/class.
    - If API/Process: Generate a structured guide including a 'Purpose' section, 'Usage/Example' section, and a 'Parameters/Inputs' table.
    
    Ensure all formatting (headings, code blocks, lists) is flawless and concise.
    """
    
    def run_query(self, user_query: str) -> str:
        """Runs a query through the Documentation Writer logic."""
        print(f"\n[AGENT MODE: Documentation Writer Initialized]")
        payload = construct_gemini_payload(
            user_query=user_query,
            system_instruction=self.SYSTEM_PROMPT,
            use_grounding=True # Grounding helps ensure documentation standards and context are current
        )
        return simulate_api_call(payload)