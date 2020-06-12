password = 'a123456'
i = 3
while True:
	pwd = input('请输入密码：')
	if pwd == password:
		print('登录成功！')
		break
	else:
		i = i - 1
		print('你还有', i ,'次机会')
		if i <= 0:
			break