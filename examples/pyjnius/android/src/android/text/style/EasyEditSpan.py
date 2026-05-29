from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EasyEditSpan"]

class EasyEditSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/EasyEditSpan"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False), ("(Landroid/app/PendingIntent;)V", False), ("()V", False)]
    EXTRA_TEXT_CHANGED_TYPE = JavaStaticField("Ljava/lang/String;")
    TEXT_DELETED = JavaStaticField("I")
    TEXT_MODIFIED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSpanTypeId = JavaMethod("()I")