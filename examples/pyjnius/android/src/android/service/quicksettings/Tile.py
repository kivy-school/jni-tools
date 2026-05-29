from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Tile"]

class Tile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/quicksettings/Tile"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STATE_ACTIVE = JavaStaticField("I")
    STATE_INACTIVE = JavaStaticField("I")
    STATE_UNAVAILABLE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getActivityLaunchForClick = JavaMethod("()Landroid/app/PendingIntent;")
    setActivityLaunchForClick = JavaMethod("(Landroid/app/PendingIntent;)V")
    updateTile = JavaMethod("()V")
    getState = JavaMethod("()I")
    setState = JavaMethod("(I)V")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getContentDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getStateDescription = JavaMethod("()Ljava/lang/CharSequence;")
    setContentDescription = JavaMethod("(Ljava/lang/CharSequence;)V")
    setStateDescription = JavaMethod("(Ljava/lang/CharSequence;)V")
    setIcon = JavaMethod("(Landroid/graphics/drawable/Icon;)V")
    getSubtitle = JavaMethod("()Ljava/lang/CharSequence;")
    setSubtitle = JavaMethod("(Ljava/lang/CharSequence;)V")
    setLabel = JavaMethod("(Ljava/lang/CharSequence;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")