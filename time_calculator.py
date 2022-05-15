def add_time(start, duration, day = ''):
  daysList = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
  hour = start.split()
  add = duration.split(':')
  time = hour[0]
  time = time.split(':')
  time.append(hour[-1])
  dayCount = 0
  
  for i in range(2):
      time[i] = int(time[i])
      add[i] = int(add[i])
  # print(time)
  # print(add)
  backup = time[2]


  def convertHour():
    mirror = 1
    for i in range(13, 25):
      if i == time[0]:
        time[0] = mirror
        break
      mirror += 1

  
  def changeFormat():
    if time[2] == 'AM':
      time[2] = 'PM'
    elif time[2] == 'PM':
      time[2] = 'AM'

  
  def addTime():
    time[0] += 1

  
  def addMinute():
    time[1] += 1

  if add[0] >= 24:
    check = add[0]
    while check >= 24:
      check -= 24
      dayCount += 1
    if check + time[0] >= 12:
      dayCount += 1
  
  
  for i in range (add[0]):
    if time[0] < 12:
      addTime()
      if time[0] == 12:
        changeFormat()
      continue
    
    if time[0] == 12:
      if i == 0:
        addTime()
        if time[0] > 12:
          convertHour()
      else:
        time[0] = 1


  for i in range(add[1]):
    if time[1] < 60:
      addMinute()
      if time[1] == 60:
        time[1] = 0
        time[0] += 1
        if time [0] == 12:
          changeFormat()
          if time[2] == 'AM':
            dayCount += 1
          continue


  if day == '' :
    if dayCount >= 2:
      time[2] += f' ({dayCount} days later)'
    elif dayCount == 1:
      time[2] += ' (next day)'
    elif dayCount == 0:
      if time[2] == 'AM':
        if backup == 'PM':
          time[2] += ' (next day)'
  else:
    day = day.lower()
    day = day.capitalize()
    if dayCount == 0:
      time[2] += f', {day}'
    else:
      resultDay = ''
      pointer = daysList.index(day)
      for i in range(dayCount):
        if pointer > 6:
          pointer = 0
        if pointer == 6:
          resultDay = daysList[0]
          pointer += 1
        else:
          resultDay = daysList[pointer + 1]
          pointer += 1

      if dayCount == 1:
        time[2] += f', {resultDay} (next day)'
      else:
        time[2] += f', {resultDay} ({dayCount} days later)'


  if len(str(time[1])) == 2:
    new_time = f'{time[0]}:{time[1]} {time[2]}'
  else:
    new_time = f'{time[0]}:0{time[1]} {time[2]}'



  
  # print(time)
  return new_time
