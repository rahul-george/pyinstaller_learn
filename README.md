# PyInstaller Learn

This repo is created to explore the PyInstaller capabilities. 

# Features Explored 
PyInstaller features explored in the example: 
 * Giving specific name, 
 * Hidden imports and additional paths to search for
 * Adding additional data files and modules via pyinstaller hooks controlled at package level. 
 * PyInstaller debug features -- noarchive and imports
 * Pyinstaller logging level
 * Handled case when you have hidden import in current package. 
 
# Command to create the exe
Following command is used to create the installer and the spec file: 

    python -m PyInstaller --clean 
                          --noconfirm 
                          --noupx 
                          --name manipulate_case 
                          -D 
                          --specpath . 
                          --additional-hooks-dir ..\lowerise\lowerise\__hooks
                          --additional-hooks-dir .\case_manipulator\__hooks 
                          --paths ..\lowerise 
                          --paths ..\capitalize 
                          --hidden-import lowerise 
                          --hidden-import capitalize 
                          -d noarchive 
                          -d imports 
                          --log-level DEBUG 
                          case_manipulator\case_manipulator.py

Single line for copy/past: 

    python -m PyInstaller --clean --noconfirm --noupx --name manipulate_case -D --specpath . --additional-hooks-dir ..\lowerise\lowerise\__hooks --additional-hooks-dir .\case_manipulator\__hooks --paths ..\lowerise --paths ..\capitalize --paths .\case_manipulator --hidden-import lowerise --hidden-import capitalize -d noarchive --log-level DEBUG case_manipulator\case_manipulator.py 

# Reference 
Refer to the official documentation for pyinstaller for the commandline arguments used. 

https://pyinstaller.readthedocs.io/_/downloads/en/stable/pdf/
