def employee(**args):
    for key,value in args.items():
        print(f"{key} : {value}")

employee(Name="Steve",ID=35,Dept="AIML",Salary=30000)