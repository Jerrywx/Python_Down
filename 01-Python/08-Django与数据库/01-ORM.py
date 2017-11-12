
'''

操作流程
    一、创建项目
        django-admin.py startproject 项目名称
    二、创建模型app
        django-admin.py startapp 模型app名称
    三、在 模型app/models.py 文件中添加数据模型

    四、在 项目 settings.py 文件
        INSTALLED_APPS 下 添加 模型app名称

    五、创建表结构
        python manage.py migrate   # 创建表结构
        $ python3.6 manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
        $ python3.6 manage.py migrate TestModel   # 创建表结构


ORM(对象关系映射)

一、创建表
    1. 单表

    2. 关联表
        一对一 (OneToOne)
        一对多 (ForeignKey)
        多对多 (ManyToMany)

二、操作表(curt):
    1. 增
        a. create
            // 方法一: 使用属性创建
            models.Book.objects.create(title="Python", price=12)
            // 方法二: 使用字典
            dic = {"title":"GO", "price":45}
            models.Book.objects.create(**dic)

            # 如果有外键
            # 一对多


        b. savre
            // 方法一:
            obj=Book(title="Python", price=12)
            obj.save()
            // 方法二:
            obj=Book()
            obj.title = "Go"
            obj.price = 45
            obj.save
    2. 删

    3. 改

    4. 查


三、联合唯一

    class Meta:
        unique_together=["author", "book"]

'''

