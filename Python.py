def lambda_handler(event, context):
    # Extract 'name' from query string parameters
    name = event.get('queryStringParameters', {}).get('name', 'Guest')
    
    # Return a personalized greeting
    return {
        'statusCode': 200,
        'body': f"Hello, {name}! Welcome to AWS Lambda."
}