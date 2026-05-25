



library to write python code for
* https://github.com/kivy/pyjnius


examples of writing java class wrappers directly instead of autoclass usage
* https://github.com/SimpleJnius/sj-firebase-ai
* https://github.com/SimpleJnius/sj-firebase-python
* https://github.com/SimpleJnius/sj-gemini-vertex-ai
* https://github.com/SimpleJnius/sj-android-billingclient
* https://github.com/SimpleJnius/sjgeofire
* https://github.com/SimpleJnius/sj-firebase-java
* https://github.com/SimpleJnius/SJGooglePlayBilling
* https://github.com/SimpleJnius/SJAndroidBilling


not sure how to deal with next part but i assume we can use this 
* https://github.com/javaparser/javaparser
to parse the java to ast , and then use the export to json feature

then write a command tool in swift that reads the json (codable) and
use https://github.com/Py-Swift/PySwiftAST to write the python code
soo logic needs to be created in convert the java ast to python ast
* https://github.com/Py-Swift/Figma2Kv/tree/master/Sources/KivyCanvasDesigner example of using PySwiftAst

and for writing the python code there is all the simplejnius repos 

and along the way also write tests to confirm our java_ast->py_ast does as expected always...

the cli tool should just have an input arg for what folder to scan, and destination for where to dump the generated files... 


# generate .pyi version of each file
we need a pyi version of each file generate, that shows the more pythonic api, since pyjnius parts should automatic just example accept str as input and otherside of calls its java string.. and so on... 
