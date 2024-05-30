import qrcode


def generate_qr_code(data, filename):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=4,
    )
    
    # Add data to QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(filename)


if __name__ == "__main__":
    # Example usage
    data = "Log_1"
    filename = "Log_1.png"
    generate_qr_code(data, filename)
    print(f"QR code saved as {filename}")
