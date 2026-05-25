from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Insets"]

class Insets(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Insets"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    NONE = JavaStaticField("Landroid/graphics/Insets;")
    bottom = JavaField("I")
    left = JavaField("I")
    right = JavaField("I")
    top = JavaField("I")
    of = JavaMultipleMethod([("(IIII)Landroid/graphics/Insets;", True, False), ("(Landroid/graphics/Rect;)Landroid/graphics/Insets;", True, False)])
    add = JavaStaticMethod("(Landroid/graphics/Insets;Landroid/graphics/Insets;)Landroid/graphics/Insets;")
    subtract = JavaStaticMethod("(Landroid/graphics/Insets;Landroid/graphics/Insets;)Landroid/graphics/Insets;")
    max = JavaStaticMethod("(Landroid/graphics/Insets;Landroid/graphics/Insets;)Landroid/graphics/Insets;")
    min = JavaStaticMethod("(Landroid/graphics/Insets;Landroid/graphics/Insets;)Landroid/graphics/Insets;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")