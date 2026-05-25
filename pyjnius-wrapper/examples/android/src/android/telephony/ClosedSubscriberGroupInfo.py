from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClosedSubscriberGroupInfo"]

class ClosedSubscriberGroupInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ClosedSubscriberGroupInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getCsgIndicator = JavaMethod("()Z")
    getHomeNodebName = JavaMethod("()Ljava/lang/String;")
    getCsgIdentity = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")