# -*- coding: utf-8 -*-

from practice.two.testdata import data


class a(object):
	url = 'http://www.sogou.com'

	@data(path='data.json', pathName='register')
	def say2(testdata):
		print(testdata)
		print(a.url)
		print(testdata['username3'])
if __name__=='__main__':
	p = a()
	p.say2()
