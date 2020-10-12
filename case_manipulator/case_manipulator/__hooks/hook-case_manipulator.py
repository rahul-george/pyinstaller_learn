from PyInstaller.utils.hooks import collect_data_files, collect_submodules

packages_for_hidden_import = ["case_manipulator.count_vowels"]

_hiddenimports = []

for pkg in packages_for_hidden_import:
    h_mods = collect_submodules(pkg)
    print("Hidden modules from case_manipulator: {}".format(",".join(h_mods)))
    _hiddenimports.extend(h_mods)

hiddenimports = _hiddenimports
_datas = collect_data_files('case_manipulator.config_files')
print("DATA FILES: {}".format(_datas))
datas = _datas
