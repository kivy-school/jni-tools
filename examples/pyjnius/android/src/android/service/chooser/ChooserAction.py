from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChooserAction"]

class ChooserAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/chooser/ChooserAction"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getAction = JavaMethod("()Landroid/app/PendingIntent;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/chooser/ChooserAction/Builder"
        __javaconstructor__ = [("(Landroid/graphics/drawable/Icon;Ljava/lang/CharSequence;Landroid/app/PendingIntent;)V", False)]
        build = JavaMethod("()Landroid/service/chooser/ChooserAction;")