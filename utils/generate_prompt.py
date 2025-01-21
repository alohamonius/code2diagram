import subprocess

def generate_prompt(repo_folder: str, out:str,exclude_patterns:str):
    """Use code2prompt to generate a prompt from the repository's code."""
    code2prompt_command = (
    f"code2prompt --path {repo_folder} --suppress-comments "
    f"--exclude \"{exclude_patterns}\" "
    f"--template ./mermaid.j2 --output {out}"
)
    subprocess.run(code2prompt_command, shell=True, check=True)