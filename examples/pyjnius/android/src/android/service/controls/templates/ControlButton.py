from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ControlButton"]

class ControlButton(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/templates/ControlButton"
    __javaconstructor__ = [("(ZLjava/lang/CharSequence;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getActionDescription = JavaMethod("()Ljava/lang/CharSequence;")
    isChecked = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")