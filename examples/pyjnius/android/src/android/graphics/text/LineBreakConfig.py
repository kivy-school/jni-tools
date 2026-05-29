from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LineBreakConfig"]

class LineBreakConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/text/LineBreakConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    HYPHENATION_DISABLED = JavaStaticField("I")
    HYPHENATION_ENABLED = JavaStaticField("I")
    HYPHENATION_UNSPECIFIED = JavaStaticField("I")
    LINE_BREAK_STYLE_AUTO = JavaStaticField("I")
    LINE_BREAK_STYLE_LOOSE = JavaStaticField("I")
    LINE_BREAK_STYLE_NONE = JavaStaticField("I")
    LINE_BREAK_STYLE_NORMAL = JavaStaticField("I")
    LINE_BREAK_STYLE_NO_BREAK = JavaStaticField("I")
    LINE_BREAK_STYLE_STRICT = JavaStaticField("I")
    LINE_BREAK_STYLE_UNSPECIFIED = JavaStaticField("I")
    LINE_BREAK_WORD_STYLE_AUTO = JavaStaticField("I")
    LINE_BREAK_WORD_STYLE_NONE = JavaStaticField("I")
    LINE_BREAK_WORD_STYLE_PHRASE = JavaStaticField("I")
    LINE_BREAK_WORD_STYLE_UNSPECIFIED = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getHyphenation = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    merge = JavaMethod("(Landroid/graphics/text/LineBreakConfig;)Landroid/graphics/text/LineBreakConfig;")
    getLineBreakStyle = JavaMethod("()I")
    getLineBreakWordStyle = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/graphics/text/LineBreakConfig$Builder"
        __javaconstructor__ = [("()V", False)]
        setHyphenation = JavaMethod("(I)Landroid/graphics/text/LineBreakConfig$Builder;")
        merge = JavaMethod("(Landroid/graphics/text/LineBreakConfig;)Landroid/graphics/text/LineBreakConfig$Builder;")
        build = JavaMethod("()Landroid/graphics/text/LineBreakConfig;")
        setLineBreakStyle = JavaMethod("(I)Landroid/graphics/text/LineBreakConfig$Builder;")
        setLineBreakWordStyle = JavaMethod("(I)Landroid/graphics/text/LineBreakConfig$Builder;")