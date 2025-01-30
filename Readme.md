# GitHub Codebase Architecture Visualizer (AI Generated)

This project generates a Mermaid diagram of a system based on the structure of a GitHub repository. It uses **code2prompt** to generate a prompt and **Gemini** to produce the Mermaid diagram.

## Use Case

- Quick architecture understanding
- Deal with the old code

## How to Use

0. Get API key in [GoogleAI Studio](https://aistudio.google.com/)
1. [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/alohamonius/code2diagram)
2. When prompted, enter the URL of a GitHub repository / API key / Attempts.
3. The repository will be cloned, the prompt will be generated, and the Mermaid diagram will be saved to `output/codebase_diagram*.png`.

## Requirements

- **code2prompt**: Used for generating prompts from code.
- **Gemini API**: Used to generate the Mermaid diagram.

## License

MIT
