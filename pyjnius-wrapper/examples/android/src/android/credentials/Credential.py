from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Credential"]

class Credential(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/credentials/Credential"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    TYPE_PASSWORD_CREDENTIAL = JavaStaticField("Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")
    getData = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")