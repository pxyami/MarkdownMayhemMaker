# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [('./makeSpam.py', '.'),
               ('./ui/*', './ui')]

a = Analysis(['main.py'],
            pathex=['C:\\Users\\i\\PycharmProjects\\MarkdownMayhemMaker'],
            binaries=[],
            datas=added_files,
            hiddenimports=[],
            hookspath=[],
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)
exe = EXE(pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        [],
        name='MarkdownMayhemMaker',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        runtime_tmpdir=None,
        console=False,
        uac_admin=False,
        icon='')