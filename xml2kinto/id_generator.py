import hashlib
import json
import uuid
from copy import deepcopy
from six import text_type


def create_id(data):
    """Compute a reproducible ID for deeply nested data structures.

    This will be used to make sure that two deeply nested data structures are
    exactly equal.
    """
    # We should ignore the enabled key.
    data = deepcopy(data)
    if 'enabled' in data:
        del data['enabled']
    serialized = json.dumps(data, sort_keys=True, separators=(',', ':'))
    hashed = hashlib.md5(serialized.encode('utf-8'))
    return text_type(uuid.UUID(hashed.hexdigest()))
