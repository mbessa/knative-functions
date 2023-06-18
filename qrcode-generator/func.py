from flask import Flask, render_template, jsonify
import qrcode
import io
import base64

application = Flask(__name__, template_folder='templates')


@application.route('/')
def qrcodes():
    qr_code_image_red_base64 = generate_qrcodes(color="red", payload="url-red")
    qr_code_image_blue_base64 = generate_qrcodes(color="blue", payload="url-blue")
    return render_template('qrcodes.html', qr_code_image_red_base64=qr_code_image_red_base64, qr_code_image_blue_base64=qr_code_image_blue_base64)


def generate_qrcodes(color, payload):
    # Generate the QR codes
    qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=4)
    qr_code.add_data(payload)
    qr_code.make(fit=True)
    qr_code_image = qr_code.make_image(fill_color=color, back_color="white")

    #Convert image to png base64 encoded
    buffered = io.BytesIO()
    qr_code_image.save(buffered, 'PNG')
    qr_code_image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return qr_code_image_base64



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
