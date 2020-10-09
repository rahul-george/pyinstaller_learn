from PyInstaller.utils.hooks import collect_data_files, collect_submodules

packages_for_hidden_import = ["lowerise"]

_hiddenimports = []

for pkg in packages_for_hidden_import:
    h_mods = collect_submodules(pkg)
    print("Hidden modules from lowerise: {}".format(",".join(h_mods)))
    _hiddenimports.extend(h_mods)


hiddenimports = _hiddenimports
datas = collect_data_files('lowerise')