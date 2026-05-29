from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClipDescription"]

class ClipDescription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ClipDescription"
    __javaconstructor__ = [("(Ljava/lang/CharSequence;[Ljava/lang/String;)V", False), ("(Landroid/content/ClipDescription;)V", False)]
    CLASSIFICATION_COMPLETE = JavaStaticField("I")
    CLASSIFICATION_NOT_COMPLETE = JavaStaticField("I")
    CLASSIFICATION_NOT_PERFORMED = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EXTRA_IS_REMOTE_DEVICE = JavaStaticField("Ljava/lang/String;")
    EXTRA_IS_SENSITIVE = JavaStaticField("Ljava/lang/String;")
    MIMETYPE_TEXT_HTML = JavaStaticField("Ljava/lang/String;")
    MIMETYPE_TEXT_INTENT = JavaStaticField("Ljava/lang/String;")
    MIMETYPE_TEXT_PLAIN = JavaStaticField("Ljava/lang/String;")
    MIMETYPE_TEXT_URILIST = JavaStaticField("Ljava/lang/String;")
    MIMETYPE_UNKNOWN = JavaStaticField("Ljava/lang/String;")
    compareMimeTypes = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)Z")
    getTimestamp = JavaMethod("()J")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    hasMimeType = JavaMethod("(Ljava/lang/String;)Z")
    filterMimeTypes = JavaMethod("(Ljava/lang/String;)[Ljava/lang/String;")
    getMimeTypeCount = JavaMethod("()I")
    getMimeType = JavaMethod("(I)Ljava/lang/String;")
    getExtras = JavaMethod("()Landroid/os/PersistableBundle;")
    setExtras = JavaMethod("(Landroid/os/PersistableBundle;)V")
    isStyledText = JavaMethod("()Z")
    getConfidenceScore = JavaMethod("(Ljava/lang/String;)F")
    getClassificationStatus = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")