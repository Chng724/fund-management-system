from flask import Flask, jsonify
from models import db
from routes.funds import funds
from routes.secure import secure
from config import Config, TestConfig

def create_app(config_class=Config):
    # Create an instance of the Flask class
    app = Flask(__name__)

    # Load configuration 
    app.config.from_object(config_class)

    # Initialize the database with the Flask app
    db.init_app(app)

    # Register the 'funds' blueprint with a URL prefix
    app.register_blueprint(funds, url_prefix='/api/funds')

    # Register the 'secure' blueprint with a URL prefix
    app.register_blueprint(secure, url_prefix='/api')

    # Create all database tables 
    with app.app_context():
        db.create_all()

    # Error Handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad Request", "message": str(error)}), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not Found", "message": str(error)}), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({"error": "Method Not Allowed", "message": str(error)}), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred"}), 500

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({"error": "Unauthorized", "message": str(error)}), 401

    return app

# Run the application if this script is executed directly
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
