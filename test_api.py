import pytest
import requests
import json
import page

# @pytest.mark.api
# class TestCreateEntry(object):

# 	def test_api_create_entry(self):
	# 	url = pytest.api + "address/new"
	# 	payload = pytest.apidata.copy()
	# 	payload["apikey"] = pytest.key
	# 	r =requests.post(url, data = payload)
	# 	temp = json.loads(r.text)
	# 	print ("\nHTTP status code: " + str(r.status_code))
	# 	r.raise_for_status()
	# 	if temp.get("error"):
	# 		pytest.fail(temp.get("error"))
	# 	rid = temp.get("id").encode('ascii', 'ignore')
	# 	pytest.rid = rid
	# 	if 'id' in temp: 
	# 		del temp['id']
	# 	assert cmp(temp, pytest.data) == 0, "API response does not match initial payload"

	# def test_api_view(self):
	# 	payload = {"apikey":pytest.key, "id": pytest.rid}
	# 	url = pytest.api + "address/view"
	# 	r =requests.get(url, params = payload)
	# 	temp = json.loads(r.text)
	# 	if 'id' in temp: 
	# 		del temp['id']
	# 	print ("\nHTTP status code: " + str(r.status_code))
	# 	r.raise_for_status()
	# 	if temp.get("error"):
	# 		pytest.fail(temp.get("error"))
	# 	assert cmp(temp, pytest.apidata) == 0, "API response does not match initial payload"


	# def test_api_delete(self):
	# 	payload = {"apikey":pytest.key, "id": pytest.rid}
	# 	url = pytest.api + "address/delete"
	# 	r =requests.post(url, data = payload)
	# 	temp = json.loads(r.text)
	# 	print (str(temp))
	# 	print ("\nHTTP status code: " + str(r.status_code))
	# 	r.raise_for_status()
	# 	if temp.get("error"):
	# 		pytest.fail(temp.get("error"))
	# 	assert str(temp.get("message")).lower() == "success"
