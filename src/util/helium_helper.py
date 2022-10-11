address_regex = "^[\d\w]{51}"

def hr_hotspot_name(name: str):
    """! Convert dashed hotspot name to a readable name."""
    return name.replace('-', ' ').title()

def reverse_hr_hotspot_name(hr_name: str):
    """! Convert human readable hotspot name to dashed version."""
    return hr_name.lower().replace(' ', '-')