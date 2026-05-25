from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChooserTarget"]

class ChooserTarget(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/chooser/ChooserTarget"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;Landroid/graphics/drawable/Icon;FLandroid/content/ComponentName;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getScore = JavaMethod("()F")
    getComponentName = JavaMethod("()Landroid/content/ComponentName;")
    getIntentExtras = JavaMethod("()Landroid/os/Bundle;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")