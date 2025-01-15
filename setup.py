import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lockis',
    packages=['lockis'],
    version='1.0.2',
    python_requires=">=3.6",
    license='Apache 2.0',
    description='Encrypt your private data with double aes256, hmac and with ttl.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='MishaKorzhik_He1Zen',
    author_email='developer.mishakorzhik@gmail.com',
    url='https://github.com/mishakorzik/lockis',
    project_urls={
        "Bug Tracker": "https://github.com/mishakorzik/lockis/issues",
        "Donate": "https://www.buymeacoffee.com/misakorzik"
    },
    install_requires=["cryptography>=3.2"],
    keywords=["encryption", "private", "key", "cipher", "aes256", "hmac", "ttl", "easy", "sha256"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
    ],

)
