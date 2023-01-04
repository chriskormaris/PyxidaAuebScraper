# -*- mode: python -*-

block_cipher = None


a = Analysis(['src\\pyxida_gui.py'],
             pathex=['.'],
             binaries=[],
             datas=[('src\\img\\compass.ico', 'img'), ('src\\img\\info.ico', 'img')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['tk'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='pyxida_gui',
          debug=False,
          strip=False,
          upx=True,
          console=True,
          icon='src\\img\\compass.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='pyxida_gui')
