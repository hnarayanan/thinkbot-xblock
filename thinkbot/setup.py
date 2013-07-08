from setuptools import setup

setup(
    name='thinkbot-xblock',
    version='0.2',
    description='Thinkbot XBlock',
    py_modules=['thinkbot'],
    install_requires=['XBlock'],
    entry_points={
        'xblock.v1': [
            'thinkbot_solution = thinkbot:ThinkbotSolutionBlock',
        ]
    }
)
