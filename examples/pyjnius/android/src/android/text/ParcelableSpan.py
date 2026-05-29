from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParcelableSpan"]

class ParcelableSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/ParcelableSpan"
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSpanTypeId = JavaMethod("()I")