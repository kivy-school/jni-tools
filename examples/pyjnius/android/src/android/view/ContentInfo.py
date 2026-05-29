from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentInfo"]

class ContentInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ContentInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_CONVERT_TO_PLAIN_TEXT = JavaStaticField("I")
    SOURCE_APP = JavaStaticField("I")
    SOURCE_AUTOFILL = JavaStaticField("I")
    SOURCE_CLIPBOARD = JavaStaticField("I")
    SOURCE_DRAG_AND_DROP = JavaStaticField("I")
    SOURCE_INPUT_METHOD = JavaStaticField("I")
    SOURCE_PROCESS_TEXT = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getClip = JavaMethod("()Landroid/content/ClipData;")
    getFlags = JavaMethod("()I")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getLinkUri = JavaMethod("()Landroid/net/Uri;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSource = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/ContentInfo$Builder"
        __javaconstructor__ = [("(Landroid/content/ClipData;I)V", False), ("(Landroid/view/ContentInfo;)V", False)]
        setLinkUri = JavaMethod("(Landroid/net/Uri;)Landroid/view/ContentInfo$Builder;")
        setClip = JavaMethod("(Landroid/content/ClipData;)Landroid/view/ContentInfo$Builder;")
        setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/ContentInfo$Builder;")
        setSource = JavaMethod("(I)Landroid/view/ContentInfo$Builder;")
        setFlags = JavaMethod("(I)Landroid/view/ContentInfo$Builder;")
        build = JavaMethod("()Landroid/view/ContentInfo;")