#!/usr/bin/env python3
"""
Microservice App2 - Product Catalog Service
A simple Flask microservice for demo purposes
"""

from flask import Flask, jsonify, request
import os
import socket
from datetime import datetime

app = Flask(__name__)

# Service metadata
SERVICE_NAME = os.getenv('APP_NAME', 'app2')
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
            '/products': 'List products',
            '/products/<id>': 'Get product by ID',
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
            'port': os.getenv('PORT', '8081')
        },
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/products', methods=['GET'])
def get_products():
    """Get all products"""
    products = [
        {'id': 1, 'name': 'Laptop', 'price': 999.99, 'category': 'Electronics', 'stock': 50},
        {'id': 2, 'name': 'Mouse', 'price': 29.99, 'category': 'Electronics', 'stock': 200},
        {'id': 3, 'name': 'Keyboard', 'price': 79.99, 'category': 'Electronics', 'stock': 150},
        {'id': 4, 'name': 'Monitor', 'price': 299.99, 'category': 'Electronics', 'stock': 75},
    ]
    return jsonify({
        'products': products,
        'count': len(products),
        'service': SERVICE_NAME
    })

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get product by ID"""
    products = {
        1: {'id': 1, 'name': 'Laptop', 'price': 999.99, 'category': 'Electronics', 'stock': 50},
        2: {'id': 2, 'name': 'Mouse', 'price': 29.99, 'category': 'Electronics', 'stock': 200},
        3: {'id': 3, 'name': 'Keyboard', 'price': 79.99, 'category': 'Electronics', 'stock': 150},
        4: {'id': 4, 'name': 'Monitor', 'price': 299.99, 'category': 'Electronics', 'stock': 75},
    }
    
    if product_id in products:
        return jsonify({
            'product': products[product_id],
            'service': SERVICE_NAME
        })
    else:
        return jsonify({
            'error': 'Product not found',
            'product_id': product_id
        }), 404

@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product"""
    data = request.get_json() or {}
    new_product = {
        'id': len(data) + 1,  # Simple ID generation
        'name': data.get('name', 'Unknown Product'),
        'price': data.get('price', 0.0),
        'category': data.get('category', 'General'),
        'stock': data.get('stock', 0)
    }
    return jsonify({
        'message': 'Product created',
        'product': new_product,
        'service': SERVICE_NAME
    }), 201

@app.route('/products/<int:product_id>/stock', methods=['GET'])
def get_stock(product_id):
    """Get stock level for a product"""
    products = {
        1: {'id': 1, 'name': 'Laptop', 'stock': 50},
        2: {'id': 2, 'name': 'Mouse', 'stock': 200},
        3: {'id': 3, 'name': 'Keyboard', 'stock': 150},
        4: {'id': 4, 'name': 'Monitor', 'stock': 75},
    }
    
    if product_id in products:
        return jsonify({
            'product_id': product_id,
            'product_name': products[product_id]['name'],
            'stock': products[product_id]['stock'],
            'service': SERVICE_NAME
        })
    else:
        return jsonify({
            'error': 'Product not found',
            'product_id': product_id
        }), 404

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8081))
    app.run(host='0.0.0.0', port=port, debug=False)

