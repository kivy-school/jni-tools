from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoteAction"]

class RemoteAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/RemoteAction"
    __javaconstructor__ = [("(Landroid/graphics/drawable/Icon;Ljava/lang/CharSequence;Ljava/lang/CharSequence;Landroid/app/PendingIntent;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    setEnabled = JavaMethod("(Z)V")
    isEnabled = JavaMethod("()Z")
    setShouldShowIcon = JavaMethod("(Z)V")
    shouldShowIcon = JavaMethod("()Z")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getContentDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getActionIntent = JavaMethod("()Landroid/app/PendingIntent;")
    clone = JavaMethod("()Landroid/app/RemoteAction;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    dump = JavaMethod("(Ljava/lang/String;Ljava/io/PrintWriter;)V")