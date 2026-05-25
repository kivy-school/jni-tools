from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SavedDatasetsInfoCallback"]

class SavedDatasetsInfoCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/SavedDatasetsInfoCallback"
    ERROR_NEEDS_USER_ACTION = JavaStaticField("I")
    ERROR_OTHER = JavaStaticField("I")
    ERROR_UNSUPPORTED = JavaStaticField("I")
    onSuccess = JavaMethod("(Ljava/util/Set;)V")
    onError = JavaMethod("(I)V")