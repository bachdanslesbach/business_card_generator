import qrcode
import base64
from PIL import Image

# Read the VCF file
with open("contact.vcf", "r", encoding="utf-8") as f:
    vcf_lines = f.read().splitlines()

# Load and verify the optimized image
img = Image.open("thumbnail.jpg")
if img.size != (100, 100):
    img = img.resize((100, 100), Image.Resampling.LANCZOS)

# Convert to RGB if needed (JPEG requires RGB)
if img.mode != "RGB":
    img = img.convert("RGB")

# Encode image as Base64
with open("thumbnail.jpg", "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

# Build PHOTO property with proper line folding
photo_entry = f"PHOTO;ENCODING=b;TYPE=JPEG:{encoded_image}"
max_length = 75
folded_photo = []
current_line = ""

for char in photo_entry:
    if len(current_line) < max_length:
        current_line += char
    else:
        folded_photo.append(current_line)
        current_line = " " + char  # Continuation line starts with space
folded_photo.append(current_line)

# Insert photo before END:VCARD
end_index = next(i for i, line in enumerate(vcf_lines) if line.strip() == "END:VCARD")
for line in reversed(folded_photo):
    vcf_lines.insert(end_index, line)

# Generate QR code
qr = qrcode.QRCode(
    version=None,  # Auto-select version
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=8,    # Smaller boxes for better scanning
    border=2,
)
qr.add_data("\n".join(vcf_lines))
qr.make(fit=True)

# Save QR code
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save("contact_qr.png")

# Show final stats
data_size = len("\n".join(vcf_lines).encode("utf-8"))
print(f"✅ QR code generated! Data size: {data_size} bytes")
print(f"QR version used: {qr.version} (max 40)")