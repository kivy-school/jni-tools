from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaSyncEvent"]

class MediaSyncEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaSyncEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SYNC_EVENT_NONE = JavaStaticField("I")
    SYNC_EVENT_PRESENTATION_COMPLETE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    setAudioSessionId = JavaMethod("(I)Landroid/media/MediaSyncEvent;")
    createEvent = JavaStaticMethod("(I)Landroid/media/MediaSyncEvent;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getType = JavaMethod("()I")
    getAudioSessionId = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")