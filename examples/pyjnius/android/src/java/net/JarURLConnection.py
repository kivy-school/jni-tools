from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JarURLConnection"]

class JarURLConnection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/net/JarURLConnection"
    getCertificates = JavaMethod("()[Ljava/security/cert/Certificate;")
    getMainAttributes = JavaMethod("()Ljava/util/jar/Attributes;")
    getAttributes = JavaMethod("()Ljava/util/jar/Attributes;")
    getManifest = JavaMethod("()Ljava/util/jar/Manifest;")
    getJarFileURL = JavaMethod("()Ljava/net/URL;")
    getJarEntry = JavaMethod("()Ljava/util/jar/JarEntry;")
    getEntryName = JavaMethod("()Ljava/lang/String;")
    getJarFile = JavaMethod("()Ljava/util/jar/JarFile;")