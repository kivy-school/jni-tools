from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DomainVerificationUserState"]

class DomainVerificationUserState(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/verify/domain/DomainVerificationUserState"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    DOMAIN_STATE_NONE = JavaStaticField("I")
    DOMAIN_STATE_SELECTED = JavaStaticField("I")
    DOMAIN_STATE_VERIFIED = JavaStaticField("I")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getUser = JavaMethod("()Landroid/os/UserHandle;")
    isLinkHandlingAllowed = JavaMethod("()Z")
    getHostToStateMap = JavaMethod("()Ljava/util/Map;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")