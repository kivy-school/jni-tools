from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParcelablePeerHandle"]

class ParcelablePeerHandle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/ParcelablePeerHandle"
    __javaconstructor__ = [("(Landroid/net/wifi/aware/PeerHandle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")