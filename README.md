<p align="center"><a href="https://github.com/iann0036/iamfast-js">JavaScript</a> • <b>Python</b> • <a href="https://github.com/iann0036/iamfast-go">Go</a> • <a href="https://github.com/iann0036/iamfast-java">Java</a> • <a href="https://github.com/iann0036/iamfast-vscode">VS Code</a></p>

# iamfast (Python)

:construction: EXPERIMENTAL - WORK IN PROGRESS :construction:

> IAM policy generation from application code

## Usage

```
pip3 install iamfast
```

## Usage

```
iamfast-python yourfile.py
```

## Example

```
> cat tests/test1.py
import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Create a SQS queue
response = sqs.create_queue(
  QueueName='SQS_QUEUE_NAME',
  Attributes={
    'DelaySeconds': '60',
    'MessageRetentionPeriod': '86400'
  }
)

print(response['QueueUrl'])
```

```
> iamfast-python tests/test1.py
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sqs:CreateQueue",
            "Resource": [
                "arn:aws:sqs:us-east-1:123456789012:SQS_QUEUE_NAME"
            ]
        }
    ]
}
```
