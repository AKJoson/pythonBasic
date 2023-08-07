#!/usr/bin/python
# Write Python 3 code in this online editor and run it.
print("Hello, World!")
a = 100
if a >  20:
	print("A大于20")
else:
	print("A不大于20")
	
# 动态语言，这个类型不是确定的
boolValue = True
boolValue = "sdfsd"
print(boolValue)

# 列表
lists = ["苹果","橘子",["飞机","大炮"],"月亮"]
print(lists[0])
print(lists[2][1])
# 移除元素
lists.pop(0)
print(lists[0])
# 插入元素, 啥子类型都可以放，灵活的很
lists.append(1)
print(lists[3])

# 元组，定义的时候进行初始化，之后不能再改变
tupleTest = ("wooo",["a",1,True],True,10)
print(tupleTest[2])
print(tupleTest[3])

for value in tupleTest:
	print(value)
testDict={"a":"CCC","b":"AAA",20:True}
print(testDict["a"])
print(testDict[20])

# 函数定义
def test_function(x):
	if x > 0:
		return True
	else:
		return False

print(test_function(0))	

# 函数返回多个值
def calculate(x,y):
	return y,x
# (20, 10) 可以观察到输出是一个元组
print(calculate(10,20))

# 函数默认参数
def studentInfo(name,age = 18):
	#pass
	print("name:",name)
	print("age:",age)
	
# 可以看到中次输出年龄是默认值18
studentInfo("蜡笔小新") 
studentInfo("小鹏鹏",25)

# 可变长参数
def dynamicArgs(name,age,*gf):
	print("name:",name)
	print("age:",age)
	for gfValue in gf:
		print(gfValue)
		
dynamicArgs("张无忌",18,"阿朱","芷若","赵敏")




