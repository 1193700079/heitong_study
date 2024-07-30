import pika


def send_message(queue_name, message):
    # 连接到 RabbitMQ 服务器
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    # 声明一个队列
    channel.queue_declare(queue=queue_name)

    # 发送消息到队列
    channel.basic_publish(exchange="", routing_key=queue_name, body=message)
    print(f" [x] Sent '{message}'")

    # 关闭连接
    connection.close()


if __name__ == "__main__":
    queue_name = "test_queue"
    message = "Hello, RabbitMQ!"
    send_message(queue_name, message)
