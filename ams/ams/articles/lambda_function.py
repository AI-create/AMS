import json
import requests
from textwrap import shorten

def lambda_handler(event, context):
    # Extract article data from the event
    article_title = event.get('title', '')
    article_content = event.get('content', '')

    # Process the data - for this example, we'll just summarize the content
    summary = shorten(article_content, width=150, placeholder="...")

    # Prepare data to send back to the Django API
    api_url = "https://d2xtaexzsbvmol.cloudfront.net/api/articles/"
    headers = {
        "Authorization": "Bearer your-valid-bearer-token",  # Replace with your actual Bearer token
        "Content-Type": "application/json"
    }
    data = {
        "title": article_title,
        "summary": summary
    }

    # Send the processed data to the Django API
    response = requests.post(api_url, headers=headers, json=data)

    # Log the response for debugging purposes
    print(response.text)

    return {
        'statusCode': response.status_code,
        'body': json.dumps('Article summary processed and sent successfully.')
    }
