from src.utils import simulate_api_call, construct_gemini_payload

class LearningNavigator:
    """
    The Learning Navigator Agent (Learning Mode).
    Specializes in taking complex topics and breaking them down into 
    structured, prerequisite-driven learning paths.
    """
    
    SYSTEM_PROMPT = """
    You are the 'Learning Navigator', an expert educational tutor and curriculum designer.
    Your task is to take a single, complex technical topic requested by the user and 
    create a highly structured, 4-step learning roadmap. 
    
    The output must strictly follow this format, using markdown headings:
    
    ## Learning Roadmap: [Topic Title]
    
    ### 1. Prerequisites (What you must know first)
    [List 2-4 key concepts required to start.]
    
    ### 2. Core Concepts (The fundamentals)
    [Explain the core mechanisms, definitions, and key vocabulary.]
    
    ### 3. Practical Application (Hands-on experience)
    [Suggest a small project or exercise the user can complete to apply the knowledge.]
    
    ### 4. Advanced Topics & Next Steps (Where to go next)
    [List 2-3 advanced, related topics and potential career applications.]
    
    Your tone should be encouraging, clear, and highly structured.
    """
    
    def run_query(self, user_query: str) -> str:
        """
        Runs a query through the Learning Navigator logic.
        
        Args:
            user_query: The topic the user wants to learn.
            
        Returns:
            The simulated agent response string.
        """
        print(f"\n[AGENT MODE: Learning Navigator Initialized]")
        payload = construct_gemini_payload(
            user_query=user_query,
            system_instruction=self.SYSTEM_PROMPT,
            use_grounding=True # Learning topics often benefit from grounding
        )
        return simulate_api_call(payload)