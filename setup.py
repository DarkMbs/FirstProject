import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                       'pandas'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                       'cryptography'])


subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                       'numpy'])
