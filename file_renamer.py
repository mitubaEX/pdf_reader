#!/usr/bin/env python

import os
import commands
import logging
import traceback
import commands
pwd = commands.getoutput("pwd")
print pwd
os.chdir(pwd)
logging.basicConfig(level=logging.DEBUG)

for root, dirs, files in os.walk('.'):
        for fname in files:
                inpath = os.path.join(root, fname)
                fname = fname.replace("\s", "_")
                fname = fname.replace(" ", "_")
                status, engfname = commands.getstatusoutput('echo "%s" | nkf -e | kakasi -Ha -ka -ja -Ja -Ka -Ea -ga' % fname)
                if status:
                        logging.error ("error: status: " + str(status))
                        continue
                outpath = os.path.join(root, engfname)
                logging.debug ('mv "%s" "%s"' % (inpath, outpath))
                status, output = commands.getstatusoutput('mv "%s" "%s"' % (inpath, outpath))
                if status:
                        logging.error ("error: status: " + str(status))
                        continue
