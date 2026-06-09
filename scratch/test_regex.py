import re

text_nested = '"[a] Public dashboard: ... the headline ratio of f"{us_eu_caci:.2f}:1" between USA and EU (aggregated) is computed on the live dataset as of April 2026.",'
text_toplevel = 'f"{us_share:.1f}% global operational AI compute = USA",'

# Regex that requires a preceding double quote
nested_pattern = r'("([^"\\]|\\.)*)f"\{([^}]+)\}([^"]*)"'

print("Nested matches:", re.findall(nested_pattern, text_nested))
print("Toplevel matches:", re.findall(nested_pattern, text_toplevel))

# Test substitution on nested
res = re.sub(nested_pattern, r'\1{\3}\4', text_nested)
# Then prepend 'f' if not present
if res.startswith('"') or res.startswith('    "'):
    res = 'f' + res
print("Nested result:", res)
