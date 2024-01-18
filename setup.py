from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='chat-ai',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=required_packages,
    entry_points='''
        [console_scripts]
        chat-ai=src.main:main
    ''',
    author='Siddhant Vij',
    author_email='siddhantvij201@gmail.com',
    description='A terminal-based chat application using OpenAI\'s GPT-4 model.',
    keywords='chat ai openai gpt-4 terminal',
    url='https://github.com/siddhant-vij/Efficient-Chat-AI'
)
