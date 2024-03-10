import psutil #this module is used for retriving information cpu,memory..)
from flask import Flask, render_template #this will going to be run flask module application, to add style in your template we can add render_template


app = Flask(__name__) 

@app.route("/") #this will run the home path of the application
def index():
    cpu_metric = psutil.cpu_percent() #for cpu untilization storing
    mem_metric = psutil.virtual_memory().percent #for memory utilization storing
    Message = None
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=Message)

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')