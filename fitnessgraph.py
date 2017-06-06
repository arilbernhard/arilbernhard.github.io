import matplotlib.pyplot as plt
import numpy as np

#plt.rc('text')
plt.rc('font', size=40)
plt.style.use('seaborn-notebook')


steps = [8289.0, 9196.0, 8312.0, 12803.0, 14552.0]
distance = [6.0, 6.9, 6.4, 10.3, 11.1]
time = [217, 197, 208, 260, 284]
calories = [2807.0, 2741.0, 2913.0, 3158.0, 3135.0]
months = ["January", "February", "March", "April", "May"]

length_per_step = []
for i in range(0, len(steps)):
    length_per_step.append((distance[i] / steps[i]) * 1000.0)

meters_per_sec = []
for i in range(0, len(steps)):
    meters_per_sec.append(((distance[i] * 1000.0) / (time[i] * 60) ) )


calories_per_second = []
for i in range(0, len(steps)):
    calories_per_second.append( calories[i] / (time[i] * 60) )


def create_graph(title,ylabel, ycontents, filename):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.title(title)

    #plt.xlabel('Month')
    plt.xticks(range(0, len(months)), months, rotation=300)

    ax.set_ylabel(ylabel)
    ax.plot(range(0,len(months)), ycontents, marker='o', color='red')
    fig.savefig("fitnessgraphs/"+filename+".svg", bbox_inches='tight')
    

create_graph("Average steps per day", "Steps",steps, "steps")
create_graph("Average distance per day","Kilometres", distance, "distance")
create_graph("Average active time per day","Minutes", time, "time")
create_graph("Average calories burned per day","Kcals", calories, "cals")

create_graph("Calories burned per second active", "Kcals/second",calories_per_second, "calpersec")

create_graph("Average length per step", "Metres/step",length_per_step, "metersperstep")
create_graph("Average metres per second when active","Metres/second", meters_per_sec, "meterspersec")
