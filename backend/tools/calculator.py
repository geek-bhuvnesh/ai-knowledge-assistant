def calculate(expression: str) -> str:
    try:
        result = eval(expression) 
        return str(result)
    except Exception as e: # type: ignore
        return "Error in calculation"