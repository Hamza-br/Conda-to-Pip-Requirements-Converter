import argparse
import os
from pathlib import Path
import ruamel.yaml


def convert_environment_to_requirements(input_file, output_dir=None):
    """
    Convert conda environment.yml to pip requirements.txt
    
    Args:
        input_file: Path to the environment.yml file
        output_dir: Directory where requirements.txt will be saved (optional)
    """
    yaml = ruamel.yaml.YAML()
    
    try:
        with open(input_file, 'r') as f:
            data = yaml.load(f)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading YAML file: {e}")
        return
    
    requirements = []
    
    for dep in data.get('dependencies', []):
        if isinstance(dep, str):
            # Extract package name and version
            parts = dep.split('=')
            if len(parts) >= 2:
                package = parts[0]
                package_version = parts[1]
                requirements.append(f"{package}=={package_version}")
            elif len(parts) == 1:
                # Just package name, no version specified
                requirements.append(parts[0])
        elif isinstance(dep, dict):
            # Handle pip dependencies
            for preq in dep.get('pip', []):
                requirements.append(preq)
    
    if output_dir:
        output_path = Path(output_dir) / 'requirements.txt'
        Path(output_dir).mkdir(parents=True, exist_ok=True)
    else:
        output_path = Path(input_file).parent / 'requirements.txt'
    
    try:
        with open(output_path, 'w') as fp:
            for requirement in requirements:
                print(requirement, file=fp)
        print(f"Successfully created {output_path}")
        print(f"Total packages: {len(requirements)}")
    except Exception as e:
        print(f"Error writing requirements file: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert Anaconda environment.yml to pip requirements.txt',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s environment.yml
  %(prog)s path/to/environment.yml -o output/
  %(prog)s environment.yml --output-dir ./requirements/
        """
    )
    
    parser.add_argument(
        'input_file',
        help='Path to the environment.yml file'
    )
    
    parser.add_argument(
        '-o', '--output-dir',
        help='Output directory for requirements.txt (default: same as input file)',
        default=None
    )
    
    args = parser.parse_args()
    
    convert_environment_to_requirements(args.input_file, args.output_dir)


if __name__ == '__main__':
    main()
