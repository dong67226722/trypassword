password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	pwd = input('请输入密码：')
	if pwd == password:
		print('登录成功！')
		break
	else:
		print('密码错误！')
		if i > 0:
			print('你还有', i ,'次机会')
		else:
			print('没机会了，账号已锁，请联络管理员！')