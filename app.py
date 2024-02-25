from flask import request, jsonify
from models import init_db_with_test_users, User, app
from weather import fetch_weather

@app.route('/update_balance', methods=['GET', 'POST'])
def update_balance():
    if request.method == 'GET':
        user_id = request.args.get('userId')
        city = request.args.get('city')
    else:
        data = request.get_json()
        user_id = data.get('userId')
        city = data.get('city')

    user = User.query.get(user_id)
    if user:
        try:
            temperature = fetch_weather(city)
        except:
            return jsonify({"error": "Error while working with api"}), 400
        try:
            user.update_balance(temperature)
            return jsonify({"message": "Balance is changed"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        return jsonify({"error": "User not found"}), 404



if __name__ == '__main__':
    init_db_with_test_users()
    app.run(debug=False)
