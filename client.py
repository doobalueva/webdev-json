from jsonrpcclient import parse, request
import requests

if __name__ == "__main__":
	result = requests.post("http://localhost:5000/", json=request("add", [100,45])).json().get('result')
	print(result)
