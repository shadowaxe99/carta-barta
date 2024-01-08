```python
import os
from pathlib import Path

def generate_api_documentation():
    """
    Generates API documentation using the docstrings from controllers and services.
    """
    os.system('pdoc --html --output-dir docs/api backend/controllers backend/services --force')

def generate_user_manual():
    """
    Generates the user manual from a predefined template.
    """
    user_manual_template = Path('docs/templates/user_manual.md')
    user_manual_output = Path('docs/user_manual.md')
    
    if user_manual_template.is_file():
        content = user_manual_template.read_text()
        user_manual_output.write_text(content)
    else:
        raise FileNotFoundError(f"Template {user_manual_template} not found.")

def generate_development_guide():
    """
    Generates the development guide from a predefined template.
    """
    development_guide_template = Path('docs/templates/development_guide.md')
    development_guide_output = Path('docs/development_guide.md')
    
    if development_guide_template.is_file():
        content = development_guide_template.read_text()
        development_guide_output.write_text(content)
    else:
        raise FileNotFoundError(f"Template {development_guide_template} not found.")

if __name__ == "__main__":
    generate_api_documentation()
    generate_user_manual()
    generate_development_guide()
```