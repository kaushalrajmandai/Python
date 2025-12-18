import os
import csv
import datetime
from text_processor import TextProcessor, file_exists_check
from summarizer_class import Summarizer

# Decorator is applied to the reading function
class FileManager:
    @file_exists_check
    def read_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()

    def save_summary(self, filename, content):
        # Create folder if it doesn't exist
        folder = "summaries"
        if not os.path.exists(folder):
            os.makedirs(folder)
            
        output_path = os.path.join(folder, f"summary_{filename}")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Summary saved to: {output_path}")

    def update_log(self, input_file, summary_len):
        # Create logs.csv if not exists
        file_exists = os.path.isfile('logs.csv')
        
        with open('logs.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            # Write header if new file
            if not file_exists:
                writer.writerow(['Timestamp', 'Input File', 'Summary Type'])
            
            writer.writerow([datetime.datetime.now(), input_file, summary_len])
        print("Log updated.")

def main():
    print("--- Text File Summarizer ---")
    file_manager = FileManager()
    summarizer = Summarizer()
    
    filename = input("Enter the .txt filename (e.g., input.txt): ")
    
    # Read file (Decorator will handle check)
    text = file_manager.read_file(filename)
    
    if text:
        print("\nChoose summary length:")
        print("1. Short")
        print("2. Medium")
        print("3. Long")
        choice = input("Enter choice (1-3): ")
        
        length_map = {'1': 'short', '2': 'medium', '3': 'long'}
        length_option = length_map.get(choice, 'medium')
        
        print(f"\nGenerating {length_option} summary...")
        
        # Generate Summary
        summary = summarizer.generate_summary(text, length_option)
        
        print("\n--- Summary Output ---")
        print(summary)
        print("----------------------\n")
        
        # Save and Log
        file_manager.save_summary(filename, summary)
        file_manager.update_log(filename, length_option)

if __name__ == "__main__":
    main()
    