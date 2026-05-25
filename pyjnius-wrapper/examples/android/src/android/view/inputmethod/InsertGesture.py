from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InsertGesture"]

class InsertGesture(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InsertGesture"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTextToInsert = JavaMethod("()Ljava/lang/String;")
    getInsertionPoint = JavaMethod("()Landroid/graphics/PointF;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/InsertGesture/Builder"
        __javaconstructor__ = [("()V", False)]
        setTextToInsert = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/InsertGesture$Builder;")
        setInsertionPoint = JavaMethod("(Landroid/graphics/PointF;)Landroid/view/inputmethod/InsertGesture$Builder;")
        setFallbackText = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/InsertGesture$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/InsertGesture;")