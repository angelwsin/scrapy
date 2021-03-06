'''
__init__.py 文件的作用是将文件夹变为一个Python模块,Python 中的每个模块的包中，都有__init__.py 文件。

通常__init__.py 文件为空，但是我们还可以为它增加其他的功能。我们在导入一个包时，实际上是导入了它的__init__.py文件。
这样我们可以在__init__.py文件中批量导入我们所需要的模块，而不再需要一个一个的导入。


注意这里访问__init__.py文件中的引用文件，需要加上包名。

__init__.py中还有一个重要的变量，__all__, 它用来将模块全部导入。
'''