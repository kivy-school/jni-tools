from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VisibleActivityInfo"]

class VisibleActivityInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/voice/VisibleActivityInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getActivityId = JavaMethod("()Landroid/service/voice/VoiceInteractionSession$ActivityId;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")