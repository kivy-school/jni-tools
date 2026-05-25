from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaSyncEvent"]

class MediaSyncEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaSyncEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SYNC_EVENT_NONE = JavaStaticField("I")
    SYNC_EVENT_PRESENTATION_COMPLETE = JavaStaticField("I")
    createEvent = JavaStaticMethod("(I)Landroid/media/MediaSyncEvent;")
    setAudioSessionId = JavaMethod("(I)Landroid/media/MediaSyncEvent;")
    getType = JavaMethod("()I")
    getAudioSessionId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")