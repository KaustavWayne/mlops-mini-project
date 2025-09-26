from dagshub import get_repo_bucket_client

# DagsHub repository info
username = "KaustavWayne"
repo = "mlops-mini-project"

# Initialize DagsHub bucket client
client = get_repo_bucket_client(f"{username}/{repo}", flavor="boto")

# List of folders to delete
folders = [
    "data/",
    "data/interim/",
    "data/processed/",
    "data/raw/",
    "models/",
    "reports/"
]

# Loop through each folder and delete all contents
for folder in folders:
    objects = client.list_objects_v2(Bucket=repo, Prefix=folder)
    for obj in objects.get("Contents", []):
        client.delete_object(Bucket=repo, Key=obj["Key"])
    print(f"Deleted folder: {folder} from DagsHub storage.")
