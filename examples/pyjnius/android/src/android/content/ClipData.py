from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ClipData"]

class ClipData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ClipData"
    __javaconstructor__ = [("(Landroid/content/ClipDescription;Landroid/content/ClipData$Item;)V", False), ("(Ljava/lang/CharSequence;[Ljava/lang/String;Landroid/content/ClipData$Item;)V", False), ("(Landroid/content/ClipData;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    newHtmlText = JavaStaticMethod("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;Ljava/lang/String;)Landroid/content/ClipData;")
    newRawUri = JavaStaticMethod("(Ljava/lang/CharSequence;Landroid/net/Uri;)Landroid/content/ClipData;")
    newPlainText = JavaStaticMethod("(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Landroid/content/ClipData;")
    getItemAt = JavaMethod("(I)Landroid/content/ClipData$Item;")
    newUri = JavaStaticMethod("(Landroid/content/ContentResolver;Ljava/lang/CharSequence;Landroid/net/Uri;)Landroid/content/ClipData;")
    toString = JavaMethod("()Ljava/lang/String;")
    getItemCount = JavaMethod("()I")
    newIntent = JavaStaticMethod("(Ljava/lang/CharSequence;Landroid/content/Intent;)Landroid/content/ClipData;")
    getDescription = JavaMethod("()Landroid/content/ClipDescription;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    addItem = JavaMultipleMethod([("(Landroid/content/ClipData$Item;)V", False, False), ("(Landroid/content/ContentResolver;Landroid/content/ClipData$Item;)V", False, False)])

    class Item(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/ClipData$Item"
        __javaconstructor__ = [("(Landroid/content/Intent;)V", False), ("(Landroid/net/Uri;)V", False), ("(Ljava/lang/CharSequence;)V", False), ("(Ljava/lang/CharSequence;Landroid/content/Intent;Landroid/net/Uri;)V", False), ("(Ljava/lang/CharSequence;Ljava/lang/String;)V", False), ("(Ljava/lang/CharSequence;Ljava/lang/String;Landroid/content/Intent;Landroid/net/Uri;)V", False)]
        coerceToText = JavaMethod("(Landroid/content/Context;)Ljava/lang/CharSequence;")
        coerceToStyledText = JavaMethod("(Landroid/content/Context;)Ljava/lang/CharSequence;")
        coerceToHtmlText = JavaMethod("(Landroid/content/Context;)Ljava/lang/String;")
        getHtmlText = JavaMethod("()Ljava/lang/String;")
        getTextLinks = JavaMethod("()Landroid/view/textclassifier/TextLinks;")
        toString = JavaMethod("()Ljava/lang/String;")
        getUri = JavaMethod("()Landroid/net/Uri;")
        getIntentSender = JavaMethod("()Landroid/content/IntentSender;")
        getIntent = JavaMethod("()Landroid/content/Intent;")
        getText = JavaMethod("()Ljava/lang/CharSequence;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/content/ClipData$Item$Builder"
            __javaconstructor__ = [("()V", False)]
            setIntent = JavaMethod("(Landroid/content/Intent;)Landroid/content/ClipData$Item$Builder;")
            setUri = JavaMethod("(Landroid/net/Uri;)Landroid/content/ClipData$Item$Builder;")
            setIntentSender = JavaMethod("(Landroid/content/IntentSender;)Landroid/content/ClipData$Item$Builder;")
            setHtmlText = JavaMethod("(Ljava/lang/String;)Landroid/content/ClipData$Item$Builder;")
            build = JavaMethod("()Landroid/content/ClipData$Item;")
            setText = JavaMethod("(Ljava/lang/CharSequence;)Landroid/content/ClipData$Item$Builder;")