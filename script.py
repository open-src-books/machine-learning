import subprocess
from pathlib import Path

def main():
    root_dir = Path.cwd()
    source_path = root_dir / "markdown"
    destination_path = root_dir / "pdf"
    mkdirs(source_path, destination_path)
    create_pdf(source_path, destination_path)

def mkdirs(source_path, destination_path):
    # Iterate through all directories in the source path
    for dir_path in source_path.rglob("*"):
        if dir_path.is_dir():
            # Compute the relative path and destination path
            relative_path = dir_path.relative_to(source_path)
            target_dir = destination_path / relative_path

            # Create the target directory
            target_dir.mkdir(parents=True, exist_ok=True)
            print(f"Created: {target_dir}")

def create_pdf(source_path, destination_path):
    for file in source_path.rglob('*.md'):
        if file.is_file():
            input_file = file
            output_file = destination_path / f"{str(input_file.relative_to(source_path))[:-3]}.pdf"

            # Generate PDF files
            command = ["pandoc", str(input_file), "-o", str(output_file)]
            try:
                subprocess.run(command, check=True)
                print(f"PDF created successfully: {output_file}")
            except subprocess.CalledProcessError as e:
                print(f"Error running Pandoc: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
