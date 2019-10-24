import requests

class TestJenkins():
	"""
	Test get a list of jobs from jenkins
	"""
	def test_get_all_job_names(value):
		print(value)
		url = "http://10.62.81.252:8088/api/json?tree=jobs[name]"
		r = requests.get(url)
		jobs = r.json()
		assert jobs['jobs'][0]['name'] == expect1
		assert jobs['jobs'][1]['name'] == expect2
		assert jobs['jobs'][-1]['name'] == expect3


if __name__ == "__main__":
	p = TestJenkins()
	p.test_get_all_job_names()