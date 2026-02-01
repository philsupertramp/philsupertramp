import yaml
import jinja2
import os
import subprocess

# Configuration
DATA_FILE = 'cv_content.yaml'
TEMPLATE_FILE = 'cv_template.tex'
OUTPUT_TEX = 'cv.tex'

def build_pdf():
    # 1. Load the YAML data
    with open(DATA_FILE, 'r') as f:
        data = yaml.safe_load(f)

    # 2. Setup Jinja2 environment with LaTeX-friendly delimiters
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('.'),
        block_start_string='\\BLOCK{',
        block_end_string='}',
        variable_start_string='\\VAR{',
        variable_end_string='}',
        comment_start_string='\\#{',
        comment_end_string='}',
        trim_blocks=True,
        lstrip_blocks=True
    )

    # 3. Render the template
    template = env.get_template(TEMPLATE_FILE)
    rendered_tex = template.render(**data)

    # 4. Write the output .tex file
    with open(OUTPUT_TEX, 'w') as f:
        f.write(rendered_tex)
    
    print(f"Generated {OUTPUT_TEX} successfully.")

if __name__ == "__main__":
    build_pdf()
