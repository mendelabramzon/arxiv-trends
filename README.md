# arxiv-trends


## arXiv Summary Tool

This command-line tool fetches the most recent articles from arXiv based on a provided keyword and generates a consolidated summary using OpenAI's model.

## Prerequisites

- Python 3.x
- `requests` library
- `openai` library

## Installation

1. Clone this repository or download the `arxiv_summary_tool.py` script.
2. Install the required Python libraries:

```bash
pip install requests openai
```

3. Set up your OpenAI API key. You can either:
   - Replace `'YOUR_OPENAI_API_KEY'` in the script with your actual OpenAI API key.
   - Or set it as an environment variable and modify the script to read from there.

## Usage

Run the tool from the terminal:

```bash
python arxiv_summary_tool.py <YOUR_KEYWORD>
```

Replace `<YOUR_KEYWORD>` with the keyword you want to search for. The script will fetch the most recent articles related to the keyword from arXiv, concatenate their abstracts, and then generate a single summary, which will be printed to the terminal.

## Notes

- Ensure you're aware of the costs associated with making API calls to OpenAI.
- Adjust the `max_tokens` parameter in the `summarize_with_openai` function based on the length and detail you want in the summary.

## License

This project is open-source and available under the MIT License.

---
