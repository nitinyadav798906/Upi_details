from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/extract_upi', methods=['POST'])
def extract_upi():
    details = request.json  # Get JSON data from POST request
    if not details:
        return jsonify({"error": "No data provided"}), 400
    
    required_fields = [
        "Name", "UPI Id", "Full Details", "MICR", "Branch", "Address",
        "State", "Contact", "UPI", "RTGS", "City", "Centre", "District",
        "NEFT", "IMPS", "SWIFT", "ISO3166", "Bank", "BankCode", "IFSC",
        "PhonePe Number"
    ]
    
    response = {field: details.get(field, "Not provided") for field in required_fields}
    
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(port=5000)
