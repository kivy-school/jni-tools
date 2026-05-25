from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ColorStateList"]

class ColorStateList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/ColorStateList"
    __javaconstructor__ = [("([[I[I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    valueOf = JavaStaticMethod("(I)Landroid/content/res/ColorStateList;")
    createFromXml = JavaMultipleMethod([("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;)Landroid/content/res/ColorStateList;", True, False), ("(Landroid/content/res/Resources;Lorg/xmlpull/v1/XmlPullParser;Landroid/content/res/Resources$Theme;)Landroid/content/res/ColorStateList;", True, False)])
    withAlpha = JavaMethod("(I)Landroid/content/res/ColorStateList;")
    withLStar = JavaMethod("(F)Landroid/content/res/ColorStateList;")
    getChangingConfigurations = JavaMethod("()I")
    isStateful = JavaMethod("()Z")
    isOpaque = JavaMethod("()Z")
    getColorForState = JavaMethod("([II)I")
    getDefaultColor = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")