from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/api')
def index():
    return jsonify({
        'status': 'ok',
        'message': 'XyraPanel Backend API',
        'endpoints': {
            'report': 'POST /api/report'
        }
    })

@app.route('/api/report', methods=['POST', 'OPTIONS'])
def report():
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.get_json()
        
        message = data.get('message')
        device_info = data.get('deviceInfo', 'Tidak tersedia')
        subject = data.get('subject', 'Laporan Masalah XyraPanel')
        app_version = data.get('appVersion', '1.0')
        
        if not message:
            return jsonify({'success': False, 'message': 'Message is required'}), 400
        
        smtp_user = os.environ.get('SMTP_USER', 'xyraofficialsup@gmail.com')
        smtp_pass = os.environ.get('SMTP_PASS')
        
        if not smtp_pass:
            return jsonify({'success': False, 'message': 'SMTP not configured'}), 500
        
        waktu = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        
        email_body = f"""
LAPORAN MASALAH XYRAPANEL
========================

Pesan:
{message}

------------------------
INFO PERANGKAT:
{device_info}

App Version: {app_version}
Waktu: {waktu}
        """
        
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = 'xyraofficialsup@gmail.com'
        msg['Subject'] = subject
        msg.attach(MIMEText(email_body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        server.quit()
        
        return jsonify({'success': True, 'message': 'Laporan berhasil dikirim!'})
        
    except Exception as e:
        print(f'Email error: {e}')
        return jsonify({'success': False, 'message': 'Gagal mengirim laporan. Silakan coba lagi.'}), 500

def handler(request):
    with app.test_client() as client:
        return client.get(request.path)
