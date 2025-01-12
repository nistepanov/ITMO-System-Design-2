import pika
import threading
import sys


class Consumer:
    """Класс для получения сообщений из RabbitMQ."""
    def __init__(self, server, channel_name, on_message_callback):
        self.server = server
        self.channel_name = channel_name
        self.connection = None
        self.channel = None
        self.queue_name = None
        self.on_message_callback = on_message_callback

    def connect(self):
        """Подключение к RabbitMQ и настройка очереди для получения сообщений."""
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.channel_name, exchange_type='fanout')

        # Объявляем временную очередь для прослушивания сообщений
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = result.method.queue
        self.channel.queue_bind(exchange=self.channel_name, queue=self.queue_name)

    def start_listening(self):
        """Начало прослушивания сообщений."""
        def callback(ch, method, properties, body):
            self.on_message_callback(body.decode())

        self.channel.basic_consume(queue=self.queue_name, on_message_callback=callback, auto_ack=True)
        print(f"[*] Подключен к каналу '{self.channel_name}'. Ожидание сообщений...", end="\n>> ")
        self.channel.start_consuming()

    def switch_channel(self, new_channel):
        """Переключение на другой канал."""
        try:
            # Отвязываем текущую очередь от канала
            self.channel.queue_unbind(exchange=self.channel_name, queue=self.queue_name)

            # Закрываем текущий канал
            self.channel.close()

            # Обновляем имя канала
            self.channel_name = new_channel

            # Создаем новый канал
            self.channel = self.connection.channel()

            # Декларируем новую очередь
            result = self.channel.queue_declare(queue='', exclusive=True)
            self.queue_name = result.method.queue

            # Привязываем новую очередь к новому каналу
            self.channel.queue_bind(exchange=self.channel_name, queue=self.queue_name)

            print(f"[*] Переключились на канал '{self.channel_name}'.")
        except Exception as e:
            print(f"[!] Ошибка при переключении канала: {e}")

    def close(self):
        """Закрытие соединения."""
        if self.connection:
            self.connection.close()


class Producer:
    """Класс для отправки сообщений в RabbitMQ."""
    def __init__(self, server, channel_name):
        self.server = server
        self.channel_name = channel_name
        self.connection = None
        self.channel = None

    def connect(self):
        """Подключение к RabbitMQ."""
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.channel_name, exchange_type='fanout')

    def send_message(self, message):
        """Отправка сообщения в текущий канал."""
        self.channel.basic_publish(exchange=self.channel_name, routing_key='', body=message)

    def switch_channel(self, new_channel):
        """Переключение на другой канал."""
        self.channel_name = new_channel
        self.channel.exchange_declare(exchange=self.channel_name, exchange_type='fanout')

    def close(self):
        """Закрытие соединения."""
        if self.connection:
            self.connection.close()


class ChatClient:
    """Основной класс чата, объединяющий продюсера и консюмера."""
    def __init__(self, server='127.0.0.1', initial_channel='default'):
        self.server = server
        self.channel_name = initial_channel
        self.consumer = None
        self.producer = None

    def on_message_received(self, message):
        """Обработка входящих сообщений."""
        if not message:
            message = "None"
        print(f"Message in: [{self.channel_name}] {message}")
        print("Awaiting your new message...\r", end='\n>> ')

    def connect(self):
        """Подключение продюсера и консюмера."""
        self.consumer = Consumer(self.server, self.channel_name, self.on_message_received)
        self.consumer.connect()

        self.producer = Producer(self.server, self.channel_name)
        self.producer.connect()

    def start(self):
        """Запуск клиента."""
        listener_thread = threading.Thread(target=self.consumer.start_listening, daemon=True)
        listener_thread.start()

        print(f"[*] Чат-клиент запущен. Текущий сервер: {self.server}, начальный канал: {self.channel_name}")

        try:
            while True:
                user_input = input()
                if user_input.startswith("!switch"):
                    _, new_channel = user_input.split()
                    self.consumer.switch_channel(new_channel)
                    self.producer.switch_channel(new_channel)
                    self.channel_name = new_channel
                else:
                    self.producer.send_message(user_input)
        except KeyboardInterrupt:
            print("\n[!] Завершение работы чата...")
            self.close()

    def close(self):
        """Закрытие соединений."""
        if self.consumer:
            self.consumer.close()
        if self.producer:
            self.producer.close()


def main():
    server = '127.0.0.1'
    initial_channel = 'default'

    if len(sys.argv) > 1:
        initial_channel = sys.argv[1]
    if len(sys.argv) > 2:
        server = sys.argv[2]

    client = ChatClient(server=server, initial_channel=initial_channel)
    client.connect()
    client.start()


if __name__ == "__main__":
    main()
