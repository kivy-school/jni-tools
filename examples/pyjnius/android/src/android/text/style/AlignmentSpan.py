from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlignmentSpan"]

class AlignmentSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/AlignmentSpan"
    getAlignment = JavaMethod("()Landroid/text/Layout$Alignment;")

    class Standard(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/style/AlignmentSpan$Standard"
        __javaconstructor__ = [("(Landroid/os/Parcel;)V", False), ("(Landroid/text/Layout$Alignment;)V", False)]
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        toString = JavaMethod("()Ljava/lang/String;")
        getAlignment = JavaMethod("()Landroid/text/Layout$Alignment;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getSpanTypeId = JavaMethod("()I")