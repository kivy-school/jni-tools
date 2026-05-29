from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Insets"]

class Insets(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Insets"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    NONE = JavaStaticField("Landroid/graphics/Insets;")
    bottom = JavaField("I")
    left = JavaField("I")
    right = JavaField("I")
    top = JavaField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    subtract = JavaStaticMethod("(Landroid/graphics/Insets;Landroid/graphics/Insets;)Landroid/graphics/Insets;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    min = JavaStaticMethod("(Landroid/graphics/Insets;Landroid/graphics/Insets;)Landroid/graphics/Insets;")
    max = JavaStaticMethod("(Landroid/graphics/Insets;Landroid/graphics/Insets;)Landroid/graphics/Insets;")
    of = JavaMultipleMethod([("(IIII)Landroid/graphics/Insets;", True, False), ("(Landroid/graphics/Rect;)Landroid/graphics/Insets;", True, False)])
    add = JavaStaticMethod("(Landroid/graphics/Insets;Landroid/graphics/Insets;)Landroid/graphics/Insets;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")