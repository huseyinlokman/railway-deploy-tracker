def validate_payload(payload):
    if not isinstance(payload, dict):
        return False

    if "project" not in payload or "name" not in payload["project"]:
        return False

    if "status" not in payload:
        return False

    return True
