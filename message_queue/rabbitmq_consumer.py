import pika


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


def receive_message(queue_name):
    # 连接到 RabbitMQ 服务器
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    # 声明一个队列
    channel.queue_declare(queue=queue_name)

    # 告诉 RabbitMQ 用哪个函数来接收消息
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    queue_name = "test_queue"
    receive_message(queue_name)
