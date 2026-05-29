from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SavedDatasetsInfoCallback"]

class SavedDatasetsInfoCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/SavedDatasetsInfoCallback"
    ERROR_NEEDS_USER_ACTION = JavaStaticField("I")
    ERROR_OTHER = JavaStaticField("I")
    ERROR_UNSUPPORTED = JavaStaticField("I")
    onError = JavaMethod("(I)V")
    onSuccess = JavaMethod("(Ljava/util/Set;)V")