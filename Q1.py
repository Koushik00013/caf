import re

def normalize_company_name(name: str | None) -> str | None:
    """
    Normalizes CAF SoftSol company name variants into:
    'CAF SoftSol India Pvt Ltd.'
    """

    if not name or not name.strip():
        return None  # graceful handling for empty / missing entries

    # Normalize spaces and lowercase
    cleaned = re.sub(r"\s+", " ", name).strip().lower()

    # Check for CAF and softsol/solution patterns
    if "caf" in cleaned and (
        "softsol" in cleaned
        or "soft solution" in cleaned
        or "softsolution" in cleaned
        or "solution" in cleaned
    ):
        return "CAF SoftSol India Pvt Ltd."

    # Fallback: title-case cleaned input
    return cleaned.title()
