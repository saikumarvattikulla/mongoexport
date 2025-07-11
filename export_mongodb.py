import subprocess
import os
from pymongo import MongoClient

# Config
DB_NAME = "Influencer"
MONGO_URI = "mongodb://localhost:27017"
OUTPUT_DIR = "./json_exports"

# Full path to mongoexport.exe — update this to your mongoexport location
MONGOEXPORT_PATH = r"C:\Users\USER\Downloads\mongodb-database-tools-windows-x86_64-100.12.2\mongodb-database-tools-windows-x86_64-100.12.2\bin\mongoexport.exe"

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Get list of collections
collections = db.list_collection_names()
print(f"Collections found: {collections}")

# Export each collection using mongoexport command
for coll in collections:
    print(f"Exporting collection: {coll}")
    output_file = os.path.join(OUTPUT_DIR, f"{coll}.json")
    
    cmd = [
        MONGOEXPORT_PATH,
        f"--uri={MONGO_URI}/{DB_NAME}",
        f"--collection={coll}",
        f"--out={output_file}"
    ]
    
    # Run the mongoexport command
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error exporting {coll}: {result.stderr}")
    else:
        print(f"Exported {coll} to {output_file}")

print("All collections exported.")
