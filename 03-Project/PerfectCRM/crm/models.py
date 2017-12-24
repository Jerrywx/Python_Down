from django.contrib.auth.models import User
from django.db import models


# 客户信息表
class Customer(models.Model):
    '''客户信息表'''
    # 客户昵称
    name = models.CharField(max_length=32, blank=True, null=True)
    # qq
    qq = models.CharField(max_length=64, unique=True)
    # qq 昵称
    qq_name = models.CharField(max_length=64, blank=True, null=True)
    # 电话
    phone = models.CharField(max_length=64, blank=True, null=True)
    # 客户来源
    source_choices = ((0, '转介绍'),
                      (1, 'QQ群'),
                      (2, '官网'),
                      (3, '百度推广'),
                      (4, '51CTO'),
                      (5, '知乎'),
                      (6, '市场推广'),
                      )
    # 客户来源途径
    source = models.SmallIntegerField(choices=source_choices)
    # 介绍人qq
    referral_from = models.CharField(verbose_name="转介绍人qq", max_length=64, blank=True, null=True)
    # 课程
    consult_course = models.ForeignKey("Course", verbose_name="资讯课程")
    # 咨询内容
    content = models.TextField(verbose_name="咨询详情")
    # 创建账号
    consultant = models.ForeignKey("UserProfile")
    # 时间
    date = models.DateTimeField(auto_now_add=True)
    # 备注
    note = models.TextField(blank=True, null=True)
    # 标签
    tags = models.ManyToManyField("Tag", blank=True, null=True)
    # 用户状态
    status_choices = ((0, "已报名"),
                      (1, "未报名"),
                      )
    status = models.SmallIntegerField(choices=status_choices, default=1)

    def __str__(self):
        return self.qq

# 标签
class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


# 客户跟进表
class CustomerFollowUp(models.Model):
    '''客户跟进表'''
    # 客户
    customer = models.ForeignKey("Customer")
    # 跟进内容
    content = models.TextField(verbose_name="跟进内容")
    # 跟进人
    consultant = models.ForeignKey("UserProfile")
    # 日期
    date = models.DateTimeField(auto_now_add=True)
    # 跟进结果
    intention_choices = ((0, '2周内报名'),
                         (1, '1个月内报名'),
                         (2, '近期无报名计划'),
                         (3, '已在其他机构报名'),
                         (4, '已经报名'),
                         (5, '拉黑'),
                         )
    intention = models.SmallIntegerField(choices=intention_choices)

    def __str__(self):
        return "<%s : %s>" % (self.customer.qq, self.intention)


# 课程列表
class Course(models.Model):
    '''课程表'''
    # 课程名
    name = models.CharField(max_length=64)
    # 价格
    price = models.PositiveSmallIntegerField()
    # 课程时间
    period = models.PositiveSmallIntegerField(verbose_name="周期(月)")
    # 课程大纲
    outline = models.TextField()

    def __str__(self):
        return self.name

# 校区
class Branch(models.Model):
    '''校区'''
    name = models.CharField(max_length=128, unique=True)
    addr = models.CharField(max_length=128)

    def __str__(self):
        return self.name


# 班级表
class ClassList(models.Model):
    '''班级表'''
    # 课程
    course = models.ForeignKey("Course")
    # 学期
    semester = models.PositiveSmallIntegerField(verbose_name="学期")
    # 老师
    teachers = models.ManyToManyField("UserProfile")
    # 班级
    branch = models.ForeignKey("Branch", verbose_name="校区")
    # 班级类型
    class_type_choices = ((0, "面授(脱产)"),
                          (1, "面授(周末)"),
                          (2, "网络班")
                          )
    class_type = models.PositiveIntegerField(choices=class_type_choices,verbose_name="班级类型")

    # 开班时间
    start_date = models.DateTimeField(verbose_name="开班日期")
    end_date = models.DateTimeField(verbose_name="结业日期",blank=True, null=True)

    # 联合唯一
    class Meta:
        unique_together = ('branch', 'course', 'semester')

    def __str__(self):
        return "%s %s %s" % (self.branch, self.course, self.semester)


