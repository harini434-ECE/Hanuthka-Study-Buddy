from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

user_memory = {}

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/ai-coach', methods=['GET', 'POST'])
def ai_coach():
    if request.method == 'POST':
        user_input = request.json.get('message')

        if "difficult" in user_input:
            user_memory['weak_topic'] = user_input

        response = f"Got it! I’ll remember this: {user_memory.get('weak_topic', '')}"
        return jsonify({'reply': response})

    return render_template('ai_coach.html')

if __name__ == '__main__':
    app.run(debug=True)
