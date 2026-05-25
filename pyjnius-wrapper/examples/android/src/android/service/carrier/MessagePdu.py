from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MessagePdu"]

class MessagePdu(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/carrier/MessagePdu"
    __javaconstructor__ = [("(Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getPdus = JavaMethod("()Ljava/util/List;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")