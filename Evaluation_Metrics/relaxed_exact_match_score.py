def calculate_rems(generated_result, gold_result):
    generated_parts = [part.strip() for part in str(generated_result).split(",")]
    gold_parts = [part.strip() for part in str(gold_result).split(",")]
    
    matching_components = [
        gold_part for gold_part in gold_parts
        if any(
            gold_part == gen_part or f" {gold_part} " in f" {gen_part} "
            for gen_part in generated_parts
        )
    ]
    
    if len(gold_parts) == 0:
        return 0.0
    
    rems_score = len(matching_components) / len(gold_parts)
    rems_score = round(rems_score, 2)
    return rems_score