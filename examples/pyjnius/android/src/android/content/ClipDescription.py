from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClipDescription"]

class ClipDescription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ClipDescription"
    __javaconstructor__ = [("(Landroid/content/ClipDescription;)V", False), ("(Ljava/lang/CharSequence;[Ljava/lang/String;)V", False)]
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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getLabel = JavaMethod("()Ljava/lang/CharSequence;")
    setExtras = JavaMethod("(Landroid/os/PersistableBundle;)V")
    getExtras = JavaMethod("()Landroid/os/PersistableBundle;")
    getTimestamp = JavaMethod("()J")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    compareMimeTypes = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)Z")
    filterMimeTypes = JavaMethod("(Ljava/lang/String;)[Ljava/lang/String;")
    getClassificationStatus = JavaMethod("()I")
    getConfidenceScore = JavaMethod("(Ljava/lang/String;)F")
    getMimeType = JavaMethod("(I)Ljava/lang/String;")
    getMimeTypeCount = JavaMethod("()I")
    hasMimeType = JavaMethod("(Ljava/lang/String;)Z")
    isStyledText = JavaMethod("()Z")