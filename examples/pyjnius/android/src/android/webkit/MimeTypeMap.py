from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MimeTypeMap"]

class MimeTypeMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/MimeTypeMap"
    hasExtension = JavaMethod("(Ljava/lang/String;)Z")
    getSingleton = JavaStaticMethod("()Landroid/webkit/MimeTypeMap;")
    getExtensionFromMimeType = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getFileExtensionFromUrl = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getMimeTypeFromExtension = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    hasMimeType = JavaMethod("(Ljava/lang/String;)Z")