from utils.clone_repository import clone_repository
from utils.generate_mermaid_diagram import generate_mermaid_diagram
from utils.generate_prompt import generate_prompt
from utils.mermaid import extract_mermaid_from_markdown, mermaid_to_image


if __name__ == "__main__":
    folder_path = "CLONED_REPO"
    prompt_path = "GENERATED_CODE2PROMPT_CODEBASE.md"
    
    github_url = input("Enter the GitHub repository URL: ") 
    google_api_key = input("YOUR_GOOGLE_API_KEY: ")

    max_attempts = input("How many diagrams? (3+ for best results): ")

    exclude_patterns = (
    ".dockerignore,.eslintrc,*.md,**/.git/**,**/.vscode/**,**/.idea/**,"
    "**/node_modules/**,**/dist/**,**/*.gitignore,**/*.scss,**/*.css,"
    "**/yarn.lock,**/package-lock.json,**/*.json,*.json"
    )
    
    clone_repository(github_url, folder_path)
    generate_prompt(folder_path,prompt_path,exclude_patterns)

    for attempt in range(1, int(max_attempts )+ 1):
        try:
            # print(attempt)
            mermaid_output_path = f"output/system_diagram{attempt}.mmd"

            print(f"Attempt {attempt}/{max_attempts}")
            
            generate_mermaid_diagram(prompt_path, google_api_key, mermaid_output_path)
            
            mermaid_code = extract_mermaid_from_markdown(mermaid_output_path)
            
            output_path = f"output/codebase_diagram{attempt}.png"

            mermaid_to_image(mermaid_code, output_path)
            
            print("Process completed successfully.")
            
        except Exception as e:
            print(f"Error on attempt {attempt}: {str(e)}")
            if attempt == max_attempts:
                print("Max attempts reached. Exiting.")