#!/usr/bin/env python3
"""
Microservice App1 - User Management Service
A simple Flask microservice for demo purposes
"""

from flask import Flask, jsonify, request
import os
import socket
from datetime import datetime

app = Flask(__name__)

# Service metadata
SERVICE_NAME = os.getenv('APP_NAME', 'app1')
SERVICE_VERSION = os.getenv('APP_VERSION', '1.0.0')
HOSTNAME = socket.gethostname()

@app.route('/')
def index():
    """Root endpoint"""
    return jsonify({
        'service': SERVICE_NAME,
        'version': SERVICE_VERSION,
        'hostname': HOSTNAME,
        'status': 'running',
        'endpoints': {
            '/': 'This endpoint',
            '/health': 'Health check',
            '/users': 'List users',
            '/users/<id>': 'Get user by ID',
            '/info': 'Service information'
        }
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': SERVICE_NAME,
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/info')
def info():
    """Service information endpoint"""
    return jsonify({
        'service': SERVICE_NAME,
        'version': SERVICE_VERSION,
        'hostname': HOSTNAME,
        'environment': {
            'python_version': os.sys.version,
            'port': os.getenv('PORT', '8080')
        },
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/users', methods=['GET'])
def get_users():
    """Get all users"""
    users = [
        {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'role': 'admin'},
        {'id': 2, 'name': 'Bob', 'email': 'bob@example.com', 'role': 'user'},
        {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com', 'role': 'user'},
    ]
    return jsonify({
        'users': users,
        'count': len(users),
        'service': SERVICE_NAME
    })

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID"""
    users = {
        1: {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'role': 'admin'},
        2: {'id': 2, 'name': 'Bob', 'email': 'bob@example.com', 'role': 'user'},
        3: {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com', 'role': 'user'},
    }
    
    if user_id in users:
        return jsonify({
            'user': users[user_id],
            'service': SERVICE_NAME
        })
    else:
        return jsonify({
            'error': 'User not found',
            'user_id': user_id
        }), 404

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json() or {}
    new_user = {
        'id': len(data) + 1,  # Simple ID generation
        'name': data.get('name', 'Unknown'),
        'email': data.get('email', 'unknown@example.com'),
        'role': data.get('role', 'user')
    }
    return jsonify({
        'message': 'User created',
        'user': new_user,
        'service': SERVICE_NAME
    }), 201

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)

