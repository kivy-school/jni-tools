from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LabeledIntent"]

class LabeledIntent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/pm/LabeledIntent"
    __javaconstructor__ = [("(Landroid/content/Intent;Ljava/lang/String;II)V", False), ("(Landroid/content/Intent;Ljava/lang/String;Ljava/lang/CharSequence;I)V", False), ("(Ljava/lang/String;II)V", False), ("(Ljava/lang/String;Ljava/lang/CharSequence;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getSourcePackage = JavaMethod("()Ljava/lang/String;")
    getLabelResource = JavaMethod("()I")
    getNonLocalizedLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getIconResource = JavaMethod("()I")
    loadLabel = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    loadIcon = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    readFromParcel = JavaMethod("(Landroid/os/Parcel;)V")