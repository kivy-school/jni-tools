from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ControlButton"]

class ControlButton(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/templates/ControlButton"
    __javaconstructor__ = [("(ZLjava/lang/CharSequence;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    isChecked = JavaMethod("()Z")
    getActionDescription = JavaMethod("()Ljava/lang/CharSequence;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")