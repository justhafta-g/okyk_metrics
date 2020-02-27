#!/usr/bin/python

import sys
import psutil

try:
	metric_type = sys.argv[1]
except Exception:
	sys.exit("Invalide argument, use cpu or mem.")

if metric_type == "mem":
	s_mem = psutil.swap_memory()
	v_mem = psutil.virtual_memory()
        print "virtual total", v_mem.total
	print "virtual used", v_mem.used
	print "virtual free", v_mem.free
	print "virtual shared", v_mem.shared
	print "swap total", s_mem.total
	print "swap used", s_mem.used
	print "swap free", s_mem.free
elif metric_type == "cpu":
        cpu = psutil.cpu_times(percpu=False)
        print "system.cpu.idle", cpu.idle
        print "system.cpu.user", cpu.user
        print "system.cpu.guest", cpu.guest
        print "system.cpu.iowait", cpu.iowait
        print "system.cpu.stolen", cpu.steal
        print "system.cpu.system", cpu.system
else:
        print "Argumet is not define, use mem or cpu!"


