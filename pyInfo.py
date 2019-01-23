#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  pyInfo.py - based on phpinfo function
#  
#  Copyright 2019 William Martinez Bas <metfar@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files 
# (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import atexit;
import sys;

def out():
	global arch;
	try:
		arch.close();
	except:
		pass;
	print("</table></div></body></html>");
	
	

#### MAIN ####

atexit.register(out);

print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="es" dir="ltr">
<head>
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
		<meta charset="utf-8"/>
		<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=.80"> 
		<meta name="description" content="Python Info">
		<style type="text/css">
			body {background-color: #fff; color: #222; font-family: sans-serif;}
			pre {margin: 0; font-family: monospace;}
			a:link {color: #009; text-decoration: none; background-color: #fff;}
			a:hover {text-decoration: underline;}
			table {border-collapse: collapse; border: 0; width: 934px; box-shadow: 1px 2px 3px #111;}
			.center {text-align: center;}
			.center table {margin: 1em auto; text-align: left;}
			.center th {text-align: center !important;}
			td, th {border: 1px solid #789ecf; font-size: 75%; vertical-align: baseline; padding: 0px 5px;}
			h1 {font-size: 150%;}
			h2 {font-size: 125%;}
			.p {text-align: left;}
			.e {background-color: #ccf; width: 300px; font-weight: bold;}
			.h {background-color: #99c; font-weight: bold;}
			.v {background-color: #ddd; max-width: 300px; overflow-x: auto; word-wrap: break-word;}
			.v i {color: #999;}
			img {float: right; border: 0;}
			hr {width: 934px; background-color: #234b6c; border: 0; height: 1px;}
		</style>
		<title>PythonInfo()</title>
		<meta name="ROBOTS" content="NOINDEX,NOFOLLOW,NOARCHIVE" />
</head>
<body>
	<div class="center">
	<table>
		<tr class="h"><td>
		<a href="https://www.python.org/"><img border="0" src="data:image/png;base64,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" alt="Python logo" /></a></td><td style="vertical-align:middle;align:center;"><h1 class="p" style="align:center;vertical-align:middle;">Python Version """+sys.version +"""
</h1>
</td></tr>
</table>
""");


# This modules give any error, so they are excluded: "base64","code","cgi","tkinter","os","pipes","posix","shutil","signal","turtle","urllib","uuid","webbrowse","pydoc"

mods=["sys","platform","__future__","_thread","argparse","array","ast","asyncio","atexit","binascii","binhex","bisect","builtins","bz2","calendar","chunk","cmath","cmd","collections","configparser","contextlib","contextvars","copy","copyreg","cProfile","crypt","csv","ctypes","curses","dataclasses","datetime","dbm","distutils","doctest","email","ensurepip","errno","fcntl","functools","gettext","glob","grp","gzip","hashlib","html","http","io","ipaddress","json","keyword","locale","lzma","math","mimetypes","mmap","msilib","msvcrt","multiprocessing","numbers","parser","pathlib","pdb","pickle","pickletools","pkgutil","plistlib","pprint","profile","pstats","pty","queue","random","re","readline","reprlib","resource","runpy","select","site","socket","sqlite3","ssl","stat","statistics","string","struct","subprocess","symbol","symtable","sysconfig","syslog","tarfile","tempfile","termios","textwrap","threading","time","timeit","token","tokeinze","trace","tracemalloc","tty","types","typing","unicodedata","unittest","uu","venv","winreg","winsound","xml","zipfile","zipimport","zlib","os","__main__"];



arch=open("reg.log","w");
for m in mods:
	try:
		exec(f"import {m}");
		exec(f"mets=dir({m})");
		print(f"<table><tr class='h'><th colspan=2>Module {m}</th></tr>");
		flg=0;
		for f in mets:
			if f!="__builtins__" and flg==0:
				if((m=="os" and f=="WNOHANG") 
					or (m=="__main__" and f=="os") ): ##until os.WNOHANG and __main__.outNone, it doesn't hang
					flg=1;
				try:
					print("<tr><td>");
					res=exec(f"print(str(f)+'</td><td>'+str({m}.{f}())+'</td></tr>');");
					arch.write(f"{m}.{f}()");
				except:
					try:
						res=exec(f"print('<tr><td>{f}</td><td>'+str({m}.{f})+'</td></tr>');");
						arch.write(f"{m}.{f}()");
					except:
						pass;
		print("</table>");
	except:
		pass;
arch.close();
print("</div></body></html>");

