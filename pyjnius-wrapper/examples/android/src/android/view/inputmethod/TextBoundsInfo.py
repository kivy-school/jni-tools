from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextBoundsInfo"]

class TextBoundsInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/TextBoundsInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_CHARACTER_LINEFEED = JavaStaticField("I")
    FLAG_CHARACTER_PUNCTUATION = JavaStaticField("I")
    FLAG_CHARACTER_WHITESPACE = JavaStaticField("I")
    FLAG_LINE_IS_RTL = JavaStaticField("I")
    getMatrix = JavaMethod("(Landroid/graphics/Matrix;)V")
    getStartIndex = JavaMethod("()I")
    getEndIndex = JavaMethod("()I")
    getCharacterBounds = JavaMethod("(ILandroid/graphics/RectF;)V")
    getCharacterFlags = JavaMethod("(I)I")
    getCharacterBidiLevel = JavaMethod("(I)I")
    getWordSegmentFinder = JavaMethod("()Landroid/text/SegmentFinder;")
    getGraphemeSegmentFinder = JavaMethod("()Landroid/text/SegmentFinder;")
    getLineSegmentFinder = JavaMethod("()Landroid/text/SegmentFinder;")
    getOffsetForPosition = JavaMethod("(FF)I")
    getRangeForRect = JavaMethod("(Landroid/graphics/RectF;Landroid/text/SegmentFinder;Landroid/text/Layout$TextInclusionStrategy;)[I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/TextBoundsInfo/Builder"
        __javaconstructor__ = [("(II)V", False)]
        clear = JavaMethod("()Landroid/view/inputmethod/TextBoundsInfo$Builder;")
        setMatrix = JavaMethod("(Landroid/graphics/Matrix;)Landroid/view/inputmethod/TextBoundsInfo$Builder;")
        setStartAndEnd = JavaMethod("(II)Landroid/view/inputmethod/TextBoundsInfo$Builder;")
        setCharacterBounds = JavaMethod("([F)Landroid/view/inputmethod/TextBoundsInfo$Builder;")
        setCharacterFlags = JavaMethod("([I)Landroid/view/inputmethod/TextBoundsInfo$Builder;")
        setCharacterBidiLevel = JavaMethod("([I)Landroid/view/inputmethod/TextBoundsInfo$Builder;")
        setGraphemeSegmentFinder = JavaMethod("(Landroid/text/SegmentFinder;)Landroid/view/inputmethod/TextBoundsInfo$Builder;")
        setWordSegmentFinder = JavaMethod("(Landroid/text/SegmentFinder;)Landroid/view/inputmethod/TextBoundsInfo$Builder;")
        setLineSegmentFinder = JavaMethod("(Landroid/text/SegmentFinder;)Landroid/view/inputmethod/TextBoundsInfo$Builder;")
        build = JavaMethod("()Landroid/view/inputmethod/TextBoundsInfo;")