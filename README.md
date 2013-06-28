Sprite Generator
================

A Python based sprite generator compiles a directory of icon assets into a tightly packed PNG file as well as a CSS file. 


Installation
------------

We recommend installing the sprite generator via PIP. 

On OsX and Linux you can do this via the terminal with the following command:

<pre><code>$ sudo pip install git+https://github.com/dennisschaaf/sprite-generator.git
</code></pre>


Configuration
-------------

In the root of your project directory (or any other place) create .sprite_generator file. This file specifies where to pull the assets from and where to put the generated sprite and css files.

For example if you have the following directory structure, the files will be taken from the assets folder and packed into the css/sprite/ directory by the tool.

![Directory Structure](http://dennisschaaf.github.io/sprite-generator/img/sprite_generator_sample_structure.png "Directory Structure")

.sprite_generator
<pre><code>[path]
inputPath=assets
outputPath=css/sprite
</code></pre>


Usage
-----

Once the project is configured you can execute the spite generator script from anywhere inside the project directory. The script will search for the config file and run as configured.

<pre><code>$ cd /your/project
$ sprite_generator.py
</code></pre>

This will take all the assets and package them up and generate the CSS and PNG file.

The output will look something like this:

![Output](http://dennisschaaf.github.io/sprite-generator/img/generator_output.png "Generator Output")

