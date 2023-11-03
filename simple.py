import humansize ①
print(humansize.approximate_size(4096, True)) ②
# output 4.0 KiB
print(humansize.approximate_size.__doc__) ③
# output 4.0 KiB
'''
Convert a file size to human-readable form.
Keyword arguments:
size -- file size in bytes
a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
if False, use multiples of 1000
Returns: string
'''


try:
    import chardet
except ImportError:
    chardet = None
#Later, you can check for the presence of the chardet module with a simple if statement:
if chardet:
    # do something
else:
    # continue anyway
'''
Another common use of the ImportError exception is when two modules implement a common A P I , but one is
more desirable than the other. (Maybe it’s faster, or it uses less memory.) You can try to import one module but
fall back to a different module if the first import fails. For example, the XML chapter talks about two modules
that implement a common A P I , called the ElementTree A P I . The first, lxml, is a third-party module that you need
to download and install yourself. The second, xml.etree.ElementTree, is slower but is part of the Python 3
standard library.
'''

try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
'''
By the end of this try..except block, you have imported some module and named it etree. Since both modules
implement a common A P I , the rest of your code doesn’t need to keep checking which module got imported.
'''


# Exception
if size < 0:
    raise ValueError('number must be non-negative')
''' Use the raise statement, followed by the exception name,
  and an optional human-readable string for debugging purposes. The syntax is reminiscent of calling a function. (In
  reality, exceptions are implemented as classes, and this raise statement is actually creating an instance of the
  ValueError class and passing the string 'number must be non-negative' to its initialization method '''



