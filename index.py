import os
from flask import Flask, request, jsonify
from docxtpl import DocxTemplate
from flask_cors import CORS
from flask import send_file
import pandas as pd
from send_email import send_offer_letter  # Import email function

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5500"])

file_path = "CandidateData.xlsx"
template_path = "offerLetter.docx"
output_folder = "Generated_Offer_Letters"

# Ensure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

@app.route('/add_candidate', methods=['POST'])
def add_candidate():
    try:
        data = request.form
        print("Received Data:", data)  # Debugging ke liye print

        name = data.get('name')
        position = data.get('position')
        salary = data.get('salary')
        joining_date = data.get('joining_date')
        email = data.get('email')

        # Check agar koi value None ho
        if not all([name, position, salary, joining_date, email]):
            return jsonify({'error': 'Missing data'}), 400

        # Check if file exists
        if not os.path.exists(file_path):
            df = pd.DataFrame(columns=["Name", "Position", "Salary", "JoiningDate", "Email"])
        else:
            df = pd.read_excel(file_path, engine='openpyxl')  # Debugging ke liye engine mention karein
        
        # Append new data
        new_candidate = pd.DataFrame([[name, position, salary, joining_date, email]], columns=df.columns)
        df = pd.concat([df, new_candidate], ignore_index=True)

        # Save Excel file
        df.to_excel(file_path, index=False, engine='openpyxl')
        print("Data saved successfully in Excel!")  # Debugging message

        # **Generate Offer Letter Automatically**
        doc = DocxTemplate(template_path)
        context = {
            "Name": name,
            "Position": position,
            "Salary": salary,
            "Joining_Date": joining_date
        }
        offer_letter_path = os.path.join(output_folder, f"Offer_Letter_{name}.docx")
        doc.render(context)
        doc.save(offer_letter_path)

        print(f"✅ Offer letter generated for {name} at {offer_letter_path}")

        return jsonify({'message': 'Candidate added successfully!'}), 200
    except Exception as e:
        print("Error:", str(e))  # Error terminal me print karein
        return jsonify({'error': str(e)}), 500

# preview button ke liye
@app.route('/preview_offer_letter', methods=['GET'])
def preview_offer_letter():
    candidate_name = request.args.get("name")

    if not candidate_name:
        return jsonify({"error": "Candidate name is required!"}), 400

    file_path = os.path.join(output_folder, f"Offer_Letter_{candidate_name}.docx")

    if not os.path.exists(file_path):
        return jsonify({"error": "Offer letter not found!"}), 404

    return send_file(file_path, as_attachment=False)  # Open in new tab

# send button ke liye
@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        data = request.json
        candidate_name = data.get("name")
        recipient_email = data.get("email")

        if not candidate_name or not recipient_email:
            return jsonify({"error": "Missing candidate name or email"}), 400

        success = send_offer_letter(recipient_email, candidate_name)

        if success:
            return jsonify({"message": "Email sent successfully!"}), 200
        else:
            return jsonify({"error": "Failed to send email"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
