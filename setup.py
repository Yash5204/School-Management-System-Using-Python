import sys
from cx_Freeze import setup,Executable

include_files = ['autorun.inf.py']
base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "s_m_s",
      version = "0.1",
      description = "This is a school management system.The data related to assemblies,special events,time table and attendance can be easily managed using this system",
      options={"build_exe": {'include_files': include_files}},
      executables=[Executable("csproject.py",base=base)])
