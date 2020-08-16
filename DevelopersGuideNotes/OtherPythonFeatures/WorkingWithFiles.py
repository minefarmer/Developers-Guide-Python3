"""
>>> import requests
>>> dir (requests)
['ConnectTimeout', 'ConnectionError', 'DependencyWarning', 'FileModeWarning', 'HTTPError', 'NullHandler', 'PreparedRequest', 'ReadTimeout', 'Request', 'RequestException', 'RequestsDependencyWarning', 'Response', 'Session', 'Timeout', 'TooManyRedirects', 'URLRequired', '__author__', '__author_email__', '__build__', '__builtins__', '__cached__', '__cake__', '__copyright__', '__description__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__title__', '__url__', '__version__', '_check_cryptography', '_internal_utils', 'adapters', 'api', 'auth', 'certs', 'chardet', 'check_compatibility', 'codes', 'compat', 'cookies', 'cryptography_version', 'delete', 'exceptions', 'get', 'head', 'hooks', 'logging', 'models', 'options', 'packages', 'patch', 'post', 'put', 'pyopenssl', 'request', 'session', 'sessions', 'status_codes', 'structures', 'urllib3', 'utils', 'warnings']
>>> 

FILES: OPEN)
Files allows us to keep data beyond the end of          myfile = open ('my_data.txt', "w+")
our programs.


Python has a built-in function that allows us
to open a file, abd then from there I get an
object that I can read and write with.

>>> myfile = open("myfile.txt", "w")
>>> myfile
<_io.TextIOWrapper name='myfile.txt' mode='w' encoding='UTF-8'>
>>> myfile.write("This is some text")
17
>>> myfile.close()
>>> exit()


FILES: WRITING  
When I've opened a file:                                myfile = open ('my_data.txt', "w+")

I can write data to a file, then close it when          myfile.write("Text")
I've finished.

>>> myfile = open('myfile.txt', 'r')
>>> mydata = myfile.read()
>>> mydata
'This is some text'
>>> myfile.close()
>>> print(mydata)
This is some text


FILES: READING
When I've opened a file:                                myfile =open('my_data.txt', 'r')

I can read data from the file, then close it            mydata = myfile.read()
when I'm finished.

                                                        my.file.close()
                                                        
                                                        print(mydata)
                                                        

"""