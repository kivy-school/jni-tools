from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class DisplayHashResultCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/displayhash/DisplayHashResultCallback"
    DISPLAY_HASH_ERROR_INVALID_BOUNDS = JavaStaticField("I")
    DISPLAY_HASH_ERROR_INVALID_HASH_ALGORITHM = JavaStaticField("I")
    DISPLAY_HASH_ERROR_MISSING_WINDOW = JavaStaticField("I")
    DISPLAY_HASH_ERROR_NOT_VISIBLE_ON_SCREEN = JavaStaticField("I")
    DISPLAY_HASH_ERROR_TOO_MANY_REQUESTS = JavaStaticField("I")
    DISPLAY_HASH_ERROR_UNKNOWN = JavaStaticField("I")
    onDisplayHashError = JavaMethod("(I)V")
    onDisplayHashResult = JavaMethod("(Landroid/view/displayhash/DisplayHash;)V")

class VerifiedDisplayHash(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/displayhash/VerifiedDisplayHash"
    __javaconstructor__ = [("(JLandroid/graphics/Rect;Ljava/lang/String;[B)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getHashAlgorithm = JavaMethod("()Ljava/lang/String;")
    getImageHash = JavaMethod("()[B")
    getTimeMillis = JavaMethod("()J")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getBoundsInWindow = JavaMethod("()Landroid/graphics/Rect;")

class DisplayHash(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/displayhash/DisplayHash"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class DisplayHashManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/displayhash/DisplayHashManager"
    getSupportedHashAlgorithms = JavaMethod("()Ljava/util/Set;")
    verifyDisplayHash = JavaMethod("(Landroid/view/displayhash/DisplayHash;)Landroid/view/displayhash/VerifiedDisplayHash;")