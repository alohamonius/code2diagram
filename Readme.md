# Repo Mermaid Generator

This project generates a Mermaid diagram of a system based on the structure of a GitHub repository. It uses **code2prompt** to generate a prompt and **Gemini** to produce the Mermaid diagram.

## How to Use

1. Open this project in [Gitpod](https://gitpod.io/).
2. When prompted, enter the URL of a GitHub repository.
3. The repository will be cloned, the prompt will be generated, and the Mermaid diagram will be saved to `output/system_diagram.mmd`.

## Requirements

- **code2prompt**: Used for generating prompts from code.
- **Gemini API**: Used to generate the Mermaid diagram.

## License

MIT
