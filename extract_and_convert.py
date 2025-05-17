import os
from pdfminer.high_level import extract_text
from gtts import gTTS

# === Step 1: Define the path to your PDF file ===
pdf_path = r"C:\Users\ADMIN\OneDrive\Desktop\pdf audio\book.pdf"  # Change this if needed

# === Step 2: Extract text from the PDF ===
try:
    text = extract_text(pdf_path)
    print("✅ PDF text extraction complete.")
except Exception as e:
    print("❌ Error extracting text from PDF:", e)
    text = ""

# === Step 3: Check and display the text ===
if text.strip():
    print("\n📄 Extracted Text Preview:\n")
    print(text[:1000] + "...")  # Show a preview of the first 1000 characters

    # === Step 4: Save extracted text to a file ===
    output_txt_path = os.path.join(os.getcwd(), "output.txt")
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✅ Text saved to: {output_txt_path}")

    # === Step 5: Convert text to speech ===
    try:
        tts = gTTS(text=text, lang='en')
        audio_path = os.path.join(os.getcwd(), "output.mp3")
        tts.save(audio_path)
        print(f"🔊 Audio saved to: {audio_path}")
    except Exception as e:
        print("❌ Error during text-to-speech conversion:", e)

else:
    print("⚠️ No text was extracted from the PDF. It might be scanned or image-based.")
    print("Try using a different PDF or use OCR (like pytesseract) for image-based PDFs.")

print("\n✅ Done!")
