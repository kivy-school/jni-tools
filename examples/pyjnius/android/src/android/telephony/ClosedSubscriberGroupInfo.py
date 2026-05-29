from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClosedSubscriberGroupInfo"]

class ClosedSubscriberGroupInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/ClosedSubscriberGroupInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCsgIndicator = JavaMethod("()Z")
    getHomeNodebName = JavaMethod("()Ljava/lang/String;")
    getCsgIdentity = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")