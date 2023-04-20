from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in whatsapp_notifications/__init__.py
from whatsapp_notifications import __version__ as version

setup(
	name="whatsapp_notifications",
	version=version,
	description="whatsapp notification integration",
	author="akhilaminc",
	author_email="raaj@akhilaminc.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
