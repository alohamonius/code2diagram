import base64
import json
import requests
from pathlib import Path

def mermaid_to_image(mermaid_text, output_path, width=900, height=900, img_format='png'):
    """
    Convert Mermaid diagram text to an image using Mermaid's online render service.
    
    Args:
        mermaid_text (str): The Mermaid diagram definition
        output_path (str): Path where the image should be saved
        width (int): Desired image width in pixels
        height (int): Desired image height in pixels
        img_format (str): Output format - 'png' or 'svg'
    """
    # Create config with size settings




    mermaid_config = {
        "code": mermaid_text,
        "mermaid": {
            "theme": "default",
            "width": width,
            "height": height
        }
    }
    
    # Convert config to JSON and encode
    json_str = json.dumps(mermaid_config)
    encoded_config = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
    
    # Create the API URL with the encoded config
    img_url = f'https://mermaid.ink/img/{encoded_config}'
    
    # Download the image
    response = requests.get(img_url)
    
    if response.status_code == 200:
        # Save the image
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Image saved successfully to {output_path} ({width}x{height})")
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
        
    mermaid_code = content[start_idx:end_idx].strip()
    
    # Remove '(' and ')'
    cleaned_mermaid_code = mermaid_code.replace('(', '').replace(')', '')
    
    return cleaned_mermaid_code