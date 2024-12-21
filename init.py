import os
import shutil
import re

class FileRenameProcessor:
    def __init__(self, input_dir, ref_dir, output_dir):
        self.input_dir = input_dir
        self.ref_dir = ref_dir
        self.output_dir = output_dir
    
    def _create_output_dir(self):
        # Create output directory if it does not exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def get_ref_files(self):
        # Get list of files in reference directory
        return [os.path.splitext(f)[0] for f in os.listdir(self.ref_dir) if os.path.isfile(os.path.join(self.ref_dir, f))]

    def find_matches(self, base_name, ref_files):
        # Search for coincidences in reference files
        search_key = base_name.replace("En_", "").replace("_", " ").lower()
        matches = []
        for ref_file in ref_files:
            if search_key in ref_file.replace("_", " ").lower():
                matches.append(ref_file)

        return matches
    
    def copy_files(self, file_name, matches):
        # Copies the generated files with the found coincidences
        source_file = os.path.join(self.input_dir, file_name)
        for match in matches:
            target_file = os.path.join(self.output_dir, f"{match}.mp3")
            shutil.copyfile(source_file, target_file)
            print(f"Created file: {target_file}")

    def process_files(self):
        # Process all files in input directory
        reference_files = self.get_ref_files()
        input_files = [f for f in os.listdir(self.input_dir) if f.endswith('.mp3')]

        # Counters
        total_processed = 0
        total_matches = 0

        for filename in input_files:
            base_name, ext = os.path.splitext(filename)

            # Find matches
            matches = self.find_matches(base_name, reference_files)
            total_matches += len(matches)

            # Copy files
            self.copy_files(filename, matches)
            total_processed += 1
        
        # Process summary
        print("\nProcess summary:")
        print(f"Total of processed files: {total_processed}")
        print(f"Total of references: {len(reference_files)}")
        print(f"Total of generated files that matches: {total_matches}")
        print("Process completed.")
    
    
if __name__ == "__main__":
    # Define directories
    input_dir = "audios/to-convert" # Directory with files to convert
    reference_dir = "audios/originals/reference" # Directory with reference files
    output_dir = "audios/converted" # Directory to save the converted files

    # Initialize processor
    converter = FileRenameProcessor(input_dir, reference_dir, output_dir)
    converter.process_files()