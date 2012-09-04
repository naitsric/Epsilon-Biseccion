from distutils.core import setup
import py2exe
setup(name="Epsilon",
      version="0.1",
      description="Con esta Aplicacion pordras ver la presicion de tu equipo",
      author="@N4itRiC",
      author_email="anticris9303@gmil.com",
      url="https://www.facebook.com/Naitsric2011",
      license="GPL",
      scripts=["epsilon.py"],
      console=["epsilon.py"]
)