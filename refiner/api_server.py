from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import os
import sys
import traceback
from refiner.refine import Refiner
from refiner.config import settings

app = Flask(__name__)
CORS(app)  # CORS desteği ekle

@app.route('/refine', methods=['POST'])
def refine():
    try:
        data = request.json
        file_id = data.get('file_id')
        encryption_key = data.get('encryption_key')
        
        logging.info(f"Refinement request received for file_id: {file_id}")
        
        # Refiner işlemini başlat
        refiner = Refiner()
        result = refiner.transform()
        
        return jsonify({
            'success': True,
            'result': result.model_dump(),
            'refinement_url': result.refinement_url,
            'schema': result.schema.model_dump()
        })
    except Exception as e:
        logging.error(f"Refinement error: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True) 