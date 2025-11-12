import random

# --- Configuration: Define possible "drifts" ---

# A simple set of drifts that mimic common errors.
# We'll map what an authority *was* to what it *can become*.
DRIFT_MUTATIONS = {
    "permitAll": ["authenticated"],
    "authenticated": ["permitAll", "ROLE_USER"],
    "ROLE_USER": ["ROLE_ADMIN", "authenticated"],
    "ROLE_ADMIN": ["ROLE_USER", "authenticated"]
}

# A list of common multi-role authorities and how they can drift
# (e.g., a rule that should be for ADMIN *and* USER is reduced to just USER)
MULTI_ROLE_DRIFT = {
    "ROLE_ADMIN,ROLE_USER": [["ROLE_ADMIN"], ["ROLE_USER"]]
}

def get_new_authorities(original_auths):
    """
    Applies a random mutation to a list of authorities.
    This is the core "drift" logic.
    """
    if not original_auths:
        return ["authenticated"]  # Default for empty list

    # Create a simple key for multi-role lookups
    original_key = ",".join(sorted(original_auths))

    # Check for multi-role drift first
    if original_key in MULTI_ROLE_DRIFT:
        new_auths = random.choice(MULTI_ROLE_DRIFT[original_key])
        print(f"    - Mutation: Multi-role drift '{original_key}' -> {new_auths}")
        return new_auths

    # Check for single-role drift
    if len(original_auths) == 1 and original_auths[0] in DRIFT_MUTATIONS:
        new_auths = [random.choice(DRIFT_MUTATIONS[original_auths[0]])]
        print(f"    - Mutation: Single-role drift '{original_auths[0]}' -> {new_auths[0]}")
        return new_auths

    # Default fallback: If no specific drift is defined,
    # swap it to a simple 'authenticated' or 'ROLE_USER'.
    fallback_auth = random.choice([["authenticated"], ["ROLE_USER"]])
    print(f"    - Mutation: Fallback drift {original_auths} -> {fallback_auth}")
    return fallback_auth