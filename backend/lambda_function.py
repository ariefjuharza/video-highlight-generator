import json

def lambda_handler(event, context):
    # Dummy lambda untuk cek arsitektur
    print("Event received:", json.dumps(event))
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda pipeline initialized!')
    }
