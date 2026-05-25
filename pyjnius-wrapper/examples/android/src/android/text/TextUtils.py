from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    getChars = JavaStaticMethod("(Ljava/lang/CharSequence;II[CI)V")
    indexOf = JavaMultipleMethod([("(Ljava/lang/CharSequence;C)I", True, False), ("(Ljava/lang/CharSequence;CI)I", True, False), ("(Ljava/lang/CharSequence;CII)I", True, False), ("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)I", True, False), ("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;I)I", True, False), ("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;II)I", True, False)])
    lastIndexOf = JavaMultipleMethod([("(Ljava/lang/CharSequence;C)I", True, False), ("(Ljava/lang/CharSequence;CI)I", True, False), ("(Ljava/lang/CharSequence;CII)I", True, False)])
    regionMatches = JavaStaticMethod("(Ljava/lang/CharSequence;ILjava/lang/CharSequence;II)Z")
    substring = JavaStaticMethod("(Ljava/lang/CharSequence;II)Ljava/lang/String;")
    join = JavaMultipleMethod([("(Ljava/lang/CharSequence;[Ljava/lang/Object;)Ljava/lang/String;", True, False), ("(Ljava/lang/CharSequence;Ljava/lang/Iterable;)Ljava/lang/String;", True, False)])
    split = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)[Ljava/lang/String;", True, False), ("(Ljava/lang/String;Ljava/util/regex/Pattern;)[Ljava/lang/String;", True, False)])
    stringOrSpannedString = JavaStaticMethod("(Ljava/lang/CharSequence;)Ljava/lang/CharSequence;")
    isEmpty = JavaStaticMethod("(Ljava/lang/CharSequence;)Z")
    getTrimmedLength = JavaStaticMethod("(Ljava/lang/CharSequence;)I")
    equals = JavaStaticMethod("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z")
    getReverse = JavaStaticMethod("(Ljava/lang/CharSequence;II)Ljava/lang/CharSequence;")
    writeToParcel = JavaStaticMethod("(Ljava/lang/CharSequence;Landroid/os/Parcel;I)V")
    dumpSpans = JavaStaticMethod("(Ljava/lang/CharSequence;Landroid/util/Printer;Ljava/lang/String;)V")
    replace = JavaStaticMethod("(Ljava/lang/CharSequence;[Ljava/lang/String;[Ljava/lang/CharSequence;)Ljava/lang/CharSequence;")
    expandTemplate = JavaStaticMethod("(Ljava/lang/CharSequence;[Ljava/lang/CharSequence;)Ljava/lang/CharSequence;", varargs=True)
    getOffsetBefore = JavaStaticMethod("(Ljava/lang/CharSequence;I)I")
    getOffsetAfter = JavaStaticMethod("(Ljava/lang/CharSequence;I)I")
    copySpansFrom = JavaStaticMethod("(Landroid/text/Spanned;IILjava/lang/Class;Landroid/text/Spannable;I)V")
    ellipsize = JavaMultipleMethod([("(Ljava/lang/CharSequence;Landroid/text/TextPaint;FLandroid/text/TextUtils$TruncateAt;)Ljava/lang/CharSequence;", True, False), ("(Ljava/lang/CharSequence;Landroid/text/TextPaint;FLandroid/text/TextUtils$TruncateAt;ZLandroid/text/TextUtils$EllipsizeCallback;)Ljava/lang/CharSequence;", True, False)])
    listEllipsize = JavaStaticMethod("(Landroid/content/Context;Ljava/util/List;Ljava/lang/String;Landroid/text/TextPaint;FI)Ljava/lang/CharSequence;")
    commaEllipsize = JavaStaticMethod("(Ljava/lang/CharSequence;Landroid/text/TextPaint;FLjava/lang/String;Ljava/lang/String;)Ljava/lang/CharSequence;")
    htmlEncode = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    concat = JavaStaticMethod("([Ljava/lang/CharSequence;)Ljava/lang/CharSequence;", varargs=True)
    isGraphic = JavaMultipleMethod([("(Ljava/lang/CharSequence;)Z", True, False), ("(C)Z", True, False)])
    isDigitsOnly = JavaStaticMethod("(Ljava/lang/CharSequence;)Z")
    getCapsMode = JavaStaticMethod("(Ljava/lang/CharSequence;II)I")
    getLayoutDirectionFromLocale = JavaStaticMethod("(Ljava/util/Locale;)I")
    makeSafeForPresentation = JavaStaticMethod("(Ljava/lang/String;IFI)Ljava/lang/CharSequence;")

    class EllipsizeCallback(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/TextUtils/EllipsizeCallback"
        ellipsized = JavaMethod("(II)V")

    class SimpleStringSplitter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/TextUtils/SimpleStringSplitter"
        __javaconstructor__ = [("(C)V", False)]
        setString = JavaMethod("(Ljava/lang/String;)V")
        iterator = JavaMethod("()Ljava/util/Iterator;")
        hasNext = JavaMethod("()Z")
        next = JavaMethod("()Ljava/lang/String;")
        remove = JavaMethod("()V")

    class StringSplitter(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/TextUtils/StringSplitter"
        setString = JavaMethod("(Ljava/lang/String;)V")

    class TruncateAt(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/TextUtils/TruncateAt"
        values = JavaStaticMethod("()[Landroid/text/TextUtils$TruncateAt;")
        valueOf = JavaStaticMethod("(Ljava/lang/String;)Landroid/text/TextUtils$TruncateAt;")
        START = JavaStaticField("Landroid/text/TextUtils/TruncateAt;")
        MIDDLE = JavaStaticField("Landroid/text/TextUtils/TruncateAt;")
        END = JavaStaticField("Landroid/text/TextUtils/TruncateAt;")
        MARQUEE = JavaStaticField("Landroid/text/TextUtils/TruncateAt;")