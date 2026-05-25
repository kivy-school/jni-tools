from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OSInAppMessagePageKt"]

class OSInAppMessagePageKt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/OSInAppMessagePageKt"
    PAGE_ID = JavaStaticField("Ljava/lang/String;")
    PAGE_INDEX = JavaStaticField("Ljava/lang/String;")