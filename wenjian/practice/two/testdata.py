import json,time


# class data_provider(object):
# 	def store(data):
# 		with open('data.json', 'w') as fw:
# 			# 将字典转化为字符串
# 			# json_str = json.dumps(data)
# 			# fw.write(json_str)
# 			# 上面两句等同于下面这句
# 			json.dump(data, fw)
#
# 	def load(path=None,pathName=None):
# 		if path != None and pathName == None:
# 			with open(path, 'r') as f:
# 				return json.load(f)
# 		if pathName!= None and pathName != None:
# 			with open(path, 'r') as f:
# 				data = json.load(f)
# 				return data[pathName]


class data(object):
	def __init__(self,path,pathName):
		self.path = path
		self.pathName = pathName

	def __call__(self,func):
		def wrapper(testdata):
			if self.path != None and self.pathName == None:
				with open(self.path, 'r') as f:
					testdata = json.load(f)
			if self.path != None and self.pathName != None:
				with open(self.path, 'r') as f:
					testdata = json.load(f)
					testdata = testdata[self.pathName]
			func(testdata)
		return  wrapper


# @data(path='data.json',pathName='register')
# def say2(testdata):
# 	print (testdata)
# if __name__=='__main__':
# 	say2('testdata')









