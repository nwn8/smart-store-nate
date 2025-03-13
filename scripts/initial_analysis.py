
import pathlib
import csv
import statistics




data_folder = "data"
raw_folder = pathlib.Path(data_folder, "raw")
customer_data_file = pathlib.Path(raw_folder, "customers_data.csv")

def analyze_Region_data(file_path: pathlib.Path) -> dict:
    """Analyze the data to calculate min, max, mean, and stdev."""
    try:
    
        Region_list = []
        with file_path.open('r') as file:
          
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                try:
                    Region = row["Region"] 
            
                    Region_list.append(Region)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        
      
        print(Region_list)
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}
    
def analyze_data(file_path: pathlib.Path) -> dict:
    """Analyze the data to calculate min, max, mean, and stdev.
    try:
        # initialize an empty list to store the scores
        Region_list = []
        with file_path.open('r') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                try:
                    Region = row["Region"] 
                    # append the score to the list
                    Region_list.append(Region)
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
    """
def process_csv_file():
    """This will write the stats to data_processed/obesity_stats.txt
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
"""

analyze_Region_data(customer_data_file)
