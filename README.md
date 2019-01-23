# pyInfo

phpinfo-like module for python - useful as a home tool to get a general view of the configuration of your python interpreter

# test
  Just run

  python3 pyInfo.py 2>/dev/null > pythoninfo.html

  and open pythoninfo.html with any browser

# testing it without downloading this code
  [code]
  import urllib.request;#this is just the function to get from url
  exec('a=urllib.request.urlopen("https://raw.githubusercontent.com/metfar/pyInfo/master/pyInfo.py").read(20000);'); #get the pyInfo
  exec(a);#run the pyInfo
  
  # I submitted this solution to php2python too. I hope it is accepted.
  [/code]
  
# contributing
  
  If anyone want to contribute with this project, let us know at metfar@gmail.com
  
# license
  This module is provided as-is
## Enjoy!!!
