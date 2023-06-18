from flask import Flask, render_template, jsonify
import qrcode

application = Flask(__name__)


@application.route('/')
def generate_qrcodes():
    # Generate the QR codes
    qr_code_red = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr_code_red.add_data('Red QR Code Data')
    qr_code_red.make(fit=True)
    qr_code_image_red = qr_code_red.make_image(fill_color="red", back_color="white")

    qr_code_blue = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr_code_blue.add_data('Blue QR Code Data')
    qr_code_blue.make(fit=True)
    qr_code_image_blue = qr_code_blue.make_image(fill_color="blue", back_color="white")

    # Render the template with the QR codes
    return render_template('qrcodes.html', qr_code_image_red=qr_code_image_red, qr_code_image_blue=qr_code_image_blue)

@application.route('/health/readiness')
def readiness_check():
    # Perform any readiness checks here
    return jsonify({'status': 'ready'})

@application.route('/health/liveness')
def liveness_check():
    # Perform any liveness checks here
    return jsonify({'status': 'alive'})

if __name__ == '__main__':
    application.run()
