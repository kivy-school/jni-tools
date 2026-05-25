from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JarURLConnection"]

class JarURLConnection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/JarURLConnection"
    __javaconstructor__ = [("(Ljava/net/URL;)V", False)]
    jarFileURLConnection = JavaField("Ljava/net/URLConnection;")
    getJarFileURL = JavaMethod("()Ljava/net/URL;")
    getEntryName = JavaMethod("()Ljava/lang/String;")
    getJarFile = JavaMethod("()Ljava/util/jar/JarFile;")
    getManifest = JavaMethod("()Ljava/util/jar/Manifest;")
    getJarEntry = JavaMethod("()Ljava/util/jar/JarEntry;")
    getAttributes = JavaMethod("()Ljava/util/jar/Attributes;")
    getMainAttributes = JavaMethod("()Ljava/util/jar/Attributes;")
    getCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")