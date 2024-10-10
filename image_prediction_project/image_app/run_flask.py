import subprocess

def run_flask():
    subprocess.Popen(
        ['python', 'C:/Users/User/Desktop/pfa python/image_prediction_project/image_app/flask_app.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

if __name__ == '__main__':
    run_flask()