# 上课记录
class CourseRecord(models.Model):
    '''上课记录'''
    # 班级
    from_class = models.ForeignKey("ClassList", verbose_name="班级")
    # 时间
    day_num = models.PositiveIntegerField(verbose_name="第几节(天)")
    # 老师
    teacher = models.ForeignKey("UserProfile")
    # 是否有作业
    has_homework = models.BooleanField(default=True)
    # 做作业标题
    homework_title = models.CharField(max_length=128, blank=True, null=True)
    # 作业内容
    homework_content = models.TextField(blank=True, null=True)
    # 课程大纲
    outline = models.TextField(verbose_name="本节课程大纲")
    # 上课时间
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.from_class, self.day_num)

    class Meta:
        unique_together = ("from_class", "day_num")


# 学习记录
class StudyRecord(models.Model):
    '''学习记录'''
    # 学生
    student = models.ForeignKey("Enrollment")
    # 上课记录
    course_record = models.ForeignKey("CourseRecord")
    # 上课情况
    attendance_choices = ((0, '已签到'),
                          (1, '迟到'),
                          (2, '缺勤'),
                          (3, '早退'),
                          )
    attendance = models.SmallIntegerField(choices=attendance_choices, default=0)

    # 成绩
    score_choices = ((100, "A+"),
                     (90, "A"),
                     (85, "B+"),
                     (80, "B"),
                     (75, "B-"),
                     (70, "C+"),
                     (60, "C"),
                     (40, "C-"),
                     (-50, "D"),
                     (-100, "COPY"),
                     (0, "N/A"),
                     )
    score = models.SmallIntegerField(choices=score_choices)

    # 备注
    memo = models.TextField(blank=True, null=True)
    # 时间
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s %s %s" % (self.student, self.course_record, self.score)


# 报名表
class Enrollment(models.Model):
    '''报名表'''
    # 客户
    customer = models.ForeignKey("Customer")
    # 班级
    enrolled_class = models.ForeignKey("ClassList", verbose_name="所报班级")
    # 谁的客户
    consultant = models.ForeignKey("UserProfile", verbose_name="课程顾问")
    # 是否签合同
    contract_agreed = models.BooleanField(default=False, verbose_name="学生已签合同")
    # 合同是否审核
    contract_approved = models.BooleanField(default=False, verbose_name="合同已审核")
    # 日期
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.customer, self.enrolled_class)

    class Meta:
        unique_together = ("customer", "enrolled_class")


# 缴费记录
class Payment(models.Model):
    '''缴费记录'''
    # 用户
    customer = models.ForeignKey("Customer")
    # 课程
    course = models.ForeignKey("Course", verbose_name="所报课程")
    # 数额
    amount = models.PositiveIntegerField(verbose_name="数额", default=500)
    # 负责人
    consultant = models.ForeignKey("UserProfile")
    # 时间
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.customer, self.amount)


# 账号表
class UserProfile(models.Model):
    '''账号表'''
    # 用户
    user = models.OneToOneField(User)
    # 名称
    name = models.CharField(max_length=32)
    # 角色
    roles = models.ManyToManyField("Role", blank=True, null=True)

    def __str__(self):
        return self.name


# 角色表
class Role(models.Model):
    '''角色表'''
    # 名字
    name = models.CharField(max_length=32, unique=True)
    # 菜单
    menus = models.ManyToManyField("Menu", blank=True)

    def __str__(self):
        return self.name


# 菜单
class Menu(models.Model):
    '''菜单'''
    # 菜单名
    name = models.CharField(max_length=32)
    # 对应url
    url_name = models.CharField(max_length=64);

    def __str__(self):
        return self.name


