from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdditionalContentContract"]

class AdditionalContentContract(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/chooser/AdditionalContentContract"

    class MethodNames(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/chooser/AdditionalContentContract$MethodNames"
        ON_SELECTION_CHANGED = JavaStaticField("Ljava/lang/String;")

    class CursorExtraKeys(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/chooser/AdditionalContentContract$CursorExtraKeys"
        POSITION = JavaStaticField("Ljava/lang/String;")

    class Columns(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/chooser/AdditionalContentContract$Columns"
        URI = JavaStaticField("Ljava/lang/String;")