from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["URLClassLoader"]

class URLClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/URLClassLoader"
    __javaconstructor__ = [("([Ljava/net/URL;Ljava/lang/ClassLoader;)V", False), ("([Ljava/net/URL;)V", False), ("([Ljava/net/URL;Ljava/lang/ClassLoader;Ljava/net/URLStreamHandlerFactory;)V", False)]
    getResourceAsStream = JavaMethod("(Ljava/lang/String;)Ljava/io/InputStream;")
    close = JavaMethod("()V")
    addURL = JavaMethod("(Ljava/net/URL;)V")
    getURLs = JavaMethod("()[Ljava/net/URL;")
    findClass = JavaMethod("(Ljava/lang/String;)Ljava/lang/Class;")
    definePackage = JavaMethod("(Ljava/lang/String;Ljava/util/jar/Manifest;Ljava/net/URL;)Ljava/lang/Package;")
    findResource = JavaMethod("(Ljava/lang/String;)Ljava/net/URL;")
    findResources = JavaMethod("(Ljava/lang/String;)Ljava/util/Enumeration;")
    getPermissions = JavaMethod("(Ljava/security/CodeSource;)Ljava/security/PermissionCollection;")
    newInstance = JavaMultipleMethod([("([Ljava/net/URL;Ljava/lang/ClassLoader;)Ljava/net/URLClassLoader;", True, False), ("([Ljava/net/URL;)Ljava/net/URLClassLoader;", True, False)])