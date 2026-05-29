from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BaseColumns"]

class BaseColumns(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/BaseColumns"
    _COUNT = JavaStaticField("Ljava/lang/String;")
    _ID = JavaStaticField("Ljava/lang/String;")