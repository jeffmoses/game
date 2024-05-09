import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name= "game",
    options= { "build_exe": {"packages":["pygame"],
                             "include_files":["racecar.png"]}, 
    }
)
executables = executables