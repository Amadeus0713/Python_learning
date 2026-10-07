students = [
    {"name":"小王","age":19,"gender":"男","major":"计算机","study_hours":15},
    {"name":"小李","age":20,"gender":"女","major":"数学","study_hours":20},
    {"name":"小张","age":19,"gender":"男","major":"英语","study_hours":10},
    {"name":"小赵","age":21,"gender":"女","major":"英语","study_hours":25},
    {"name":"小陈","age":20,"gender":"女","major":"计算机","study_hours":18},
    {"name":"小刘","age":19,"gender":"男","major":"计算机","study_hours":12},
] #student是一个列表（list） 而其中的每一个元素是一个字典（dict）

a = sum(1 for s in students if s["gender"] == "男") #sum（）用来求和
b = sum(1 for s in students if s["gender"] == "女")
c = students.count("name")
d = len(students) #len() 用来统计列表里的元素

study_time_count = sum(s["study_hours"] for s in students)
average_study_time = study_time_count / d

best_name = max(students,key = lambda s:s["study_hours"])["name"] #max()来求最大项
best_time = max(students,key = lambda s:s["study_hours"])["study_hours"]
max(students,key = lambda s:s["study_hours"])["name"]
e = min(students,key = lambda s:s["study_hours"])

print(f"调查人数:{d}")
print(f"男生：{a}")
print(f"女士：{b}")
print(f"平均学习时间:{average_study_time:.2f}")
print(f"学习时间最长：{best_name}")
print(f"学习时间：{best_time}")
print(e)

major_counts = {}
major_times = {}

male_time_choose = 0
for s in students:
    major = s["major"]
    if major not in major_counts:
        major_counts[major] = 0
        major_times[major] = 0
    
    major_counts[major] += 1
    major_times[major] += s["study_hours"]

    if s["study_hours"] >= 15:
        print(s["name"])

    if s["study_hours"] >= 15 and s["gender"] == "男":
        male_time_choose = male_time_choose + 1

for major_name,count in major_counts.items():
    print(f"{major_name}专业：{count}人")

