from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClearCredentialStateRequest"]

class ClearCredentialStateRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/ClearCredentialStateRequest"
    __javaconstructor__ = [("(Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getData = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")