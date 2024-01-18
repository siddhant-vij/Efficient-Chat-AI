def calculate_token_cost(input_tokens: int, output_tokens: int) -> float:
    cost_per_input_token = 0.01 / 1000
    cost_per_output_token = 0.03 / 1000
    total_cost = (input_tokens * cost_per_input_token) + \
        (output_tokens * cost_per_output_token)
    return total_cost
