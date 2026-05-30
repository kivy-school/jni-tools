from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class Linkify(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/util/Linkify"
    __javaconstructor__ = [("()V", False)]
    ALL = JavaStaticField("I")
    EMAIL_ADDRESSES = JavaStaticField("I")
    MAP_ADDRESSES = JavaStaticField("I")
    PHONE_NUMBERS = JavaStaticField("I")
    WEB_URLS = JavaStaticField("I")
    sPhoneNumberMatchFilter = JavaStaticField("Landroid/text/util/Linkify$MatchFilter;")
    sPhoneNumberTransformFilter = JavaStaticField("Landroid/text/util/Linkify$TransformFilter;")
    sUrlMatchFilter = JavaStaticField("Landroid/text/util/Linkify$MatchFilter;")
    addLinks = JavaMultipleMethod([("(Landroid/text/Spannable;Ljava/util/regex/Pattern;Ljava/lang/String;[Ljava/lang/String;Landroid/text/util/Linkify$MatchFilter;Landroid/text/util/Linkify$TransformFilter;)Z", True, False), ("(Landroid/widget/TextView;Ljava/util/regex/Pattern;Ljava/lang/String;[Ljava/lang/String;Landroid/text/util/Linkify$MatchFilter;Landroid/text/util/Linkify$TransformFilter;)V", True, False), ("(Landroid/widget/TextView;I)Z", True, False), ("(Landroid/widget/TextView;Ljava/util/regex/Pattern;Ljava/lang/String;)V", True, False), ("(Landroid/widget/TextView;Ljava/util/regex/Pattern;Ljava/lang/String;Landroid/text/util/Linkify$MatchFilter;Landroid/text/util/Linkify$TransformFilter;)V", True, False), ("(Landroid/text/Spannable;Ljava/util/regex/Pattern;Ljava/lang/String;[Ljava/lang/String;Landroid/text/util/Linkify$MatchFilter;Landroid/text/util/Linkify$TransformFilter;Ljava/util/function/Function;)Z", True, False), ("(Landroid/text/Spannable;I)Z", True, False), ("(Landroid/text/Spannable;ILjava/util/function/Function;)Z", True, False), ("(Landroid/text/Spannable;Ljava/util/regex/Pattern;Ljava/lang/String;)Z", True, False), ("(Landroid/text/Spannable;Ljava/util/regex/Pattern;Ljava/lang/String;Landroid/text/util/Linkify$MatchFilter;Landroid/text/util/Linkify$TransformFilter;)Z", True, False)])

    class MatchFilter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/util/Linkify$MatchFilter"
        acceptMatch = JavaMethod("(Ljava/lang/CharSequence;II)Z")

    class TransformFilter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/util/Linkify$TransformFilter"
        transformUrl = JavaMethod("(Ljava/util/regex/Matcher;Ljava/lang/String;)Ljava/lang/String;")

class Rfc822Token(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/util/Rfc822Token"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V", False)]
    quoteNameIfNecessary = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    quoteComment = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    quoteName = JavaStaticMethod("(Ljava/lang/String;)Ljava/lang/String;")
    setAddress = JavaMethod("(Ljava/lang/String;)V")
    getComment = JavaMethod("()Ljava/lang/String;")
    setComment = JavaMethod("(Ljava/lang/String;)V")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    setName = JavaMethod("(Ljava/lang/String;)V")
    getAddress = JavaMethod("()Ljava/lang/String;")

class Rfc822Tokenizer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/util/Rfc822Tokenizer"
    __javaconstructor__ = [("()V", False)]
    tokenize = JavaMultipleMethod([("(Ljava/lang/CharSequence;Ljava/util/Collection;)V", True, False), ("(Ljava/lang/CharSequence;)[Landroid/text/util/Rfc822Token;", True, False)])
    findTokenEnd = JavaMethod("(Ljava/lang/CharSequence;I)I")
    terminateToken = JavaMethod("(Ljava/lang/CharSequence;)Ljava/lang/CharSequence;")
    findTokenStart = JavaMethod("(Ljava/lang/CharSequence;I)I")