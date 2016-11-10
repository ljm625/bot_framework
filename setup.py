try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='GimmeBot',
    version='0.0.1',
    description='Smart Engine',
    authors='Team GimmeBot',
    author_email='jiaminli@cisco.com & edguribe@cisco.com & joshwong@cisco.com',
    url='https://gitscm@gitscm.cisco.com/scm/sa/gimmebot.git',
    packages=['gimmebot'],
    scripts=[],
    data_files=[],
    #Update if additonal installs required
    install_requires=['PyYAML==3.11'],
)
