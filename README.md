# HL7v2.5 Parser

This repository contains a Python-based parser for HL7v2.5 medical record files, capable of converting these files into JSON format. This tool has been tested against the Redox engine, demonstrating superior performance in various scenarios.

## Features

- **Parse HL7v2.5 files to JSON:** Converts HL7v2.5 medical records into a structured JSON format for easier processing and integration.
- **Detailed breakdown:** Breaks down HL7 messages into segments, data fields, components, and sub-components for detailed analysis.
- **Validation:** Tested extensively to ensure accuracy and reliability.

## Requirements

- Python 3.11

## Getting Started

To use this parser, simply clone this repository and follow the steps below:

```bash
git clone https://github.com/dev-vivekkumarverma/hl7v2.5-Parser.git
```

**Note:** Do not add the extension of the input file (defaults to `.txt`).

Open the `.ipynb` file in Jupyter Notebook and follow the instructions provided in the markdown cells to parse your HL7v2.5 files.

## Important Points

### Structure:

- **Trigger Event:** The event that takes place which generates the message.
- **Segments:** Data-field delimiter separated (e.g., `<cr>`), identified by a three-letter code (e.g., MHS, PID).
  - **Data-fields:** Data between the data-field separator (`|`). For example: `|A01|20150601135823+0100|`. Datafields can also repeat with the data field seperator ("|") using the repetition seperator character ('~').
    - **Components:** Data inside a data-field separated by component separator delimiter (`^`). For example: `|23432^Smith^Gordon^Denny^Jr^MD^^^AssignAuth&1.2.3.4.5.6&ISO^L^9^1000^DN^ AssignFac&1.2.3.4.5.7&ISO^^G^20100101000000+0100^20330101000000+0100^doctor|`.
      - **Sub-components:** Parts of the components separated by sub-component separator delimiter (`&`) if present. For example: `^AssignFac&1.2.3.4.5.7&ISO^`.

### Example Usage

Here's a brief example of how to use the parser:
- After cloning the repository change the directory with following command
  ```bash
      cd hl7v2.5-Parser
  ```
  then change the `input_file_name` in the `Hl7v2.ipynb` file:
  
```python
input_file_name='hl7v2_test'  # replace with your hl7v2.5 file path
```
then run the entire notebook. Your output files will be stored in `output_folder` with format `{input_file_name}_output_{date}.json`

## Advantages

- **Transparency:** The parser provides detailed keys in the output JSON, allowing for easy cross-referencing with HL7 definitions.
- **Customizable:** Easy to modify and extend for specific use cases.

For reference, use [this recommended site](https://hl7-definition.caristix.com/v2/HL7v2.5.1/) to look up HL7 data fields and structures.

