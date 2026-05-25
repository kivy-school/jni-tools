from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DrmInfo"]

class DrmInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/DrmInfo"
    __javaconstructor__ = [("(I[BLjava/lang/String;)V", False), ("(ILjava/lang/String;Ljava/lang/String;)V", False)]
    put = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")
    get = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    keyIterator = JavaMethod("()Ljava/util/Iterator;")
    iterator = JavaMethod("()Ljava/util/Iterator;")
    getData = JavaMethod("()[B")
    getMimeType = JavaMethod("()Ljava/lang/String;")
    getInfoType = JavaMethod("()I")