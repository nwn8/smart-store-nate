
import pathlib
import csv
import statistics
from utils import utils_logger


fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"

def analyze_data(file_path: pathlib.Path) -> dict:
    """Analyze the data to calculate min, max, mean, and stdev."""
    try:
        # initialize an empty list to store the scores
        score_list = []
        with file_path.open('r') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                try:
                    score = float(row["Obesity"])  # Extract and convert to float
                    # append the score to the list
                    score_list.append(score)
                except ValueError as e:
                    utils_logger.logger.warning(f"Skipping invalid row: {row} ({e})")
        
        # Calculate statistics
        stats = {
            "min": min(score_list),
            "max": max(score_list),
            "mean": statistics.mean(score_list),
            "stdev": statistics.stdev(score_list) if len(score_list) > 1 else 0,
        }
        return stats
    except Exception as e:
        utils_logger.logger.error(f"Error processing CSV file: {e}")
        return {}
    

def process_csv_file():
    """This will write the stats to data_processed/obesity_stats.txt"""
    input_file = pathlib.Path(fetched_folder_name, "Obesity.csv")
    output_file = pathlib.Path(processed_folder_name, "obesity_stats.txt")
    
    stats = analyze_data(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("Obesity Statistics:\n")
        file.write(f"Minimum: {stats['min']:.2f}\n")
        file.write(f"Maximum: {stats['max']:.2f}\n")
        file.write(f"Mean: {stats['mean']:.2f}\n")
        file.write(f"Standard Deviation: {stats['stdev']:.2f}\n")
    
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")