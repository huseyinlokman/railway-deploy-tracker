# validators.py
import re
from typing import List

def validate_payload(payload: dict) -> bool:
    # Accept if payload has either minimal keys or Railway webhook keys
    if not isinstance(payload, dict):
        return False

    # Check minimal structure
    if "project" in payload and isinstance(payload["project"], dict) and "name" in payload["project"]:
        if "status" in payload:
            return True

    # Check Railway webhook-like structure
    if "severity" in payload and "message" in payload:
        return True

    return False


def check_syntax_errors(payload: dict) -> List[str]:
    issues = []
    message = payload.get("message", "")
    syntax_patterns = [
        r"SyntaxError",
        r"invalid syntax",
        r"missing comma",
        r"unexpected EOF",
    ]
    for pattern in syntax_patterns:
        if re.search(pattern, message, re.IGNORECASE):
            issues.append(f"Syntax error detected in message: {message}")
            break
    return issues


def check_build_failures(payload: dict) -> List[str]:
    issues = []
    message = payload.get("message", "") or ""
    build_fail_patterns = [
        r"failed to build",
        r"build failed",
        r"error:",
        r"exception",
        r"traceback",
    ]
    for pattern in build_fail_patterns:
        if re.search(pattern, message, re.IGNORECASE):
            issues.append(f"Build failure or error detected: {message}")
            break
    return issues


def run_all_validators(payload: dict) -> List[str]:
    issues = []
    issues.extend(check_syntax_errors(payload))
    issues.extend(check_build_failures(payload))
    # add more validators here if needed
    return issues