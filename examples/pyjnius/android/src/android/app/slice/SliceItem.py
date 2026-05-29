from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSlice = JavaMethod("()Landroid/app/slice/Slice;")
    getHints = JavaMethod("()Ljava/util/List;")
    getRemoteInput = JavaMethod("()Landroid/app/RemoteInput;")
    hasHint = JavaMethod("(Ljava/lang/String;)Z")
    getSubType = JavaMethod("()Ljava/lang/String;")
    getInt = JavaMethod("()I")
    getLong = JavaMethod("()J")
    getAction = JavaMethod("()Landroid/app/PendingIntent;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getBundle = JavaMethod("()Landroid/os/Bundle;")
    describeContents = JavaMethod("()I")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getText = JavaMethod("()Ljava/lang/CharSequence;")
    getFormat = JavaMethod("()Ljava/lang/String;")