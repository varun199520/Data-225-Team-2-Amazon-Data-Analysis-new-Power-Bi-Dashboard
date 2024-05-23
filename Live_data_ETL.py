import csv
import requests
import boto3
import os
from datetime import datetime

def fetch_and_save_deals():
    url = "https://real-time-amazon-data.p.rapidapi.com/deals"
    headers = {
        "X-RapidAPI-Key": os.getenv('RAPIDAPI_KEY'),
        "X-RapidAPI-Host": "real-time-amazon-data.p.rapidapi.com"
    }
    params = {
        "country": "US",
        "deal_state": "ALL",
        "deal_type": "ALL"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        deals = data.get("data", {}).get("deals", [])

        # Define CSV file name and headers
        current_date = datetime.now().strftime("%Y%m%d")
        csv_file_name = "deals.csv"
        csv_headers = ["Deal ID", "Deal Type", "Deal Title", "Deal Photo", "Deal State", "Deal URL", "Deal Starts At", "Deal Ends At", "Deal Price Min", "Deal Price Max", "Deal Badge", "Type", "Product ASIN", "Is Prime"]

        # Write data to CSV file
        with open(csv_file_name, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=csv_headers)
            writer.writeheader()
            for deal in deals:
                writer.writerow({
                    "Deal ID": deal.get("deal_id", ""),
                    "Deal Type": deal.get("deal_type", ""),
                    "Deal Title": deal.get("deal_title", ""),
                    "Deal Photo": deal.get("deal_photo", ""),
                    "Deal State": deal.get("deal_state", ""),
                    "Deal URL": deal.get("deal_url", ""),
                    "Deal Starts At": deal.get("deal_starts_at", ""),
                    "Deal Ends At": deal.get("deal_ends_at", ""),
                    "Deal Price Min": deal.get("deal_price_min", {}).get("amount", ""),
                    "Deal Price Max": deal.get("deal_price_max", {}).get("amount", ""),
                    "Deal Badge": deal.get("deal_badge", ""),
                    "Type": deal.get("type", ""),
                    "Product ASIN": deal.get("product_asin", ""),
                    "Is Prime": deal.get("is_prime", "")
                })

        # Upload CSV file to S3 bucket
        try :
            s3_client = boto3.client('s3',
                                    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                                    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                                    region_name='us-east-1')  
            
            # Create deals folder if it doesn't exist
            folder_key = f"{current_date}/deals"
            # s3_client.put_object(Bucket=bucket_name, Key=folder_key)
            
            # Upload the CSV file to S3
            object_key = f"{folder_key}/{csv_file_name}"
            bucket_name = "amazon-live-api-data-group2"
            with open(csv_file_name, "rb") as file:
                s3_client.upload_fileobj(file, bucket_name, object_key)

            print(f"Data has been written to and uploaded to S3: s3://{bucket_name}/{object_key}")
        except:
            print("ERROR")
    else:
        print("Failed to retrieve deals. Status Code:", response.status_code)
