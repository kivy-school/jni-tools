from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["EasyEditSpan"]

class EasyEditSpan(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/style/EasyEditSpan"
    __javaconstructor__ = [("()V", False), ("(Landroid/app/PendingIntent;)V", False), ("(Landroid/os/Parcel;)V", False)]
    EXTRA_TEXT_CHANGED_TYPE = JavaStaticField("Ljava/lang/String;")
    TEXT_DELETED = JavaStaticField("I")
    TEXT_MODIFIED = JavaStaticField("I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getSpanTypeId = JavaMethod("()I")