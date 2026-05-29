from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AconfigPackage"]

class AconfigPackage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/flagging/AconfigPackage"
    load = JavaStaticMethod("(Ljava/lang/String;)Landroid/os/flagging/AconfigPackage;")
    getBooleanFlagValue = JavaMethod("(Ljava/lang/String;Z)Z")