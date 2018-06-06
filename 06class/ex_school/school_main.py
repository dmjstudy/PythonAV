#!/usr/bin/python3
# coding: utf-8 
"""
__title__ = ''
__author__ = ''dengminjie
__mtime__ = '18/06/05 0005'
#  功能
角色:学校、学员、课程、讲师
要求:
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含，周期，价格，通过学校创建课程
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
5. 创建讲师角色时要关联学校，
6. 提供两个角色接口
6.1 学员视图， 可以注册， 交学费， 选择班级，
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
6.3 管理视图，创建讲师， 创建班级，创建课程
7. 上面的操作产生的数据都通过pickle序列化保存到文件里
"""

class School(object):
    def __init__(self,sl_id,sl_name,sl_addr):
        self.sl_id=sl_id
        self.sl_name=sl_name
        self.sl_addr = sl_addr
        self.students = []
        self.staffs = []
        self.all_Te_name = []
        self.all_St_name= []

    def enroll(self, stu_obj):
        print("为学员%s 办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)
        self.all_St_name.append(stu_obj.name)

    def hire(self, staff_obj):
        print("雇佣新员工%s" % staff_obj.name)
        self.staffs.append(staff_obj)
        self.all_Te_name.append(staff_obj.name)

    def sl_print(self):
        print("""
            学校ID       学校        教师
            %s%s %s
            学生有 %s
        """%(self.sl_id.ljust(10," "),
             self.sl_addr.ljust(10," "),
             str(self.all_Te_name).ljust(15," "),
             str(self.all_St_name).ljust(15," "))
        )

class Course(object):
    def __init__(self,co_id,co_name,co_price):
        self.co_id = co_id
        self.co_name = co_name
        self.co_price = co_price




class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course
    def tell(self):
        print('''
        ---- info of Teacher:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print("%s is teaching course [%s]" %(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        ---- info of Student:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self,amount):
        print("%s has paid tution for $%d"% (self.name,amount) )

def main():
    school_bj = School('1', '老男孩', 'Beijing')
    school_sh = School('2', '教育', 'ShangHai')
    # self,name,age,sex,salary,course
    teacher1 = Teacher("dengMinjie", '28', 'M', '10000', 'python')
    teacher2 = Teacher("zhangYu", '25', 'F', '10000', 'python')
    student1 = Student("shuyan",'03','F','1001','一')
    student2 = Student("shuyang",'02','M','1002','一')
    # student1.tell()
    # student2.tell()

    school_bj.hire(teacher1)
    school_bj.hire(teacher2)
    school_bj.enroll(student1)
    school_bj.enroll(student2)
    student1.pay_tuition(1000)
    student2.pay_tuition(1000)

    school_bj.sl_print()
    school_sh.sl_print()

if __name__ == '__main__':
    main()

