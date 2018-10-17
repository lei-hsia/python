Models: 

class BaseModel(models.Model):

	is_delete = models.BooleanField(default = False)
	create_time = models.DateTimeField(auto_now_add = True)
	update_time = models.DateTimeField(auto_now = True)

	class Meta:
		abstract = True


class PassportManager(models.Manager):
	'''操作数据库的方法都写在PassportManager中'''

	def add_one_passport(self, username, password, email):
		'''add one user register info'''
		# 1. 获取self所在的模型类
		model_class = self.model
		# 2. 创建一个model_class模型类对象
		obj = model_class(username = username, password = password, email = email)
		# 3. 保存进数据库
		obj.save()
		# 4. 返回obj
		return obj

class Passport(BaseModel):
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)
	email = models.EmailField()

	objects = PassportManager()

	class Meta:
		db_table = 's_user_account'


views.py:
from df_user.models import Passport

def register(request):
	return render(request, 'df_user/register.html')

def register_handle(request):
	# 用户信息注册
	# 1. receive register info
	username = request.POST.get('user_name')
	password = request.POST.get('pwd')
	email = request.POST.get('email')
	# 2. save info into db
	# 所有操作数据库的工作，都应该写在模型类的Manager类中，
	# method封装好之后，在views.py中直接调用
	#passport = Passport(username = username, password = password, email = email)
	#passport.save()
	obj = Passport.objects.add_one_passport(username = username, password = password, email = email)
	obj.save()

	# 3. jump to login page
