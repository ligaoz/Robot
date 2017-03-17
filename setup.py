'''
Created on 17 Mar 2017

@author: liga
'''
from setuptools import setup

setup(name="led_tester",
      version="0.1",
      description="Exploratory Robot",
      url="",
      author="Liga Ozolina",
      author_email="liga.ozolina@ucdconnect.ie",
      license="GPL3",
      packages=["robot"],
      entry_points={
          'console_scripts': ['robot=robot.main:main']
      },
      )
