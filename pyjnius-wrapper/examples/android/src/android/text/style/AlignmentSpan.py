from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlignmentSpan"]

class AlignmentSpan(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/AlignmentSpan"
    getAlignment = JavaMethod("()Landroid/text/Layout$Alignment;")

    class Standard(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/style/AlignmentSpan/Standard"
        __javaconstructor__ = [("(Landroid/text/Layout$Alignment;)V", False), ("(Landroid/os/Parcel;)V", False)]
        getSpanTypeId = JavaMethod("()I")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        getAlignment = JavaMethod("()Landroid/text/Layout$Alignment;")
        toString = JavaMethod("()Ljava/lang/String;")