Used VS Code to generate this project. 

Also the following command is used to generate the spec file and the dist. 

    python -m PyInstaller --clean --noconfirm --noupx --name manipulate_case -D --specpath . --additional-hooks-dir ..\lowerise\lowerise\__hooks --additional-hooks-dir .\case_manipulator\__hooks --paths ..\lowerise --paths ..\capitalize --paths .\case_manipulator --hidden-import lowerise --hidden-import capitalize -d noarchive --log-level DEBUG case_manipulator\case_manipulator.py 

PyInstaller features explored: 
 * Giving specific name, 
 * Hidden imports and additional paths to search for
 * Adding additional data files and modules via pyinstaller hooks controlled at package level. 
 * PyInstaller debug features -- noarchive and imports
 * Pyinstaller logging level
 * Also handled case when we need to add hooks to the script directory for hidden imports. 