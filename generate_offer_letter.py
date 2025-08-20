from docxtpl import DocxTemplate
import pandas as pd
import os
from send_email import send_offer_letter  # Import email function

# File paths
template_path = "offerLetter.docx"  # Your MS Word template
excel_path = "CandidateData.xlsx"  # Your candidate data Excel file
output_folder = "Generated_Offer_Letters"  # Folder to save the final offer letters

# Ensure output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

 # Load candidate data from Excel
df = pd.read_excel(excel_path)

# Loop through candidates
for _, row in df.iterrows():
    if pd.isna(row["Name"]) or pd.isna(row["Position"]) or pd.isna(row["Salary"]) or pd.isna(row["Joining Date"]):
        print(f"❌ ERROR: Missing data for {row['Name']}. Skipping!")
        continue

    # Load the template
    doc = DocxTemplate(template_path)

    # Context data to replace placeholders
    context = {
        "Name": row["Name"],
        "Position": row["Position"],
        "Salary": str(row["Salary"]),
        "Joining_Date": str(row["Joining Date"])
    }

    # Render template with actual data
    doc.render(context)

    # Save the new offer letter
    output_path = os.path.join(output_folder, f"Offer_Letter_{row['Name']}.docx")
    print(f"Saving offer letter at: {output_path}")  # Debugging
    doc.save(output_path)

    print(f"✅ Offer letter generated for {row['Name']} with formatting intact!")

print("✅ All offer letters generated successfully!")

# Send offer letter via email
send_offer_letter(row["Email"], row["Name"])