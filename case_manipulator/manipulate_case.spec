# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['case_manipulator\\case_manipulator.py'],
             pathex=['..\\lowerise', '..\\capitalize', '.\\case_manipulator', '.'],
             binaries=[],
             datas=[],
             hiddenimports=['lowerise', 'capitalize'],
             hookspath=['..\\lowerise\\lowerise\\__hooks', '.\\case_manipulator\\__hooks'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=True)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='manipulate_case',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='manipulate_case')
