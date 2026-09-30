import requests
import sys


SERVER_URL = "http://127.0.0.1:5000/predict"


def predict_marks(student_data):
	response = requests.post(SERVER_URL, json=student_data, timeout=10)
	response.raise_for_status()
	return response.json()["prediction"]


def main():
	student_data = {
		"attendance": 85,
		"studyhours": 6,
		"assignmentscore": 75,
		"internalmarks": 80,
		"previousgpa": 8.5,
	}

	try:
		prediction = predict_marks(student_data)
	except requests.exceptions.ConnectionError:
		print("Could not connect to the Flask server. Start Flaskserver.py first.")
		sys.exit(1)
	except requests.exceptions.HTTPError as error:
		print(f"The server returned an error: {error}")
		sys.exit(1)

	print(f"Predicted final marks: {prediction:.2f}")


if __name__ == "__main__":
	main()


