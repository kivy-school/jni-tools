from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResultReceiver"]

class ResultReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/ResultReceiver"
    __javaconstructor__ = [("(Landroid/os/Handler;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    send = JavaMethod("(ILandroid/os/Bundle;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")