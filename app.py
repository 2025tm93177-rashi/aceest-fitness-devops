from flask import Flask, jsonify, request

app = Flask(__name__)

# Core Business Data Store
PROGRAMS = {
    "fat_loss": {
        "name": "Fat Loss (FL)",
        "workout": "Mon: Back Squat 5x5 + Core | Tue: EMOM 20min Assault Bike | Wed: Bench Press + 21-15-9",
        "diet": "Breakfast: Egg Whites + Oats | Lunch: Grilled Chicken + Brown Rice | Dinner: Fish Curry + Millet Roti",
        "calorie_factor": 22
    },
    "muscle_gain": {
        "name": "Muscle Gain (MG)",
        "workout": "Mon: Squat 5x5 | Tue: Bench 5x5 | Wed: Deadlift 4x6 | Thu: Front Squat 4x8",
        "diet": "Breakfast: Eggs + PB Oats | Lunch: Chicken Biryani | Dinner: Mutton Curry + Rice",
        "calorie_factor": 35
    },
    "beginner": {
        "name": "Beginner (BG)",
        "workout": "Circuit Training: Air Squats, Ring Rows, Push-ups. Focus: Technique Mastery",
        "diet": "Balanced Tamil Meals: Idli-Sambar, Rice-Dal, Chapati. Target: 120g Protein/day",
        "calorie_factor": 26
    }
}

clients_db = []

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        "status": "online",
        "system": "ACEest Functional Fitness System",
        "version": "1.0.0"
    }), 200

@app.route('/programs', methods=['GET'])
def get_programs():
    return jsonify({"status": "success", "data": PROGRAMS}), 200

@app.route('/calculate-calories', methods=['POST'])
def calculate_calories():
    data = request.get_json() or {}
    weight = data.get('weight')
    program_key = data.get('program')

    if not weight or weight <= 0:
        return jsonify({"error": "Valid positive weight in kg is required"}), 400

    if program_key not in PROGRAMS:
        return jsonify({"error": f"Invalid program key. Choose from: {list(PROGRAMS.keys())}"}), 400

    factor = PROGRAMS[program_key]['calorie_factor']
    estimated_calories = int(weight * factor)

    return jsonify({
        "status": "success",
        "client_weight": weight,
        "program": PROGRAMS[program_key]['name'],
        "estimated_daily_calories": estimated_calories
    }), 200

@app.route('/clients', methods=['POST'])
def add_client():
    data = request.get_json() or {}
    name = data.get('name')
    program_key = data.get('program')
    weight = data.get('weight')

    if not name or not program_key or not weight:
        return jsonify({"error": "Missing required fields: name, program, weight"}), 400

    if program_key not in PROGRAMS:
        return jsonify({"error": "Invalid program selection"}), 400

    client = {
        "id": len(clients_db) + 1,
        "name": name,
        "program": PROGRAMS[program_key]['name'],
        "weight": weight,
        "target_calories": int(weight * PROGRAMS[program_key]['calorie_factor'])
    }
    clients_db.append(client)
    return jsonify({"status": "success", "data": client}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
