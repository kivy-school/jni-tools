from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoteAction"]

class RemoteAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/RemoteAction"
    __javaconstructor__ = [("(Landroid/graphics/drawable/Icon;Ljava/lang/CharSequence;Ljava/lang/CharSequence;Landroid/app/PendingIntent;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    setShouldShowIcon = JavaMethod("(Z)V")
    shouldShowIcon = JavaMethod("()Z")
    getActionIntent = JavaMethod("()Landroid/app/PendingIntent;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    clone = JavaMultipleMethod([("()Landroid/app/RemoteAction;", False, False), ("()Ljava/lang/Object;", False, False)])
    isEnabled = JavaMethod("()Z")
    dump = JavaMethod("(Ljava/lang/String;Ljava/io/PrintWriter;)V")
    getContentDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    setEnabled = JavaMethod("(Z)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")