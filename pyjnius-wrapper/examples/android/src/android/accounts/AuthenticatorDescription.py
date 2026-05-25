from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AuthenticatorDescription"]

class AuthenticatorDescription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accounts/AuthenticatorDescription"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;IIIIZ)V", False), ("(Ljava/lang/String;Ljava/lang/String;IIII)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    accountPreferencesId = JavaField("I")
    customTokens = JavaField("Z")
    iconId = JavaField("I")
    labelId = JavaField("I")
    packageName = JavaField("Ljava/lang/String;")
    smallIconId = JavaField("I")
    type = JavaField("Ljava/lang/String;")
    newKey = JavaStaticMethod("(Ljava/lang/String;)Landroid/accounts/AuthenticatorDescription;")
    describeContents = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")