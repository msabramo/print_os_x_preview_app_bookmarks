# If true, then the svn revision won't be used to calculate the
# revision (set to True for real releases)
RELEASE = False

__version__ = '0.0'

from setuptools import setup

setup(name="print_os_x_preview_app_bookmarks",
      version=__version__,
      description="Uses Python and PyObjC to parse OS X Preview.app's bookmarks",
      long_description=open('README.md').read(),
      keywords='PyObjC,Preview.app',
      author="Marc Abramowitz",
      author_email="marc@marc-abramowitz.com",
      url="https://github.com/msabramo/print_os_x_preview_app_bookmarks",
      license="MIT",
      zip_safe=False,
      scripts=['print_os_x_preview_app_bookmarks.py'],
      install_requires=['pyobjc-framework-Cocoa>=2.2'],
      )
