import math as m
import datetime as dt
import json
import os

noclass = ["Lunch"]
extra_stuff = "?authuser=1&hs=179"
jsonfile = "classes.json"


class Gtime:
	"""Gavin's time of day object"""
	def __init__(self, int_time):
		if type(int_time) is int:
			self.minutes = int_time % 100
			self.hours = m.floor(int_time / 100)
		elif type(int_time) is Gtime:
			self.minutes = int_time.minutes
			self.hours = int_time.hours

	def __sub__(self, other_Gtime):
		hour_dif = (self.hours - other_Gtime.hours) * 100
		min_dif = self.minutes - other_Gtime.minutes
		if min_dif < 0:
			hour_dif -= 100
			min_dif += 60
		if min_dif >= 60:
			hour_dif += 100
			min_dif -= 60
		return Gtime(hour_dif + min_dif)

	def __add__(self, other_Gtime):
		hour_sum = (self.hours + other_Gtime.hours) * 100
		min_sum = self.minutes + other_Gtime.minutes
		if min_sum < 0:
			hour_sum -= 100
			min_sum += 60
		if min_sum >= 60:
			hour_sum += 100
			min_sum -= 60
		return Gtime(hour_sum + min_sum)

	def __lt__(self, other_Gtime):
		return self.to_int() < Gtime(other_Gtime).to_int()

	def __gt__(self, other_Gtime):
		return self.to_int() > Gtime(other_Gtime).to_int()

	def __le__(self, other_Gtime):
		return self.to_int() <= Gtime(other_Gtime).to_int()

	def __ge__(self, other_Gtime):
		return self.to_int() >= Gtime(other_Gtime).to_int()

	def __eq__(self, other_Gtime):
		return self.to_int() == Gtime(other_Gtime).to_int()


	def c_time():
		dt_current = dt.datetime.now().time()
		return Gtime(100 * dt_current.hour + dt_current.minute)

	def to_int(self):
		return 100 * self.hours + self.minutes

	def in_timerange(self, other_Gtime_range: tuple):
		return other_Gtime_range[0] >= self and other_Gtime_range[1] < self


class Schedule:

	#			0			1				2		3		4			5			6			7		8			9
	colors = ["Yellow", "Light Blue", "Homeroom", "Pink", "Green", "Dark Blue", "Orange", "Purple", "X-Block", "Lunch", "None"]
	schedule = [
	[0, 2, 1, 9, 6, 5, 10],
	[4, 2, 3, 9, 7, 8, 10],
	[0, 1, 2, 3, 4, 5, 6, 7, 9, 10],
	[1, 2, 0, 9, 5, 6, 10],
	[3, 2, 4, 9, 8, 7, 10]
	]

	timings = [
	[(800, 920), (920, 945), (945, 1105), (1105, 1135), (1135, 1255), (1305, 1425), (1425, 2400)],
	[(800, 920), (920, 945), (945, 1105), (1105, 1135), (1135, 1255), (1305, 1425), (1425, 2400)],
	[(800, 820), (830, 850), (855, 905), (910, 930), (940, 1000), (1010, 1030), (1040, 1100), (1110, 1130), (1130, 2400)],
	[(800, 920), (920, 945), (945, 1105), (1105, 1135), (1135, 1255), (1305, 1425), (1425, 2400)],
	[(800, 920), (920, 945), (945, 1105), (1105, 1135), (1135, 1255), (1305, 1425), (1425, 2400)]
	]


	def __init__(self, courses: dict):
		self.courses = {}
		for color in courses:
			self.courses[color] = {}
			self.courses[color]["name"] = courses[color]["name"]
			self.courses[color]["meet_link"] = courses[color]["meet_link"]

	def get_day():
		return dt.datetime.today().weekday()



	def timed_index(time, arr_ignore:list = []):
		time_to_find = Gtime(time)
		day = Schedule.get_day()
		# print((Schedule.timings[day]))
		for idx, val in enumerate(Schedule.timings[day]):
			if Schedule.colors[Schedule.schedule[day][idx]] in arr_ignore:
				continue
			if Gtime(Schedule.timings[day][idx][1]) > time_to_find:
				return idx
			if idx > 0 and Gtime(Schedule.timings[day][idx][1]) <  time_to_find and Gtime(Schedule.timings[day][idx - 1][1]) >=  time_to_find:
				return idx
			

		return False
			
	def get_color(time, arr_ignore:list = []):
		day = Schedule.get_day()
		return Schedule.colors[Schedule.schedule[day][Schedule.timed_index(time, arr_ignore=arr_ignore)]]

	def get_class_name(self, time, arr_ignore:list = []):
		day = Schedule.get_day()
		return self.courses[Schedule.get_color(time, arr_ignore=arr_ignore)]["name"]

	def get_next_meet_link(self, time, arr_ignore:list = []):
		timef = Gtime(time)
		day = Schedule.get_day()
		color = Schedule.get_color(timef, arr_ignore=arr_ignore)
		return self.courses[color]["meet_link"]


f = open(jsonfile,)
data = json.load(f)
schd = Schedule(data)
f.close()


time = Gtime.c_time()
# time = 920
next_class = schd.get_class_name(time, arr_ignore=noclass)
link = schd.get_next_meet_link(time, arr_ignore=noclass)
if link:
	os.system('start chrome "'+ link + extra_stuff + '"')
else
	print("no more classes")
