from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DomainVerificationUserState"]

class DomainVerificationUserState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/verify/domain/DomainVerificationUserState"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DOMAIN_STATE_NONE = JavaStaticField("I")
    DOMAIN_STATE_SELECTED = JavaStaticField("I")
    DOMAIN_STATE_VERIFIED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getUser = JavaMethod("()Landroid/os/UserHandle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getHostToStateMap = JavaMethod("()Ljava/util/Map;")
    isLinkHandlingAllowed = JavaMethod("()Z")