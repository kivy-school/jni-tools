from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AuthenticatorDescription"]

class AuthenticatorDescription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accounts/AuthenticatorDescription"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;IIII)V", False), ("(Ljava/lang/String;Ljava/lang/String;IIIIZ)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    accountPreferencesId = JavaField("I")
    customTokens = JavaField("Z")
    iconId = JavaField("I")
    labelId = JavaField("I")
    packageName = JavaField("Ljava/lang/String;")
    smallIconId = JavaField("I")
    type = JavaField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    newKey = JavaStaticMethod("(Ljava/lang/String;)Landroid/accounts/AuthenticatorDescription;")