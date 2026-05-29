from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Region"]

class Region(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Region"
    __javaconstructor__ = [("(Landroid/graphics/Rect;)V", False), ("()V", False), ("(Landroid/graphics/Region;)V", False), ("(IIII)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isComplex = JavaMethod("()Z")
    isRect = JavaMethod("()Z")
    quickContains = JavaMultipleMethod([("(IIII)Z", False, False), ("(Landroid/graphics/Rect;)Z", False, False)])
    getBoundaryPath = JavaMultipleMethod([("()Landroid/graphics/Path;", False, False), ("(Landroid/graphics/Path;)Z", False, False)])
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    isEmpty = JavaMethod("()Z")
    contains = JavaMethod("(II)Z")
    getBounds = JavaMultipleMethod([("(Landroid/graphics/Rect;)Z", False, False), ("()Landroid/graphics/Rect;", False, False)])
    set = JavaMultipleMethod([("(IIII)Z", False, False), ("(Landroid/graphics/Rect;)Z", False, False), ("(Landroid/graphics/Region;)Z", False, False)])
    op = JavaMultipleMethod([("(Landroid/graphics/Region;Landroid/graphics/Region$Op;)Z", False, False), ("(Landroid/graphics/Region;Landroid/graphics/Region;Landroid/graphics/Region$Op;)Z", False, False), ("(IIIILandroid/graphics/Region$Op;)Z", False, False), ("(Landroid/graphics/Rect;Landroid/graphics/Region$Op;)Z", False, False), ("(Landroid/graphics/Rect;Landroid/graphics/Region;Landroid/graphics/Region$Op;)Z", False, False)])
    quickReject = JavaMultipleMethod([("(Landroid/graphics/Region;)Z", False, False), ("(Landroid/graphics/Rect;)Z", False, False), ("(IIII)Z", False, False)])
    translate = JavaMultipleMethod([("(IILandroid/graphics/Region;)V", False, False), ("(II)V", False, False)])
    setEmpty = JavaMethod("()V")
    union = JavaMethod("(Landroid/graphics/Rect;)Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    setPath = JavaMethod("(Landroid/graphics/Path;Landroid/graphics/Region;)Z")

    class Op(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/Region$Op"
        DIFFERENCE = JavaStaticField("Landroid/graphics/Region$Op;")
        INTERSECT = JavaStaticField("Landroid/graphics/Region$Op;")
        REPLACE = JavaStaticField("Landroid/graphics/Region$Op;")
        REVERSE_DIFFERENCE = JavaStaticField("Landroid/graphics/Region$Op;")
        UNION = JavaStaticField("Landroid/graphics/Region$Op;")
        XOR = JavaStaticField("Landroid/graphics/Region$Op;")
        values = JavaStaticMethod("()[Landroid/graphics/Region$Op;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/graphics/Region$Op;")
        DIFFERENCE = JavaStaticField("Landroid/graphics/Region$Op;")
        INTERSECT = JavaStaticField("Landroid/graphics/Region$Op;")
        REPLACE = JavaStaticField("Landroid/graphics/Region$Op;")
        REVERSE_DIFFERENCE = JavaStaticField("Landroid/graphics/Region$Op;")
        UNION = JavaStaticField("Landroid/graphics/Region$Op;")
        XOR = JavaStaticField("Landroid/graphics/Region$Op;")