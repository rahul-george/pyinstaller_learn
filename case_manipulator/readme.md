Used VS Code to generate this project. 

Also the following command is used to generate the spec file and the dist. 

    python -m PyInstaller --clean --noconfirm --noupx --name manipulate_case -D --specpath . --additional-hooks-dir ..\lowerise\lowerise\__hooks --paths ..\lowerise --paths ..\capitalize --hidden-import lowerise --hidden-import capitalize -d noarchive -d imports --log-level DEBUG case_manipulator\case_manipulator.py

PyInstaller features explored: 
 * Giving specific name, 
 * Hidden imports and additional paths to search for
 * Adding additional data files and modules via pyinstaller hooks controlled at package level. 
 * PyInstaller debug features -- noarchive and imports
 * Pyinstaller logging level