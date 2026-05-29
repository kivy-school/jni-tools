from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URLClassLoader"]

class URLClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/URLClassLoader"
    __javaconstructor__ = [("(Ljava/lang/String;[Ljava/net/URL;Ljava/lang/ClassLoader;Ljava/net/URLStreamHandlerFactory;)V", False), ("(Ljava/lang/String;[Ljava/net/URL;Ljava/lang/ClassLoader;)V", False), ("([Ljava/net/URL;Ljava/lang/ClassLoader;Ljava/net/URLStreamHandlerFactory;)V", False), ("([Ljava/net/URL;)V", False), ("([Ljava/net/URL;Ljava/lang/ClassLoader;)V", False)]
    newInstance = JavaMultipleMethod([("([Ljava/net/URL;Ljava/lang/ClassLoader;)Ljava/net/URLClassLoader;", True, False), ("([Ljava/net/URL;)Ljava/net/URLClassLoader;", True, False)])
    findResource = JavaMethod("(Ljava/lang/String;)Ljava/net/URL;")
    getResourceAsStream = JavaMethod("(Ljava/lang/String;)Ljava/io/InputStream;")
    close = JavaMethod("()V")
    findResources = JavaMethod("(Ljava/lang/String;)Ljava/util/Enumeration;")
    getURLs = JavaMethod("()[Ljava/net/URL;")