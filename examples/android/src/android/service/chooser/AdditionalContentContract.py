from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdditionalContentContract"]

class AdditionalContentContract(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/chooser/AdditionalContentContract"

    class Columns(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/chooser/AdditionalContentContract/Columns"
        URI = JavaStaticField("Ljava/lang/String;")

    class CursorExtraKeys(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/chooser/AdditionalContentContract/CursorExtraKeys"
        POSITION = JavaStaticField("Ljava/lang/String;")

    class MethodNames(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/chooser/AdditionalContentContract/MethodNames"
        ON_SELECTION_CHANGED = JavaStaticField("Ljava/lang/String;")