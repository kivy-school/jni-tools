from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RectF"]

class RectF(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/RectF"
    __javaconstructor__ = [("()V", False), ("(FFFF)V", False), ("(Landroid/graphics/RectF;)V", False), ("(Landroid/graphics/Rect;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    bottom = JavaField("F")
    left = JavaField("F")
    right = JavaField("F")
    top = JavaField("F")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    toShortString = JavaMethod("()Ljava/lang/String;")
    isEmpty = JavaMethod("()Z")
    width = JavaMethod("()F")
    height = JavaMethod("()F")
    centerX = JavaMethod("()F")
    centerY = JavaMethod("()F")
    setEmpty = JavaMethod("()V")
    set = JavaMultipleMethod([("(FFFF)V", False, False), ("(Landroid/graphics/RectF;)V", False, False), ("(Landroid/graphics/Rect;)V", False, False)])
    offset = JavaMethod("(FF)V")
    offsetTo = JavaMethod("(FF)V")
    inset = JavaMethod("(FF)V")
    contains = JavaMultipleMethod([("(FF)Z", False, False), ("(FFFF)Z", False, False), ("(Landroid/graphics/RectF;)Z", False, False)])
    intersect = JavaMultipleMethod([("(FFFF)Z", False, False), ("(Landroid/graphics/RectF;)Z", False, False)])
    setIntersect = JavaMethod("(Landroid/graphics/RectF;Landroid/graphics/RectF;)Z")
    intersects = JavaMultipleMethod([("(FFFF)Z", False, False), ("(Landroid/graphics/RectF;Landroid/graphics/RectF;)Z", True, False)])
    round = JavaMethod("(Landroid/graphics/Rect;)V")
    roundOut = JavaMethod("(Landroid/graphics/Rect;)V")
    union = JavaMultipleMethod([("(FFFF)V", False, False), ("(Landroid/graphics/RectF;)V", False, False), ("(FF)V", False, False)])
    sort = JavaMethod("()V")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    readFromParcel = JavaMethod("(Landroid/os/Parcel;)V")