import sys

# Mock Configuration
SEARCH_PATHS = {"z": "/mnt/zdrive", "Y": "/mnt/ydrive"}

# --- The Buggy Initialization ---
# The code loads SEARCH_TARGETS verbatim from SEARCH_PATHS
# FIX: Normalize keys to uppercase to match search/view logic
SEARCH_TARGETS = {k.upper(): v for k, v in SEARCH_PATHS.items()}

print(f"DEBUG: SEARCH_TARGETS keys: {list(SEARCH_TARGETS.keys())}")

errors = []

# --- Scenario 1: Search Filter ---
# User provides "z", code uppercases it to "Z".
user_input = "z"
processed_drive = user_input.upper() # "Z"

# Filter check
if processed_drive not in SEARCH_TARGETS:
    errors.append(f"Search Filter: Processed drive '{processed_drive}' not found in SEARCH_TARGETS {list(SEARCH_TARGETS.keys())}")

# --- Scenario 2: View Endpoint ---
# User requests "z:\file.txt", code extracts "z" and uppercases to "Z".
file_path = "z:\\note.txt"
drive_key = file_path[0].upper() # "Z"

if drive_key not in SEARCH_TARGETS:
    errors.append(f"View Endpoint: Drive key '{drive_key}' not found in SEARCH_TARGETS")

if errors:
    print("Bug Reproduced:")
    for e in errors:
        print(f" - {e}")
    sys.exit(1) # Exit with error to signal failure
else:
    print("Bug NOT Reproduced. All checks passed.")
    sys.exit(0)
