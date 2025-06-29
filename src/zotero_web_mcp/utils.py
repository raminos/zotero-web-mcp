from typing import List, Dict

def format_creators(creators: List[Dict[str, str]]) -> str:
    """
    Format creator names into a string.
    
    Args:
        creators: List of creator objects from Zotero.
        
    Returns:
        Formatted string with creator names.
    """
    names = []
    for creator in creators:
        if "firstName" in creator and "lastName" in creator:
            names.append(f"{creator['lastName']}, {creator['firstName']}")
        elif "name" in creator:
            names.append(creator["name"])
    return "; ".join(names) if names else "No authors listed"
