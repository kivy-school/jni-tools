from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmSupportInfo"]

class DrmSupportInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmSupportInfo"
    __javaconstructor__ = [("()V", False)]
    addMimeType = JavaMethod("(Ljava/lang/String;)V")
    addFileSuffix = JavaMethod("(Ljava/lang/String;)V")
    getMimeTypeIterator = JavaMethod("()Ljava/util/Iterator;")
    getFileSuffixIterator = JavaMethod("()Ljava/util/Iterator;")
    setDescription = JavaMethod("(Ljava/lang/String;)V")
    getDescriprition = JavaMethod("()Ljava/lang/String;")
    getDescription = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")