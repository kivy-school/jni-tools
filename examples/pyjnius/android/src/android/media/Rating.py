from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getStarRating = JavaMethod("()F")
    hasHeart = JavaMethod("()Z")
    isRated = JavaMethod("()Z")
    isThumbUp = JavaMethod("()Z")
    newHeartRating = JavaStaticMethod("(Z)Landroid/media/Rating;")
    newPercentageRating = JavaStaticMethod("(F)Landroid/media/Rating;")
    getRatingStyle = JavaMethod("()I")
    getPercentRating = JavaMethod("()F")
    newStarRating = JavaStaticMethod("(IF)Landroid/media/Rating;")
    newThumbRating = JavaStaticMethod("(Z)Landroid/media/Rating;")
    newUnratedRating = JavaStaticMethod("(I)Landroid/media/Rating;")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")