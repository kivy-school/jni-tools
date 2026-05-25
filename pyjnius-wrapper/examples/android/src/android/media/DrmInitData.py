from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmInitData"]

class DrmInitData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/DrmInitData"
    get = JavaMethod("(Ljava/util/UUID;)Landroid/media/DrmInitData$SchemeInitData;")
    getSchemeInitDataCount = JavaMethod("()I")
    getSchemeInitDataAt = JavaMethod("(I)Landroid/media/DrmInitData$SchemeInitData;")

    class SchemeInitData(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/DrmInitData/SchemeInitData"
        __javaconstructor__ = [("(Ljava/util/UUID;Ljava/lang/String;[B)V", False)]
        UUID_NIL = JavaStaticField("Ljava/util/UUID;")
        data = JavaField("[B")
        mimeType = JavaField("Ljava/lang/String;")
        uuid = JavaField("Ljava/util/UUID;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")