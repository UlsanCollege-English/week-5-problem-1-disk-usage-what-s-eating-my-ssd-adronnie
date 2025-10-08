# src/disk_usage.py

def total_size(node):
    """
    Compute total size of a nested file/dir tree.
    node format:
      - file: {"type": "file", "name": str, "size": int}
      - dir:  {"type": "dir", "name": str, "children": [nodes]}
    """
    # Handle None or invalid node
    if not node or not isinstance(node, dict):
        return 0

    node_type = node.get("type")

    # Base case: file
    if node_type == "file":
        return node.get("size", 0) or 0

    # Recursive case: directory
    if node_type == "dir":
        children = node.get("children", [])
        return sum(total_size(child) for child in children)

    # Unknown type — ignore
    return 0
