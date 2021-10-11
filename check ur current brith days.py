import datetime as dt
bd=dt.datetime(2000,12,25)
time_alive=dt.datetime.today()-bd
print("days",time_alive.days)
print("seconds",time_alive.seconds)
print("microseconds",time_alive.microseconds)
print("min",time_alive.min)
