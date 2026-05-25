from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TvContentRating"]

class TvContentRating(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TvContentRating"
    UNRATED = JavaStaticField("Landroid/media/tv/TvContentRating;")
    createRating = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;)Landroid/media/tv/TvContentRating;", varargs=True)
    unflattenFromString = JavaStaticMethod("(Ljava/lang/String;)Landroid/media/tv/TvContentRating;")
    getDomain = JavaMethod("()Ljava/lang/String;")
    getRatingSystem = JavaMethod("()Ljava/lang/String;")
    getMainRating = JavaMethod("()Ljava/lang/String;")
    getSubRatings = JavaMethod("()Ljava/util/List;")
    flattenToString = JavaMethod("()Ljava/lang/String;")
    contains = JavaMethod("(Landroid/media/tv/TvContentRating;)Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")