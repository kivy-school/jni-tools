from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SliceItem"]

class SliceItem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/slice/SliceItem"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FORMAT_ACTION = JavaStaticField("Ljava/lang/String;")
    FORMAT_BUNDLE = JavaStaticField("Ljava/lang/String;")
    FORMAT_IMAGE = JavaStaticField("Ljava/lang/String;")
    FORMAT_INT = JavaStaticField("Ljava/lang/String;")
    FORMAT_LONG = JavaStaticField("Ljava/lang/String;")
    FORMAT_REMOTE_INPUT = JavaStaticField("Ljava/lang/String;")
    FORMAT_SLICE = JavaStaticField("Ljava/lang/String;")
    FORMAT_TEXT = JavaStaticField("Ljava/lang/String;")
    getHints = JavaMethod("()Ljava/util/List;")
    getFormat = JavaMethod("()Ljava/lang/String;")
    getSubType = JavaMethod("()Ljava/lang/String;")
    getText = JavaMethod("()Ljava/lang/CharSequence;")
    getBundle = JavaMethod("()Landroid/os/Bundle;")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getAction = JavaMethod("()Landroid/app/PendingIntent;")
    getRemoteInput = JavaMethod("()Landroid/app/RemoteInput;")
    getInt = JavaMethod("()I")
    getSlice = JavaMethod("()Landroid/app/slice/Slice;")
    getLong = JavaMethod("()J")
    hasHint = JavaMethod("(Ljava/lang/String;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")