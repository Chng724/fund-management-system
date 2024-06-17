from flask import Blueprint, request, jsonify, abort

# Create a blueprint for secure routes
secure = Blueprint('secure', __name__)

# Route to a secure endpoint
@secure.route('/secure-endpoint', methods=['GET'])
def secure_endpoint():
    # Simulate an authentication check
    if not request.headers.get("Authorization"):
        # 401 Unauthorized status if the Authorization header is missing
        abort(401, description="Missing or invalid authentication token")
    
    # Return a success message if the authentication token is present
    return jsonify({"message": "Access granted to secure endpoint"}), 200
