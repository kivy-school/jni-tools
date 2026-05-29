from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Linkify"]

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
    addLinks = JavaMultipleMethod([("(Landroid/widget/TextView;I)Z", True, False), ("(Landroid/widget/TextView;Ljava/util/regex/Pattern;Ljava/lang/String;)V", True, False), ("(Landroid/widget/TextView;Ljava/util/regex/Pattern;Ljava/lang/String;Landroid/text/util/Linkify$MatchFilter;Landroid/text/util/Linkify$TransformFilter;)V", True, False), ("(Landroid/widget/TextView;Ljava/util/regex/Pattern;Ljava/lang/String;[Ljava/lang/String;Landroid/text/util/Linkify$MatchFilter;Landroid/text/util/Linkify$TransformFilter;)V", True, False), ("(Landroid/text/Spannable;Ljava/util/regex/Pattern;Ljava/lang/String;[Ljava/lang/String;Landroid/text/util/Linkify$MatchFilter;Landroid/text/util/Linkify$TransformFilter;Ljava/util/function/Function;)Z", True, False), ("(Landroid/text/Spannable;ILjava/util/function/Function;)Z", True, False), ("(Landroid/text/Spannable;Ljava/util/regex/Pattern;Ljava/lang/String;)Z", True, False), ("(Landroid/text/Spannable;Ljava/util/regex/Pattern;Ljava/lang/String;Landroid/text/util/Linkify$MatchFilter;Landroid/text/util/Linkify$TransformFilter;)Z", True, False), ("(Landroid/text/Spannable;Ljava/util/regex/Pattern;Ljava/lang/String;[Ljava/lang/String;Landroid/text/util/Linkify$MatchFilter;Landroid/text/util/Linkify$TransformFilter;)Z", True, False), ("(Landroid/text/Spannable;I)Z", True, False)])

    class MatchFilter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/util/Linkify$MatchFilter"
        acceptMatch = JavaMethod("(Ljava/lang/CharSequence;II)Z")

    class TransformFilter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/text/util/Linkify$TransformFilter"
        transformUrl = JavaMethod("(Ljava/util/regex/Matcher;Ljava/lang/String;)Ljava/lang/String;")