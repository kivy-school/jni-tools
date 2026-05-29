from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TvContentRating"]

class TvContentRating(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TvContentRating"
    UNRATED = JavaStaticField("Landroid/media/tv/TvContentRating;")
    getMainRating = JavaMethod("()Ljava/lang/String;")
    createRating = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;)Landroid/media/tv/TvContentRating;", varargs=True)
    getRatingSystem = JavaMethod("()Ljava/lang/String;")
    getSubRatings = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    contains = JavaMethod("(Landroid/media/tv/TvContentRating;)Z")
    flattenToString = JavaMethod("()Ljava/lang/String;")
    unflattenFromString = JavaStaticMethod("(Ljava/lang/String;)Landroid/media/tv/TvContentRating;")
    getDomain = JavaMethod("()Ljava/lang/String;")