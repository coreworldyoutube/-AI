from setuptools import setup, find_packages

# パッケージ情報
setup(
    name='NekomiAI',  # パッケージ名
    version='0.1',  # バージョン
    packages=find_packages(),  # パッケージの自動探索
    install_requires=[],
    description='NEKO HA SEKAI WO KAERU NODA.',  # ライブラリの簡単な説明
    author='MUNETORI COREWORLD',  # 作者名
    author_email='your.email@example.com',  # 作者のメールアドレス
    url='https://github.com/yourusername/Coreworld',  # GitHub のリポジトリ URL
    classifiers=[  # PyPIにアップロードするときの分類
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # 必要なPythonのバージョン
)
