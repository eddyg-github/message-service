# app.py
from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'POST':
        data = request.get_json()
        message = data.get('message')
        if message:
            redis_client.lpush('messages', message)
            return jsonify({"success": True, "message": "Message added successfully"})
        else:
            return jsonify({"success": False, "error": "Message is required"}), 400
    elif request.method == 'GET':
        messages = [msg.decode('utf-8') for msg in redis_client.lrange('messages', 0, -1)]
        return jsonify({"messages": messages})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
