from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Tile"]

class Tile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/quicksettings/Tile"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STATE_ACTIVE = JavaStaticField("I")
    STATE_INACTIVE = JavaStaticField("I")
    STATE_UNAVAILABLE = JavaStaticField("I")
    getState = JavaMethod("()I")
    setState = JavaMethod("(I)V")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")
    setIcon = JavaMethod("(Landroid/graphics/drawable/Icon;)V")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    setLabel = JavaMethod("(Ljava/lang/CharSequence;)V")
    getSubtitle = JavaMethod("()Ljava/lang/CharSequence;")
    setSubtitle = JavaMethod("(Ljava/lang/CharSequence;)V")
    getContentDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getStateDescription = JavaMethod("()Ljava/lang/CharSequence;")
    setContentDescription = JavaMethod("(Ljava/lang/CharSequence;)V")
    setStateDescription = JavaMethod("(Ljava/lang/CharSequence;)V")
    describeContents = JavaMethod("()I")
    updateTile = JavaMethod("()V")
    getActivityLaunchForClick = JavaMethod("()Landroid/app/PendingIntent;")
    setActivityLaunchForClick = JavaMethod("(Landroid/app/PendingIntent;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")