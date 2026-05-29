from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChooserTarget"]

class ChooserTarget(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/chooser/ChooserTarget"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;Landroid/graphics/drawable/Icon;FLandroid/content/ComponentName;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getIntentExtras = JavaMethod("()Landroid/os/Bundle;")
    toString = JavaMethod("()Ljava/lang/String;")
    getScore = JavaMethod("()F")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getComponentName = JavaMethod("()Landroid/content/ComponentName;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")