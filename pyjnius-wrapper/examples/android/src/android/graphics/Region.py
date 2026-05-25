from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Region"]

class Region(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Region"
    __javaconstructor__ = [("()V", False), ("(Landroid/graphics/Region;)V", False), ("(Landroid/graphics/Rect;)V", False), ("(IIII)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    setEmpty = JavaMethod("()V")
    set = JavaMultipleMethod([("(Landroid/graphics/Region;)Z", False, False), ("(Landroid/graphics/Rect;)Z", False, False), ("(IIII)Z", False, False)])
    setPath = JavaMethod("(Landroid/graphics/Path;Landroid/graphics/Region;)Z")
    isEmpty = JavaMethod("()Z")
    isRect = JavaMethod("()Z")
    isComplex = JavaMethod("()Z")
    getBounds = JavaMultipleMethod([("()Landroid/graphics/Rect;", False, False), ("(Landroid/graphics/Rect;)Z", False, False)])
    getBoundaryPath = JavaMultipleMethod([("()Landroid/graphics/Path;", False, False), ("(Landroid/graphics/Path;)Z", False, False)])
    contains = JavaMethod("(II)Z")
    quickContains = JavaMultipleMethod([("(Landroid/graphics/Rect;)Z", False, False), ("(IIII)Z", False, False)])
    quickReject = JavaMultipleMethod([("(Landroid/graphics/Rect;)Z", False, False), ("(IIII)Z", False, False), ("(Landroid/graphics/Region;)Z", False, False)])
    translate = JavaMultipleMethod([("(II)V", False, False), ("(IILandroid/graphics/Region;)V", False, False)])
    union = JavaMethod("(Landroid/graphics/Rect;)Z")
    op = JavaMultipleMethod([("(Landroid/graphics/Rect;Landroid/graphics/Region$Op;)Z", False, False), ("(IIIILandroid/graphics/Region$Op;)Z", False, False), ("(Landroid/graphics/Region;Landroid/graphics/Region$Op;)Z", False, False), ("(Landroid/graphics/Rect;Landroid/graphics/Region;Landroid/graphics/Region$Op;)Z", False, False), ("(Landroid/graphics/Region;Landroid/graphics/Region;Landroid/graphics/Region$Op;)Z", False, False)])
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    finalize = JavaMethod("()V")

    class Op(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/Region/Op"
        values = JavaStaticMethod("()[Landroid/graphics/Region$Op;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/graphics/Region$Op;")
        DIFFERENCE = JavaStaticField("Landroid/graphics/Region/Op;")
        INTERSECT = JavaStaticField("Landroid/graphics/Region/Op;")
        UNION = JavaStaticField("Landroid/graphics/Region/Op;")
        XOR = JavaStaticField("Landroid/graphics/Region/Op;")
        REVERSE_DIFFERENCE = JavaStaticField("Landroid/graphics/Region/Op;")
        REPLACE = JavaStaticField("Landroid/graphics/Region/Op;")