from setuptools import setup

setup(name='emojify',
      version='0.1',
      description='A python project to overlay an emoji on your face based on the emotion predicted by the convolutional neural network',
      url='https://github.com/mrtripathi11/Emojify-Create-Your-Own-Emoji-Project',
      author=('Saurabh Tripathi,Aviral Willy,Lalit Agrawal,Siddhant Dubey ,Pratyush Khare'),
      author_email='tsaurabh078@gmail.com',
      license='MIT',
      packages=['emojify'],
      install_requires=[
          'theano',
          'keras',
          'imutils',
          'numpy'
      ],
      zip_safe=False)