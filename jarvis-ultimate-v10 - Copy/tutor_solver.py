\class TutorSolver:
    def __init__(self, llm_brain):
        self.brain = llm_brain
        
    def solve_math(self, problem_description):
        """Forces the LLM to use step-by-step logic for math problems."""
        prompt = (
            f"Act as an expert math tutor. Solve the following problem step-by-step. "
            f"Show all calculations clearly before providing the final answer:\n\n{problem_description}"
        )
        return self.brain.process_prompt(prompt)
        
    def explain_code(self, code_snippet):
        """Breaks down programming logic."""
        prompt = (
            f"Act as a senior software engineer. Explain what this code does in simple terms. "
            f"Identify any obvious bugs:\n\n{code_snippet}"
        )
        return self.brain.process_prompt(prompt)