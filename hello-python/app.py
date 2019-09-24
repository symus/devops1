import os, pika
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

host = os.getenv("RABBITMQ_HOST", "localhost")
port = os.getenv("RABBITMQ_PORT", 5672)
queue = os.getenv("RABBITMQ_QUEUE", "hello")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        flavour=request.form.get("flavour")
        app.logger.info(flavour)
        enqueue(flavour)
    return render_template("landing.html")


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})


def enqueue(value):
    app.logger.info("Received message: %s", value)
    params = pika.ConnectionParameters(host=host, port=port)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange='', routing_key=queue, body=value)
    connection.close()
    app.logger.info("Enqueued message on host %s:%s queue %s: %s", host, port,
                    queue, value)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)