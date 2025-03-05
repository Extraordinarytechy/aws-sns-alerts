import boto3

# Initialize SNS client
sns_client = boto3.client("sns", region_name="ap-south-1")  # Change region if needed

# Step1:Ask user for the SNS Topic name
topic_name = input("Enter SNS Topic name: ")
response = sns_client.create_topic(Name=topic_name)
topic_arn = response["TopicArn"]
print(f"SNS Topic Created: {topic_arn}")

# Step2:Ask user to subscribe via Email or SMS
protocol = input("Enter subscription type (email/sms): ").strip().lower()
endpoint = input(f"Enter your {protocol} address (email or phone number): ")

response = sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol=protocol,
    Endpoint=endpoint
)

print("Subscription request sent. Please check your email/SMS to confirm.")

# Step3:Ask user if they want to send a test notification
send_test = input("Do you want to send a test alert? (yes/no): ").strip().lower()

if send_test == "yes":
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message="Test Alert: AWS SNS Setup Successful!",
        Subject="AWS SNS Test Notification"
    )
    print("SNS Alert Sent! Check your email/SMS.")
else:
    print("Setup completed without sending a test alert.")
