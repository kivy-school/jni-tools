from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Annotation"]

class Annotation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/Annotation"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False), ("(Ljava/lang/String;Ljava/lang/String;)V", False)]
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getValue = JavaMethod("()Ljava/lang/String;")
    getKey = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSpanTypeId = JavaMethod("()I")