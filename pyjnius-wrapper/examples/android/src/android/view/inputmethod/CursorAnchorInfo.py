from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CursorAnchorInfo"]

class CursorAnchorInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/CursorAnchorInfo"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_HAS_INVISIBLE_REGION = JavaStaticField("I")
    FLAG_HAS_VISIBLE_REGION = JavaStaticField("I")
    FLAG_IS_RTL = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    getSelectionStart = JavaMethod("()I")
    getSelectionEnd = JavaMethod("()I")
    getComposingTextStart = JavaMethod("()I")
    getComposingText = JavaMethod("()Ljava/lang/CharSequence;")
    getInsertionMarkerFlags = JavaMethod("()I")
    getInsertionMarkerHorizontal = JavaMethod("()F")
    getInsertionMarkerTop = JavaMethod("()F")
    getInsertionMarkerBaseline = JavaMethod("()F")
    getInsertionMarkerBottom = JavaMethod("()F")
    getCharacterBounds = JavaMethod("(I)Landroid/graphics/RectF;")
    getCharacterBoundsFlags = JavaMethod("(I)I")
    getVisibleLineBounds = JavaMethod("()Ljava/util/List;")
    getEditorBoundsInfo = JavaMethod("()Landroid/view/inputmethod/EditorBoundsInfo;")
    getTextAppearanceInfo = JavaMethod("()Landroid/view/inputmethod/TextAppearanceInfo;")
    getMatrix = JavaMethod("()Landroid/graphics/Matrix;")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/CursorAnchorInfo/Builder"
        __javaconstructor__ = [("()V", False)]
        setSelectionRange = JavaMethod("(II)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        setComposingText = JavaMethod("(ILjava/lang/CharSequence;)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        setInsertionMarkerLocation = JavaMethod("(FFFFI)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        addCharacterBounds = JavaMethod("(IFFFFI)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        setEditorBoundsInfo = JavaMethod("(Landroid/view/inputmethod/EditorBoundsInfo;)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        setMatrix = JavaMethod("(Landroid/graphics/Matrix;)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        setTextAppearanceInfo = JavaMethod("(Landroid/view/inputmethod/TextAppearanceInfo;)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        addVisibleLineBounds = JavaMethod("(FFFF)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        clearVisibleLineBounds = JavaMethod("()Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/CursorAnchorInfo;")
        reset = JavaMethod("()V")