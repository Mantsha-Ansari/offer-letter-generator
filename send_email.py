import yagmail
import os

# Sender Email Credentials
SENDER_EMAIL = "inayamantsha17@gmail.com"
SENDER_PASSWORD = "tefofpyndlfpmttv"  # Use App Password if 2FA is enabled

try:
    yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)

    print("✅ Successfully connected to Gmail SMTP!")
except Exception as e:
    print(f"❌ Error: {e}")

def send_offer_letter(recipient_email, candidate_name):
    try:
        yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)

        # Offer letter file path
        file_path = os.path.join("Generated_Offer_Letters", f"Offer_Letter_{candidate_name}.docx")

        if not os.path.exists(file_path):
            print(f"❌ Offer letter not found for {candidate_name}")
            return False

        # Email content
        subject = f"Job Offer from HCDS Technologies - {candidate_name}"
        body = f"Dear {candidate_name},\n\nPlease find attached your offer letter.\n\nBest regards,\nHR Team"

        # Send email with attachment
        yag.send(to=recipient_email, subject=subject, contents=body, attachments=[file_path])

        print(f"✅ Offer letter sent successfully to {recipient_email}")
        return True

    except Exception as e:
        print(f"❌ Failed to send email: {str(e)}")
        return False

# Example Usage (For Testing)
# send_offer_letter("recipient@example.com", "John Doe")
