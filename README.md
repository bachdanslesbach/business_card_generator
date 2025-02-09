# Business Card QR Code Generator

This Python script generates a QR code from a VCF (vCard) file and embeds a thumbnail image into the vCard data. The QR code can be scanned to quickly share contact information.

## Features

- Reads a VCF file and embeds a thumbnail image.
- Encodes the image in Base64 and inserts it into the VCF data.
- Generates a QR code from the modified VCF data.
- Saves the QR code as an image file.

## Requirements

- Python 3.x
- Libraries: `qrcode`, `Pillow`

You can install the required libraries using pip:
```bash
pip install qrcode[pil] pillow
```

## Usage

1. **Prepare Your Files**:
   - Ensure you have a VCF file named `contact.vcf` in the same directory as the script.
   - Place a thumbnail image named `thumbnail.jpg` in the same directory. The image will be resized to 100x100 pixels if it is not already.

2. **Run the Script**:
   - Execute the script using Python:
     ```bash
     python generate_qr.py
     ```

3. **Output**:
   - The script will generate a QR code image named `contact_qr.png` in the same directory.
   - It will also print the size of the encoded data and the QR code version used.

## How It Works

1. **Read the VCF File**:
   - The script reads the `contact.vcf` file and stores its contents.

2. **Process the Thumbnail Image**:
   - The script opens the `thumbnail.jpg` image, resizes it if necessary, and converts it to RGB mode.
   - The image is then encoded in Base64.

3. **Modify the VCF Data**:
   - The Base64-encoded image is inserted into the VCF data with proper line folding.

4. **Generate the QR Code**:
   - A QR code is generated from the modified VCF data.
   - The QR code is saved as `contact_qr.png`.

5. **Output Statistics**:
   - The script prints the size of the encoded data and the QR code version used.

## Notes

- The script assumes the VCF file and thumbnail image are named `contact.vcf` and `thumbnail.jpg`, respectively. You can modify the script to accept different file names if needed.
- The QR code version is automatically selected to fit the data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
