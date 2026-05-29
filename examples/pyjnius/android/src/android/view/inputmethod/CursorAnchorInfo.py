from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CursorAnchorInfo"]

class CursorAnchorInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/CursorAnchorInfo"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_HAS_INVISIBLE_REGION = JavaStaticField("I")
    FLAG_HAS_VISIBLE_REGION = JavaStaticField("I")
    FLAG_IS_RTL = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getComposingText = JavaMethod("()Ljava/lang/CharSequence;")
    getCharacterBounds = JavaMethod("(I)Landroid/graphics/RectF;")
    getCharacterBoundsFlags = JavaMethod("(I)I")
    getComposingTextStart = JavaMethod("()I")
    getEditorBoundsInfo = JavaMethod("()Landroid/view/inputmethod/EditorBoundsInfo;")
    getInsertionMarkerBaseline = JavaMethod("()F")
    getInsertionMarkerBottom = JavaMethod("()F")
    getInsertionMarkerFlags = JavaMethod("()I")
    getInsertionMarkerHorizontal = JavaMethod("()F")
    getInsertionMarkerTop = JavaMethod("()F")
    getTextAppearanceInfo = JavaMethod("()Landroid/view/inputmethod/TextAppearanceInfo;")
    getVisibleLineBounds = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getMatrix = JavaMethod("()Landroid/graphics/Matrix;")
    getSelectionEnd = JavaMethod("()I")
    getSelectionStart = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/CursorAnchorInfo$Builder"
        __javaconstructor__ = [("()V", False)]
        addCharacterBounds = JavaMethod("(IFFFFI)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        addVisibleLineBounds = JavaMethod("(FFFF)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        clearVisibleLineBounds = JavaMethod("()Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        setEditorBoundsInfo = JavaMethod("(Landroid/view/inputmethod/EditorBoundsInfo;)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        setInsertionMarkerLocation = JavaMethod("(FFFFI)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        setSelectionRange = JavaMethod("(II)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        setTextAppearanceInfo = JavaMethod("(Landroid/view/inputmethod/TextAppearanceInfo;)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        reset = JavaMethod("()V")
        setMatrix = JavaMethod("(Landroid/graphics/Matrix;)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        setComposingText = JavaMethod("(ILjava/lang/CharSequence;)Landroid/view/inputmethod/CursorAnchorInfo$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/CursorAnchorInfo;")