from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Rating"]

class Rating(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/Rating"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RATING_3_STARS = JavaStaticField("I")
    RATING_4_STARS = JavaStaticField("I")
    RATING_5_STARS = JavaStaticField("I")
    RATING_HEART = JavaStaticField("I")
    RATING_NONE = JavaStaticField("I")
    RATING_PERCENTAGE = JavaStaticField("I")
    RATING_THUMB_UP_DOWN = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    newUnratedRating = JavaStaticMethod("(I)Landroid/media/Rating;")
    newHeartRating = JavaStaticMethod("(Z)Landroid/media/Rating;")
    newThumbRating = JavaStaticMethod("(Z)Landroid/media/Rating;")
    newStarRating = JavaStaticMethod("(IF)Landroid/media/Rating;")
    newPercentageRating = JavaStaticMethod("(F)Landroid/media/Rating;")
    isRated = JavaMethod("()Z")
    getRatingStyle = JavaMethod("()I")
    hasHeart = JavaMethod("()Z")
    isThumbUp = JavaMethod("()Z")
    getStarRating = JavaMethod("()F")
    getPercentRating = JavaMethod("()F")