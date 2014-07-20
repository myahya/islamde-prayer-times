#!/usr/bin/python

import getopt, os, string, sys, time, urllib
from bottle import route, run, template
from datetime import date
from stat import S_ISREG, ST_CTIME, ST_MODE

inputfile = ''

def representsInt(s):
  """
  Returns True if the passed string can be represents an integer, False
  otherwise.
  """
  try:
    int(s)
    return True
  except ValueError:
    return False

def getCity(prayertimefile):
  """
  Returns the name of the city in the file.
  """
  f = open(prayertimefile, 'r')

  city = ''
  while True:
    line = f.readline()
    if 'City: ' in line:
      city = string.lstrip(line, 'City ')
      break

  f.close()

  return city

def getTodayLine(prayertimefile):
  """
  Returns the line corresponding to today's entry.
  """
  f = open(prayertimefile, 'r')

  today = date.today()
  month_name = today.strftime('%B')
  day_num = today.day

  while True:
    if month_name in f.readline():
      break;

  f.readline()
  f.readline()
  f.readline()

  print month_name
  print day_num

  day_line = ''
  while True:
    day_line = f.readline()
    parts = string.split(day_line)
    if not parts:
      continue
    current_day_num = parts[0]
    if representsInt(current_day_num) and int(current_day_num) == day_num:
      break

  f.close()
  print day_line
  return day_line


@route('/')
def index():
  """
  Serves index page
  """
  return template('template', today=getTodayLine(inputfile).split(),
                  date=date.today(), city=getCity(inputfile))

def getInputFile(inputfile):
  """
  Returns the input prayer times text file.
  """

  # No input file specified, look for the most recently created txt file
  # that looks like a prayer times file.
  if not inputfile:
    entries = (os.path.join('.', fn) for fn in os.listdir('.'))
    entries = ((os.stat(path), path) for path in entries)
    entries = ((stat[ST_CTIME], path)
              for stat, path in entries if S_ISREG(stat[ST_MODE]))

    for cdate, path in sorted(entries):
      if os.path.basename(path).endswith('.txt'):
        f = open(path, 'r')
        if 'Prayer Times' in f.readline(): # Confirm it's not some random file
          return os.path.basename(path)

  # Download file if needed
  elif inputfile.startswith('http://'):
    print 'Downloading ', inputfile
    remotefile = urllib.URLopener()
    remotefile.retrieve(inputfile,inputfile.split('/')[-1])
    inputfile = inputfile.split('/')[-1]

  else:
    return inputfile

def main(argv):
  """
  Main.
  """
  global inputfile
  try:
    opts, args = getopt.getopt(argv, "hp:i:","")
  except getopt.GetoptError:
    print 'islamde-prayertimes.py -i <inputfile>'
    sys.exit(2)

  port =8087

  for opt, arg in opts:
    if opt in ("-i"):
      inputfile = arg
    if opt in ("-p"):
      port = arg
    if opt in ("-h"):
      print """
usage python islamde-prayertimes.py [-i inputfile] [-p port]

  -h shows this help message.
  -i set the input file (can be a local file or a URL). When omitted, default is
  to use the most recently created txt file in the current directory. If a URL
  is specifid, the file will be downloaded to the current directory.
  -p set the port, the default is 8087."""
      sys.exit(2)

  inputfile = getInputFile(inputfile)

  print 'Running with input file: ', inputfile

  run(host='localhost', port=port)

if __name__ == "__main__":
  main(sys.argv[1:])
