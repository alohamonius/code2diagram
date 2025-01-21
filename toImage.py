import base64
import json
import requests
from pathlib import Path

def mermaid_to_image(mermaid_text, output_path, img_format='png'):
    """
    Convert Mermaid diagram text to an image using Mermaid's online render service.
    
    Args:
        mermaid_text (str): The Mermaid diagram definition
        output_path (str): Path where the image should be saved
        img_format (str): Output format - 'png' or 'svg'
    """
    # Encode the Mermaid text to base64
    encoded_text = base64.b64encode(mermaid_text.encode('utf-8')).decode('utf-8')
    
    # Create the API URL with the encoded text
    img_url = f'https://mermaid.ink/img/{encoded_text}'
    
    # Download the image
    response = requests.get(img_url)
    
    if response.status_code == 200:
        # Save the image
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Image saved successfully to {output_path}")
    else:
        print(f"Error: Could not generate image. Status code: {response.status_code}")

def extract_mermaid_from_markdown(markdown_path):
    """
    Extract Mermaid diagram code from markdown file.
    
    Args:
        markdown_path (str): Path to the markdown file
        
    Returns:
        str: Extracted Mermaid diagram code
    """
    with open(markdown_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find content between ```mermaid and ``` tags
    start_tag = "```mermaid"
    end_tag = "```"
    
    start_idx = content.find(start_tag)
    if start_idx == -1:
        raise ValueError("No Mermaid diagram found in markdown file")
        
    start_idx += len(start_tag)
    end_idx = content.find(end_tag, start_idx)
    
    if end_idx == -1:
        raise ValueError("Mermaid diagram not properly closed in markdown file")
        
    return content[start_idx:end_idx].strip()

# Example usage
if __name__ == "__main__":
    # Path to your res.md file
    markdown_path = "res.md"
    
    try:
        # Extract Mermaid diagram from markdown
        mermaid_code = extract_mermaid_from_markdown(markdown_path)
        
        # Convert to image
        output_path = "codebase_diagram.png"  # or .svg for SVG format
        mermaid_to_image(mermaid_code, output_path)
        
    except Exception as e:
        print(f"Error: {str(e)}")