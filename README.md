# Conda to Pip Requirements Converter

A simple Python script that converts Anaconda `environment.yml` files to pip `requirements.txt` files.

## Overview

This tool helps you bridge the gap between conda and pip package management by automatically converting your conda environment specifications into a format that pip can use.

## Features

- Converts conda package specifications to pip format
- Handles both conda and pip dependencies from `environment.yml`
- Supports packages with or without version specifications
- Simple, standalone script with minimal dependencies

## Requirements

- Python 3.x
- ruamel.yaml

Install the required package:
```bash
pip install ruamel.yaml
```

## Usage

### Basic Usage

Convert an `environment.yml` file in the current directory:
```bash
python convert_env.py environment.yml
```

### Specify Input File Path

Convert an environment file from any location:
```bash
python convert_env.py path/to/environment.yml
```

### Specify Output Directory

Save the `requirements.txt` to a specific directory:
```bash
python convert_env.py environment.yml -o output/
python convert_env.py environment.yml --output-dir ./requirements/
```

### Command-Line Options

- `input_file`: Path to the environment.yml file (required)
- `-o, --output-dir`: Output directory for requirements.txt (optional, defaults to same directory as input file)

### Examples

```bash
# Convert environment.yml in current directory
python convert_env.py environment.yml

# Convert from a different directory
python convert_env.py ~/projects/myapp/environment.yml

# Save output to specific location
python convert_env.py environment.yml -o ./pip-requirements/

# Convert and organize in project structure
python convert_env.py envs/dev-environment.yml -o requirements/
```

## Input Format

Your `environment.yml` should follow the standard conda format:

```yaml
name: my-environment
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - numpy=1.21.0
  - pandas
  - pip:
    - requests==2.28.0
    - flask
```

## Output Format

The generated `requirements.txt` will contain:

```
python==3.9
numpy==1.21.0
pandas
requests==2.28.0
flask
```

## How It Works

1. Parses the `environment.yml` file using ruamel.yaml
2. Iterates through dependencies:
   - **String dependencies**: Converts `package=version` to `package==version`
   - **Dict dependencies**: Extracts pip packages and keeps them as-is
3. Writes all dependencies to `requirements.txt`

## Limitations

- Does not preserve conda-specific features like build strings or channels
- Platform-specific dependencies may need manual adjustment
- Some conda packages may have different names in pip

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use and modify as needed.

## Author

[Your Name]

## Acknowledgments

- Built with [ruamel.yaml](https://sourceforge.net/projects/ruamel-yaml/) for robust YAML parsing
