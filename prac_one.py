# 	Exercise one
# Default display code
class Dataset:
    def __init__(self):
        self.type = "csv"
# Solution code
class Dataset:
    def __init__(self, data):
        self.data = data

f = open("nfl.csv", 'r')
csvreader = csv.reader(f)
nfl_data = list(csvreader)

nfl_dataset = Dataset(nfl_data)
dataset_data = nfl_dataset.data

# 	Exercise two
# Default display code
class Dataset:
    def __init__(self, data):
        self.data = data
        
    # Your method goes here
# Solution code
class Dataset:
    def __init__(self, data):
        self.data = data
    
    def print_data(self, num_rows):
        print(self.data[:num_rows])


nfl_dataset = Dataset(nfl_data)
nfl_dataset.print_data(5)
# 	Exercise three
# Default display code
class Dataset:
    def __init__(self, data):
        self.data = data

class Dataset:
    def extract_header(self):
        self.header = self.data[0]
        self.data = self.data[1:]
        
nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.extract_header()