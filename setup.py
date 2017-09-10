from setuptools import setup

setup(
    name='Termato',
    version='1.0',
    description='A CLI pomodoro timer!',
    author='Alex Pay',
    url='https://github.com/alexpay',
    py_modules=['termato'],
    install_requires=[
        'click'],
    entry_points='''
        [console_scripts]
        termato=termato:timer
    '''
)
