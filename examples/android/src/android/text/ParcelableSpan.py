from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParcelableSpan"]

class ParcelableSpan(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/ParcelableSpan"
    getSpanTypeId = JavaMethod("()I")