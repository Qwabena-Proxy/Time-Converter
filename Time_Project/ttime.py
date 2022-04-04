def time_convert(**kwargs):
  time_convert_dict ={
    '13':'1',
    '14':'2',
    '15':'3',
    '16':'4',
    '17':'5',
    '18':'6',
    '19':'7',
    '20':'8',
    '21':'9',
    '22':'10',
    '23':'11',
    '24':'12',
  }
  #Creating an arg
  a = kwargs['time']
  if a:
    spl = a.split(':')
    if int(spl[0]) > 12:
      ti = time_convert_dict[spl[0]]
      print(f'{ti}:{spl[1]} PM')
    else:
      print(a +' AM')
      
