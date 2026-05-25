from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QuickViewConstants"]

class QuickViewConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/QuickViewConstants"
    FEATURE_DELETE = JavaStaticField("Ljava/lang/String;")
    FEATURE_DOWNLOAD = JavaStaticField("Ljava/lang/String;")
    FEATURE_EDIT = JavaStaticField("Ljava/lang/String;")
    FEATURE_PRINT = JavaStaticField("Ljava/lang/String;")
    FEATURE_SEND = JavaStaticField("Ljava/lang/String;")
    FEATURE_VIEW = JavaStaticField("Ljava/lang/String;")