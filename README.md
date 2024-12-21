# gtav-files-renamer

## Overview

`gtav-files-renamer` is a tool designed to help you rename files for Grand Theft Auto V (GTA V). This can be particularly useful for modders who need to rename large numbers of audio files with specific naming conventions that are required by the game.

## Features

- Batch rename files
- Customizable naming patterns

## Requirements

- Python 3.x
- `os` module (standard library)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/edev0x/gtav-files-renamer.git
    ```
2. Navigate to the project directory:
    ```sh
    cd gtav-files-renamer
    ```
3. Create your own virtual environment (optional):
    ```sh
    python -m venv env
    ```
4. Activate your virtual environment (optional):
    ```sh
    source env/bin/activate (Linux) or source env/Scripts/activate (Windows)
    ```

## Usage

1. Ensure you have Python 3.x installed on your system.
2. Before running the scripts modify the lines `67, 68, and 69` defining the PATH of `files-to-convert`, `reference` files directory (how the files to convert must be or want to be renamed or created) and the `output` directory, where each of the converted files will be saved.
2. Run the script:
    ```sh
    python init.py
    ```

NOTE: You must edit the `def copy_files`, `def process_files`, `def find_matches` methods to your specific needs. Since this project is an `ad-hoc` solution for renaming **AUDIO** files for the LSPD radio calls.  

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

No license is attached to it, you can use it and modify the source code as your needs.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.
