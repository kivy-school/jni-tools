from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResultReceiver"]

class ResultReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/ResultReceiver"
    __javaconstructor__ = [("(Landroid/os/Handler;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    send = JavaMethod("(ILandroid/os/Bundle;)V")
    onReceiveResult = JavaMethod("(ILandroid/os/Bundle;)V")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")