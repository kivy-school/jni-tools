from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextUtils"]

class TextUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/TextUtils"
    CAP_MODE_CHARACTERS = JavaStaticField("I")
    CAP_MODE_SENTENCES = JavaStaticField("I")
    CAP_MODE_WORDS = JavaStaticField("I")
    CHAR_SEQUENCE_CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SAFE_STRING_FLAG_FIRST_LINE = JavaStaticField("I")
    SAFE_STRING_FLAG_SINGLE_LINE = JavaStaticField("I")
    SAFE_STRING_FLAG_TRIM = JavaStaticField("I")
    ellipsize = JavaMultipleMethod([("(Ljava/lang/CharSequence;Landroid/text/TextPaint;FLandroid/text/TextUtils$TruncateAt;)Ljava/lang/CharSequence;", True, False), ("(Ljava/lang/CharSequence;Landroid/text/TextPaint;FLandroid/text/TextUtils$TruncateAt;ZLandroid/text/TextUtils$EllipsizeCallback;)Ljava/lang/CharSequence;", True, False)])
    equals = JavaStaticMethod("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z")
    getChars = JavaStaticMethod("(Ljava/lang/CharSequence;II[CI)V")
    indexOf = JavaMultipleMethod([("(Ljava/lang/CharSequence;CII)I", True, False), ("(Ljava/lang/CharSequence;CI)I", True, False), ("(Ljava/lang/CharSequence;C)I", True, False), ("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;I)I", True, False), ("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;II)I", True, False), ("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)I", True, False)])
    regionMatches = JavaStaticMethod("(Ljava/lang/CharSequence;ILjava/lang/CharSequence;II)Z")
    lastIndexOf = JavaMultipleMethod([("(Ljava/lang/CharSequence;CI)I", True, False), ("(Ljava/lang/CharSequence;C)I", True, False), ("(Ljava/lang/CharSequence;CII)I", True, False)])
    substring = JavaStaticMethod("(Ljava/lang/CharSequence;II)Ljava/lang/String;")
    isEmpty = JavaStaticMethod("(Ljava/lang/CharSequence;)Z")
    replace = JavaStaticMethod("(Ljava/lang/CharSequence;[Ljava/lang/String;[Ljava/lang/CharSequence;)Ljava/lang/CharSequence;")
    split = JavaMultipleMethod([("(Ljava/lang/String;Ljava/util/regex/Pattern;)[Ljava/lang/String;", True, False), ("(Ljava/lang/String;Ljava/lang/String;)[Ljava/lang/String;", True, False)])
    join = JavaMultipleMethod([("(Ljava/lang/CharSequence;[Ljava/lang/Object;)Ljava/lang/String;", True, False), ("(Ljava/lang/CharSequence;Ljava/lang/Iterable;)Ljava/lang/String;", True, False)])
    concat = JavaStaticMethod("([Ljava/lang/CharSequence;)Ljava/lang/CharSequence;", varargs=True)
    copySpansFrom = JavaStaticMethod("(Landroid/text/Spanned;IILjava/lang/Class;Landroid/text/Spannable;I)V")
    commaEllipsize = JavaStaticMethod("(Ljava/lang/CharSequence;Landroid/text/TextPaint;FLjava/lang/String;Ljava/lang/String;)Ljava/lang/CharSequence;")
    dumpSpans = JavaStaticMethod("(Ljava/lang/CharSequence;Landroid/util/Printer;Ljava/lang/String;)V")
    expandTemplate = JavaStaticMethod("(Ljava/lang/CharSequence;[Ljava/lang/CharSequence;)Ljava/lang/CharSequence;", varargs=True)
    getCapsMode = JavaStaticMethod("(Ljava/lang/CharSequence;II)I")
    getLayoutDirectionFromLocale = JavaStaticMethod("(Ljava/util/Locale;)I")
    getReverse = JavaStaticMethod("(Ljava/lang/CharSequence;II)Ljava/lang/CharSequence;")
    getTrimmedLength = JavaStaticMethod("(Ljava/lang/CharSequence;)I")
    htmlEncode = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    isDigitsOnly = JavaStaticMethod("(Ljava/lang/CharSequence;)Z")
    isGraphic = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Z", True, False), ("(C)Z", True, False)])
    listEllipsize = JavaStaticMethod("(Landroid/content/Context;Ljava/util/List;Ljava/lang/String;Landroid/text/TextPaint;FI)Ljava/lang/CharSequence;")
    makeSafeForPresentation = JavaStaticMethod("(Ljava/lang/String;IFI)Ljava/lang/CharSequence;")
    stringOrSpannedString = JavaStaticMethod("(Ljava/lang/CharSequence;)Ljava/lang/CharSequence;")
    writeToParcel = JavaStaticMethod("(Ljava/lang/CharSequence;Landroid/os/Parcel;I)V")
    getOffsetAfter = JavaStaticMethod("(Ljava/lang/CharSequence;I)I")
    getOffsetBefore = JavaStaticMethod("(Ljava/lang/CharSequence;I)I")

    class TruncateAt(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/TextUtils$TruncateAt"
        END = JavaStaticField("Landroid/text/TextUtils$TruncateAt;")
        MARQUEE = JavaStaticField("Landroid/text/TextUtils$TruncateAt;")
        MIDDLE = JavaStaticField("Landroid/text/TextUtils$TruncateAt;")
        START = JavaStaticField("Landroid/text/TextUtils$TruncateAt;")
        values = JavaStaticMethod("()[Landroid/text/TextUtils$TruncateAt;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/text/TextUtils$TruncateAt;")
        END = JavaStaticField("Landroid/text/TextUtils$TruncateAt;")
        MARQUEE = JavaStaticField("Landroid/text/TextUtils$TruncateAt;")
        MIDDLE = JavaStaticField("Landroid/text/TextUtils$TruncateAt;")
        START = JavaStaticField("Landroid/text/TextUtils$TruncateAt;")

    class StringSplitter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/TextUtils$StringSplitter"
        setString = JavaMethod("(Ljava/lang/String;)V")

    class SimpleStringSplitter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/TextUtils$SimpleStringSplitter"
        __javaconstructor__ = [("(C)V", False)]
        remove = JavaMethod("()V")
        iterator = JavaMethod("()Ljava/util/Iterator;")
        hasNext = JavaMethod("()Z")
        next = JavaMultipleMethod([("()Ljava/lang/Object;", False, False), ("()Ljava/lang/String;", False, False)])
        setString = JavaMethod("(Ljava/lang/String;)V")

    class EllipsizeCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/TextUtils$EllipsizeCallback"
        ellipsized = JavaMethod("(II)V")