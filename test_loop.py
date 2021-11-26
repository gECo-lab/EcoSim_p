from time import sleep
from random import random
import requests
from typing import Dict


N_ITERATIONS = 5


def processing() -> None:
	sleep(random() * 1)


def post_current_current_iteration(current_iteration: int) -> None:

	if current_iteration > 0:

		data = {"iteraton": f"{current_iteration}", "end": "0"}		

		resp = requests.post("http://127.0.0.1:5000/status", json=data)

		resp_json: Dict = resp.json()		

		print(resp_json)

		processing()

		return post_current_current_iteration(current_iteration - 1)	

	data = {"iteraton": f"{current_iteration}", "end": "1"}

	resp = requests.post("http://127.0.0.1:5000/status", json=data)

	resp_json: Dict = resp.json()

	print(resp_json)

	return None


post_current_current_iteration(N_ITERATIONS)
