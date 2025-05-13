import unittest
from unittest.mock import patch, MagicMock
from sqs_sender import send_message_to_sqs

class TestSQSSender(unittest.TestCase):

    @patch("sqs_sender.boto3.client")
    def test_send_message_success(self, mock_boto_client):
        # Arrange
        mock_sqs = MagicMock()
        mock_response = {
            "MessageId": "12345",
            "ResponseMetadata": {"HTTPStatusCode": 200}
        }
        mock_sqs.send_message.return_value = mock_response
        mock_boto_client.return_value = mock_sqs

        queue_url = "https://sqs.us-east-1.amazonaws.com/123456789012/my-queue"
        message_body = "Hello, SQS!"

        # Act
        response = send_message_to_sqs(queue_url, message_body)

        # Assert
        mock_sqs.send_message.assert_called_once_with(
            QueueUrl=queue_url,
            MessageBody=message_body
        )
        self.assertEqual(response["MessageId"], "12345")

    @patch("sqs_sender.boto3.client")
    def test_send_message_failure(self, mock_boto_client):
        # Arrange
        mock_sqs = MagicMock()
        mock_sqs.send_message.side_effect = Exception("Erro de teste")
        mock_boto_client.return_value = mock_sqs

        # Act
        response = send_message_to_sqs("fake_url", "msg")

        # Assert
        self.assertIn("Error", response)

if __name__ == "__main__":
    unittest.main()
