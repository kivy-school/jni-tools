from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MimeTypeMap"]

class MimeTypeMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/MimeTypeMap"
    getFileExtensionFromUrl = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    hasMimeType = JavaMethod("(Ljava/lang/String;)Z")
    getMimeTypeFromExtension = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    hasExtension = JavaMethod("(Ljava/lang/String;)Z")
    getExtensionFromMimeType = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getSingleton = JavaStaticMethod("()Landroid/webkit/MimeTypeMap;")