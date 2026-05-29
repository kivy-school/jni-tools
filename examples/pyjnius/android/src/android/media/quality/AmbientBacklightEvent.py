from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AmbientBacklightEvent"]

class AmbientBacklightEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/quality/AmbientBacklightEvent"
    __javaconstructor__ = [("(ILandroid/media/quality/AmbientBacklightMetadata;)V", False)]
    AMBIENT_BACKLIGHT_EVENT_DISABLED = JavaStaticField("I")
    AMBIENT_BACKLIGHT_EVENT_ENABLED = JavaStaticField("I")
    AMBIENT_BACKLIGHT_EVENT_INTERRUPTED = JavaStaticField("I")
    AMBIENT_BACKLIGHT_EVENT_METADATA_AVAILABLE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getMetadata = JavaMethod("()Landroid/media/quality/AmbientBacklightMetadata;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getEventType = JavaMethod("()I")