from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChooserAction"]

class ChooserAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/chooser/ChooserAction"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getAction = JavaMethod("()Landroid/app/PendingIntent;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/chooser/ChooserAction$Builder"
        __javaconstructor__ = [("(Landroid/graphics/drawable/Icon;Ljava/lang/CharSequence;Landroid/app/PendingIntent;)V", False)]
        build = JavaMethod("()Landroid/service/chooser/ChooserAction;")