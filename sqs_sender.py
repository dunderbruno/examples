import boto3
from botocore.exceptions import BotoCoreError, ClientError

def send_message_to_sqs(queue_url: str, message_body: str) -> dict:
    """
    Envia uma mensagem para uma fila SQS.

    :param queue_url: URL da fila SQS
    :param message_body: Conteúdo da mensagem
    :return: Resposta do SQS ou erro
    """
    sqs = boto3.client("sqs")

    try:
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body
        )
        return response
    except (BotoCoreError, ClientError) as error:
        print(f"Erro ao enviar mensagem para SQS: {error}")
        return {"Error": str(error)}
