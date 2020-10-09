# pyinstaller_learn

This repo is created to explore the PyInstaller capabilities. 

PyInstaller features explored in the example: 
 * Giving specific name, 
 * Hidden imports and additional paths to search for
 * Adding additional data files and modules via pyinstaller hooks controlled at package level. 
 * PyInstaller debug features -- noarchive and imports
 * Pyinstaller logging level
 

Following command is used to create the installer and the spec file: 

    python -m PyInstaller --clean 
                          --noconfirm 
                          --noupx 
                          --name manipulate_case 
                          -D 
                          --specpath . 
                          --additional-hooks-dir ..\lowerise\lowerise\__hooks 
                          --paths ..\lowerise 
                          --paths ..\capitalize 
                          --hidden-import lowerise 
                          --hidden-import capitalize 
                          -d noarchive 
                          -d imports 
                          --log-level DEBUG 
                          case_manipulator\case_manipulator.py

Single line for copy/past: 
    python -m PyInstaller --clean --noconfirm --noupx --name manipulate_case -D --specpath . --additional-hooks-dir ..\lowerise\lowerise\__hooks --paths ..\lowerise --paths ..\capitalize --hidden-import lowerise --hidden-import capitalize -d noarchive -d imports --log-level DEBUG case_manipulator\case_manipulator.py

